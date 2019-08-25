# telelog
Extension for tqdm progressbar and text logging in Telegram

# Installation
Now the project can not be found in PyPI

But you can install from git:

```
pip install git+https://github.com/pituganov/tg_tqdm
```

Before usage of lib you need to create `.telelog` file with bot token, chat id and proxy (optional).

Example:
```
TELELOG_BOT_TOKEN=TELEGRAM_BOT_TOKEN
TELELOG_CHAT_ID=CHAT_ID
# optional
TELELOG_PROXY=PROXY
```

# Usage
```
import time
from telelog import tqdm, send_text

for _ in tqdm(range(1000)):
    time.sleep(0.1)

send_text('Hello World')
```

# Tips

You can use this from different python scripts in parallel

![tg_tqdm_how_it_work](https://github.com/ermakovpetr/tg_tqdm/blob/master/tg_tqdm_how_it_work.gif?raw=true)

# What TELEGRAM_BOT_TOKEN and CHAT_ID?

You must create a bot that will send you the progress bar. **But it's easy!**

- **TELEGRAM_BOT_TOKEN**
1) Find *@BotFather* in Telegram
2) Follow the instructions to create a new bot.
Video guide:
![tg_tqdm_how_create_bot](https://github.com/ermakovpetr/tg_tqdm/blob/master/tg_tqdm_how_create_bot.gif?raw=true)

    in video my TELEGRAM_BOT_TOKEN is `639207352:AAFJKonqGVcHIkMHLm46h1UVH7mtU4xJD70`

- **CHAT_ID**
1) Open the chat with your new bot
2) Write to him `/start` and one more message
3) Run this code (where TELEGRAM_BOT_TOKEN from prev step)
```
import telepot
bot = telepot.Bot(TELEGRAM_BOT_TOKEN)
bot.getUpdates()[0]['message']['chat']['id']
```
4) Result is you CHAT_ID
