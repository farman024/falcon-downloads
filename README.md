# 🎬 Personal Video Downloader Bot

Downloads Instagram Reels and YouTube Shorts — no ads, no spam.

## Deploy on Railway (from your phone)

### Step 1 — Upload to GitHub
1. Create a new GitHub repo (e.g. `my-dl-bot`)
2. Upload all 4 files: `bot.py`, `requirements.txt`, `Procfile`, `railway.toml`

### Step 2 — Deploy on Railway
1. Go to [railway.app](https://railway.app) on your phone
2. Sign up / login with GitHub
3. Click **New Project** → **Deploy from GitHub repo**
4. Select your repo
5. Go to **Variables** tab → Add:
   ```
   BOT_TOKEN = your_bot_token_here
   ```
6. Click **Deploy** ✅

### Step 3 — Test it
Open your bot on Telegram, send `/start`, then paste any Instagram Reel or YouTube Shorts link!

## Supported Links
- `https://www.instagram.com/reel/...`
- `https://www.youtube.com/shorts/...`
- `https://youtu.be/...`
