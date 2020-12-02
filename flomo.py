import requests
import json
import re
import os

from datetime import datetime

from config import cookies, template as tc
from notify import notify

folder_path = os.path.dirname(os.path.abspath(__file__))


class Flomo():
    def __init__(self, cookies=cookies):
        self.cookies = cookies
        self.session = requests.session()

    def get(self):
        '''get all memo'''
        headers = {
            'cookie': self.cookies['Hm'],
            'X-Requested-With': 'XMLHttpRequest',
        }
        data = {}
        response = self.session.get('https://flomoapp.com/api/memo/',
                                    headers=headers, json=data)
        # response.encoding = 'utf-8'
        # get_cookies = response.headers['Set-Cookie']

        return json.loads(response.text)

    def new(self, content, parent_memo_id=None, file_ids=[], source='web'):
        '''put a new memo'''
        payload = {
            "content": content,
            "file_ids": file_ids,
            "parent_memo_id": parent_memo_id,
            "source": source
        }
        cookies_tmp = self.cookies['Hm'] + \
            '; XSRF-TOKEN=' + self.cookies['XSRF-TOKEN'] + \
            '; flomo_session='+self.cookies['flomo_session']
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Cookie': cookies_tmp,
            'X-Requested-With': 'XMLHttpRequest',
            'X-XSRF-TOKEN': self.cookies['XSRF-TOKEN'],
        }
        response = self.session.put('https://flomoapp.com/api/memo/',
                                    headers=headers, json=payload)
        return response


if __name__ == '__main__':
    import sys
    flomo = Flomo()

    if sys.argv[1] == 'new':
        content = sys.argv[2]
        if content == 't':
            # template
            from datetime import datetime
            today = datetime.now().strftime(tc['time_format'])

            with open(os.path.join(folder_path, tc['path']), 'r') as f:
                content = f.read()
            response = flomo.new(content.format(today))
            if response.status_code == 200:
                notify("flomo: memo template", today)
            else:
                notify("🚨 flomo Error", response)
        else:
            response = flomo.new(
                ''.join([f'<p>{c}</p>' for c in content.split('\n')]))
            if response.status_code == 200:
                notify("flomo: new memo", content)
            else:
                notify("🚨 flomo Error", response)
