# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from ftplib import FTP


def get_data_init():
    with open('exchange_kst.ini', 'r') as in_f:
        global data_init
        data_init = json.load(in_f)
        in_f.close
        if len(data_init) > 0:
            return True
        else:
            return False


def ftp_connect():
    global ftp
    ftp_conf = data_init['ftp']
    # соединение
    try:
        ftp = FTP(host=ftp_conf['host'],
                  user=ftp_conf['user'],
                  passwd=ftp_conf['password'])
        files_list = ftp.nlst()
        if ftp_conf['cwd'] in files_list:
            try:
                ftp.cwd('Poly6')
            except Exception as E:
                print('FTP "cwd" error: {err}'.format(err=E))
                return False
        return True
    except Exception as E:
        print('FTP connect error: {err}'.format(err=E))
        return False


def email_connect():
    return False


def start():
    if not get_data_init():
        print('Ошибка инициализации!')
        return

    if data_init['type'] == 'ftp':
        result = ftp_connect()
    elif data_init['type'] == 'email':
        result = email_connect()

    if result:
        print('OK connect')
    else:
        print('Error connect')

    # закрыть ftp соединеие
    ftp.quit


if __name__ == '__main__':
    start()
    # if len(sys.argv) != 2:
    #    print('Отсутствует парамтр - файл обработки')
