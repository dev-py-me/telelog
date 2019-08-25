from ._client import tqdm, send_text

__all__ = ['tqdm', 'send_text', '__version__']

version_info = 0, 0, 2

__version__ = '.'.join(map(str, version_info))
