# -*- coding: utf-8 -*-

import os
import json
import subprocess


def get_windows_username():
    return os.environ.get('USERNAME')


def main():
    global GITHUB_LOCAL
    username = get_windows_username()
    file_path = f'C:\\Users\\{username}\\AppData\\Local\\JetBrains\\Toolbox\\apps\\PyCharm-C\\ch-0\\.history.json'

    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            history_list = data.get('history', [])
            for item in history_list:
                if 'system-install-path' in item['item']:
                    path = item['item']['system-install-path']
                    subprocess.Popen(f"{path}\\bin\\pycharm64.exe {GITHUB_LOCAL}", shell=True)


if __name__ == '__main__':
    GITHUB_LOCAL = 'D:\\code\\github\\kaffa\\kaffa.github.io'
    main()
