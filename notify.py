import os

from config import notify_config as nc

icon_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'logo-192x192.png')


def notify(title, message,
           subtitle='', sound=nc['sound'],
           activate=nc['activate'],
           icon=icon_path):
    '''https://github.com/julienXX/terminal-notifier'''

    t = f'-title "{title}"'
    s = f'-subtitle "{subtitle}"'
    m = f'-message "{message}"'
    icon = f'-appIcon "{icon}"'
    activate = f'-activate "{activate}"'
    sound = f'-sound "{sound}"'

    cmd = '/usr/local/Cellar/terminal-notifier/2.0.0/terminal-notifier.app/Contents/MacOS/terminal-notifier {} '.format(
        ' '.join([m, t, s, icon, activate, sound]))
    os.system(cmd)


def notify2(title, text):
    os.system(
        f"""osascript -e \'display notification "{text}" with title "{title}"'""")
