__version__ = '0.0.3-alpha'


import platform
import requests
import json
import re
import os


class Flomo():
    def __init__(self, api=None, cookies=None):
        if api is None and cookies is None:
            raise Exception('please input api or cookies')

        self.api = api
        self.cookies = cookies
        self.session = requests.session()
        if cookies:
            cookies_tmp = self.cookies['Hm'] + \
                '; XSRF-TOKEN=' + self.cookies['XSRF-TOKEN'] + \
                '; flomo_session='+self.cookies['flomo_session']
            self.headers = {
                'Content-Type': 'application/json;charset=UTF-8',
                'Cookie': cookies_tmp,
                'X-Requested-With': 'XMLHttpRequest',
                'X-XSRF-TOKEN': self.cookies['XSRF-TOKEN'],
            }
        else:
            self.headers = None

    def get(self, tag=''):
        '''get all memo'''
        if self.cookies is not None:
            # headers = {
            #     'cookie': self.cookies['Hm'],
            #     'X-Requested-With': 'XMLHttpRequest',
            # }
            if tag:
                url = f'https://flomoapp.com/api/memo/?tag={tag.strip("#")}'
            else:
                url = 'https://flomoapp.com/api/memo/'
            response = self.session.get(url, headers=self.headers, json={})
            # response.encoding = 'utf-8'
            # get_cookies = response.headers['Set-Cookie']
            return json.loads(response.text)
        else:
            print('this method is not supported officially yet.')

    def update(self, slug, content, file_ids=[], parent_memo_slug=None, source='web'):
        '''update a memo'''
        payload = {
            'content': content,
            'file_ids': file_ids,
            'parent_memo_slug': parent_memo_slug,
            'source': source,
        }
        response = self.session.put(f'https://flomoapp.com/api/memo/{slug}/',
                                    headers=self.headers, json=payload)
        return response

    def new(self, content, parent_memo_id=None, file_ids=[], source='web', method='api'):
        '''put a new memo
        content: memo content
        method: `api` or `cookies`, determine the method to send the new memo

        return response'''
        if self.api is not None and method == 'api':
            response = self.session.post(
                self.api,
                headers={'Content-Type': 'application/json'},
                json={'content': content})
        else:
            payload = {
                "content": content,
                "file_ids": file_ids,
                "parent_memo_id": parent_memo_id,
                "source": source
            }

            response = self.session.put('https://flomoapp.com/api/memo/',
                                        headers=self.headers, json=payload)
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
