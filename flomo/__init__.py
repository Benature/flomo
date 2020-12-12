__version__ = '0.0.1-beta'


import platform
import requests
import json
import re
import os


class Flomo():
    def __init__(self, cookies):
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


def notify(title, message, subtitle='',
           sound='Hero',
           open='https://flomoapp.com/',
           method='',
           activate='',
           icon='https://i.loli.net/2020/12/06/inPGAIkvbyK7SNJ.png',
           terminal_notifier_path='terminal-notifier'):
    sysstr = platform.system()

    if sysstr == 'Darwin':  # macOS
        # print('macOS notification')
        if method == 'terminal-notifier':
            '''https://github.com/julienXX/terminal-notifier'''

            t = f'-title "{title}"'
            m = f'-message "{message}"'

            s = f'-subtitle "{subtitle}"'
            icon = f'-appIcon "{icon}"'
            sound = f'-sound "{sound}"'

            activate = '' if activate == '' else f'-activate "{activate}"'
            open = '' if open == '' else f'-open "{open}"'

            cmd = '{} {} '.format(terminal_notifier_path,
                                  ' '.join([m, t, s, icon, activate, open, sound]))
            os.system(cmd)
        else:
            os.system(
                f"""osascript -e 'display notification "{message}" with title "{title}"'""")
    elif sysstr == "Windows":
        print('TODO: windows notification')
    elif sysstr == "Linux":
        print('TODO: Linux notification')
