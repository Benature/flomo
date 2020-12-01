from bs4 import BeautifulSoup as bs
import requests
import json
import sys

from notify import notify
from flomo import Flomo

cmd = sys.argv[1].split(' ')
url = cmd[0]
# url = 'https://www.xiaoyuzhoufm.com/episode/5e280fab418a84a0461fa936?s=eyJ1IjoiNWVmMWM2YTBiMzY1ZmE4MzI0OWIzZWNhIn0%3D%0A'
if len(cmd) > 1:
    paste = cmd[1]
else:
    paste = ''

session = requests.session()


def get_xyz(url):
    response = session.get(url)
    soup = bs(response.text, 'lxml')

    title = soup.select('.title')[1].text
    title = title.lstrip('# ').strip(' .')
    podcaster = soup.select('.name')[0].text.strip().replace(' ', '')

    url_clip = url.split('?')[0]
    content = f'''[<strong><u>{title}</u></strong>]({url_clip} ) #podcaster/{podcaster}
    #播客/
    '''
    return content, title


content, title = get_xyz(url)
content_html = ''.join([f'<p>{c}</p>' for c in content.split('\n')])


if len(paste) > 0:
    import richxerox
    richxerox.copy(html=content_html)
    notify("小宇宙👉剪贴板", title)
else:
    flomo = Flomo()
    response = flomo.new(content_html)
    response_json = json.loads(response.text)
    if response.status_code == 200:
        if response_json['code'] == 0:
            notify("小宇宙👉flomo", title)
        else:
            notify("🚨 flomo Error", response_json['message'])
    else:
        notify("🚨 flomo Failed", response_json['message'])
