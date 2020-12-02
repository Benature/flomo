import os

from config import notify_config as nc

icon_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'media/logo-192x192.png')


def notify(title, message,
           subtitle='', sound=nc['sound'],
           open=nc['open'],
           activate=nc['activate'],
           icon=icon_path):
    '''https://github.com/julienXX/terminal-notifier'''

    t = f'-title "{title}"'
    s = f'-subtitle "{subtitle}"'
    m = f'-message "{message}"'
    icon = f'-appIcon "{icon}"'
    activate = f'-activate "{activate}"'
    sound = f'-sound "{sound}"'
    open = '' if open == '' else f'-open "{open}"'

    cmd = '{} {} '.format(nc['app_path'],
                          ' '.join([m, t, s, icon, activate, open, sound]))
    os.system(cmd)


def notify2(title, text):
    os.system(
        f"""osascript -e \'display notification "{text}" with title "{title}"'""")
