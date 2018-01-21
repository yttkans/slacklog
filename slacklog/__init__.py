# coding: utf_8
import logging
import logging.handlers

__version__ = '1.0.0'

URL = 'https://slack.com/api/chat.postMessage'


class SlackHandler(logging.Handler):
    def __init__(self, auto_pre=False, **kwargs):
        super().__init__()
        import requests
        self._auto_pre = auto_pre
        self._params = kwargs
        self._session = requests.Session()

    def emit(self, record):
        d = dict(self._params)
        t = self.format(record)
        d['text'] = f'```{t[:3992]}```' if self._auto_pre else t[:4000]
        r = self._session.post(URL, data=d)
        r.raise_for_status()
        if not r.json()['ok']:
            raise Exception(r.text)
