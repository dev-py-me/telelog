import telepot
from os import environ
from tqdm import tqdm as default_tqdm
from datetime import datetime

TOKEN = environ['TELELOG_BOT_TOKEN']
CHAT_ID = environ['TELELOG_CHAT_ID']

if 'TELELOG_PROXY' in environ:
    PROXY = environ['TELELOG_PROXY']
    telepot.api.set_proxy(PROXY)


class _TqdmIO:
    def __init__(self, show_last_update=True):
        self.bot = telepot.Bot(TOKEN)
        self.prev_text = '<< Init tg_tqdm bar >>'
        self.text = self.prev_text
        self.show_last_update = show_last_update
        self.message = self.bot.sendMessage(
            CHAT_ID, self.text)

    def write(self, s: str):
        new_text = s.strip().replace('\r', '')
        if len(new_text) != 0:
            self.text = new_text

    def flush(self):
        if self.prev_text != self.text:
            if '%' in self.text:
                self.bot.editMessageText(
                    telepot.message_identifier(self.message),
                    self.text)
                self.prev_text = self.text


class _PlainTextIO:
    def __init__(self):
        self.bot = telepot.Bot(TOKEN)

    def send_text(self, text: str) -> None:
        self.message = self.bot.sendMessage(CHAT_ID, text)


def send_text(text: str) -> None:
    tg_io = _PlainTextIO()
    tg_io.send_text(text)


def tqdm(iterable, show_last_update=True,
         desc=None, total=None, leave=True, ncols=None, mininterval=1.0, maxinterval=10.0,
         miniters=None, ascii=False, disable=False, unit='it',
         unit_scale=False, dynamic_ncols=False, smoothing=0.3,
         bar_format=None, initial=0, position=None, postfix=None,
         unit_divisor=1000, gui=False, **kwargs):
    tg_io = _TqdmIO(show_last_update)
    return default_tqdm(
        iterable=iterable,
        desc=desc,
        total=total,
        leave=leave,
        file=tg_io,
        ncols=ncols,
        mininterval=mininterval,
        maxinterval=maxinterval,
        miniters=miniters,
        ascii=ascii,
        disable=disable,
        unit=unit,
        unit_scale=unit_scale,
        dynamic_ncols=dynamic_ncols,
        smoothing=smoothing,
        bar_format=bar_format,
        initial=initial,
        position=position,
        postfix=postfix,
        unit_divisor=unit_divisor,
        gui=gui,
        **kwargs)
