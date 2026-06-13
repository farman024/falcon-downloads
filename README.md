# 🦅 Falcon Downloads

A private, personal Telegram bot that downloads Instagram Reels instantly — no ads, no forced channel joins, no spam. Just paste the link and get the video.

> Built by [Farman J](https://github.com/farman024) — Indie Maker & AI Generalist

---

## ✨ Features

- 📸 Downloads Instagram Reels from public accounts
- 🔒 Private & owner-only — no one else can use it
- ⚡ 3 download methods with automatic fallback
- 🧹 Auto-deletes temp files after sending
- 🚫 Zero ads, zero forced follows, zero nonsense

---

## 🛠️ Tech Stack

| Layer | Tech |
|---|---|
| Language | Python 3 |
| Bot Framework | python-telegram-bot v21.5 |
| Downloader | instaloader + yt-dlp |
| Hosting | Local (Windows) |

---

## 🚀 Run Locally (Windows)

### Step 1 — Clone or Download
Download this repo as a ZIP and extract it to a folder on your PC.

### Step 2 — Add your Bot Token
Open `start_bot.bat` in Notepad and replace:
```
set BOT_TOKEN=your_bot_token_here
```
with your actual token from [@BotFather](https://t.me/BotFather).

### Step 3 — Run the Bot
Double-click `start_bot.bat` — the bot will install dependencies and start automatically.

Keep the terminal window open while using the bot. Minimize it and forget it's there!

### Step 4 — Test it
Open Telegram → message your bot → send `/start` → paste any Instagram Reel link!

---

## 📸 Supported Links

```
https://www.instagram.com/reel/xxxxx/
https://www.instagram.com/p/xxxxx/
```

> **Note:** Only public Instagram Reels are supported. Private accounts require login cookies.

---

## 🔒 Privacy & Security

- Bot Token stored locally — never in source code
- Only the owner's Telegram ID can use the bot
- All downloaded files are deleted immediately after sending

---

## 📁 Project Structure

```
falcon-downloads/
├── bot.py              # Main bot logic
├── requirements.txt    # Python dependencies
├── start_bot.bat       # One-click Windows startup script
├── cookies.txt         # YouTube auth cookies (optional)
├── Procfile            # Legacy Railway config
├── railway.toml        # Legacy Railway config
└── README.md           # This file
```

---

## 🗺️ Roadmap

- [ ] YouTube Shorts support (via residential proxy or RapidAPI)
- [ ] TikTok video download support
- [ ] Twitter/X video download support
- [ ] Download history log
- [ ] Audio-only extraction (MP3)

---

*Falcon Downloads — Built with 🦅 by Farman J · March 11, 2026*
