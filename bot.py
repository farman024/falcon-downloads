import os
import re
import logging
import yt_dlp
import instaloader
from pathlib import Path
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
OWNER_ID = 1424116164  # Falcon Downloads — private bot

INSTAGRAM_PATTERN = re.compile(r'https?://(www\.)?instagram\.com/(reel|reels|p)/[\w\-]+')
YOUTUBE_PATTERN = re.compile(r'https?://(www\.)?(youtube\.com|youtu\.be)/\S+')

def is_supported_link(text: str):
    if INSTAGRAM_PATTERN.search(text):
        return "instagram"
    if YOUTUBE_PATTERN.search(text):
        return "youtube"
    return None

def extract_url(text: str, platform: str):
    if platform == "instagram":
        match = INSTAGRAM_PATTERN.search(text)
    else:
        match = YOUTUBE_PATTERN.search(text)
    return match.group(0) if match else None

def extract_shortcode(url: str):
    match = re.search(r'/(reel|reels|p)/([\w\-]+)', url)
    return match.group(2) if match else None

async def download_instagram(url: str, output_path: str) -> bool:
    shortcode = extract_shortcode(url)
    if not shortcode:
        return False

    L = instaloader.Instaloader(
        download_videos=True,
        download_video_thumbnails=False,
        download_geotags=False,
        download_comments=False,
        save_metadata=False,
        quiet=True,
        dirname_pattern="/tmp/insta_{shortcode}",
    )

    try:
        post = instaloader.Post.from_shortcode(L.context, shortcode)
        if not post.is_video:
            return False

        # Download directly using video_url
        import urllib.request
        urllib.request.urlretrieve(post.video_url, output_path)
        return True
    except Exception as e:
        logger.error(f"Instaloader error: {e}")
        return False

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != OWNER_ID:
        await update.message.reply_text("🔒 This is a private bot.")
        return

    text = update.message.text or ""
    platform = is_supported_link(text)

    if not platform:
        await update.message.reply_text(
            "Send me an Instagram Reel link and I'll download it for you! 🎬"
        )
        return

    url = extract_url(text, platform)
    status_msg = await update.message.reply_text("⏳ Downloading... please wait.")

    output_path = f"/tmp/{update.message.message_id}.mp4"
    success = False

    try:
        if platform == "instagram":
            success = await download_instagram(url, output_path)
            if not success:
                # Fallback to yt-dlp
                ydl_opts = {
                    "outtmpl": output_path,
                    "format": "best[ext=mp4]/best",
                    "quiet": True,
                    "no_warnings": True,
                    "http_headers": {
                        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15"
                    },
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                success = True
        else:
            ydl_opts = {
                "outtmpl": output_path,
                "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
                "quiet": True,
                "no_warnings": True,
                "merge_output_format": "mp4",
                "socket_timeout": 30,
                "cookiefile": os.path.join(os.path.dirname(os.path.abspath(__file__)), "cookies.txt"),
                "extractor_args": {"youtube": {"player_client": ["ios"]}},
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            success = True

        if not os.path.exists(output_path):
            for f in os.listdir("/tmp"):
                if str(update.message.message_id) in f:
                    output_path = f"/tmp/{f}"
                    break

        await status_msg.edit_text("📤 Uploading video...")

        with open(output_path, "rb") as video_file:
            await update.message.reply_video(
                video=video_file,
                supports_streaming=True,
                caption=f"✅ Downloaded from {'Instagram' if platform == 'instagram' else 'YouTube'}"
            )

        await status_msg.delete()

        if os.path.exists(output_path):
            os.remove(output_path)

    except Exception as e:
        logger.error(f"Download error: {e}")
        await status_msg.edit_text(
            "❌ Failed to download. The video might be private or the link is invalid.\n\nTry again with a different link."
        )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != OWNER_ID:
        await update.message.reply_text("🔒 This is a private bot.")
        return
    await update.message.reply_text(
        "👋 Hey! I'm your personal video downloader bot.\n\n"
        "Just send me:\n"
        "• 📸 Instagram Reel link\n\n"
        "And I'll send you the video — no ads, no spam, no BS. ✅"
    )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    from telegram.ext import CommandHandler
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    logger.info("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
    
