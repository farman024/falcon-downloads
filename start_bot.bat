@echo off
title Falcon Downloads Bot
echo.
echo  ========================================
echo   FALCON DOWNLOADS BOT - Starting...
echo  ========================================
echo.

:: Set your Bot Token here
set BOT_TOKEN=your_bot_token_here

:: Install dependencies using python -m pip (ensures correct Python version)
echo Installing dependencies...
python -m pip install yt-dlp instaloader python-telegram-bot -q

echo.
echo  Bot is running! Don't close this window.
echo  Send a Reel link to @Falcon_Downloadsbot
echo.

:: Run the bot
python bot.py

pause
