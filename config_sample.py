cookies = {
    'Hm': 'Hm_lvt_xxxx=abxxxxc; Hm_lpvt_xxxxx=xxxxx;',
    'XSRF-TOKEN': 'xxxxxx',
    'flomo_session': 'xxxxx',
}

notify_config = {
    'method': 'terminal-notifier',
    # 如果 method 不是 terminal-notifier，不必做以下配置
    'sound': 'Hero',
    'activate': 'com.google.Chrome.app.xxxxxxxx',
    'open': '',  # 如不需打开网页请设置为空字符串 ''
    'app_path': '/usr/local/Cellar/terminal-notifier/2.0.0/terminal-notifier.app/Contents/MacOS/terminal-notifier',  # 注意版本号
}

template = {
    'path': 'templates/daily.html',
    'time_format': '%Y%m%d',
}
