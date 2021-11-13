#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config
import requests


def run():
    r = requests.get(config.url, headers=config.headers)
    result = r.json()
    stores = result['stores']

    for store_key in config.stores:
        if store_key in stores:
            data = stores[store_key]
            #data['MLE63CH/A'] = {'availability': {'contract': False, 'unlocked': True}}
            for key in data:
                if data[key]['availability']['unlocked'] and key in config.iPhones:
                    store_name = config.stores[store_key]
                    name = config.iPhones[key]
                    message = '[ALERT] {} {}店铺有货!'.format(name, store_name)
                    ding(message)


def ding(message):
    '''发送钉钉通知'''
    params = {
        "msgtype": "text",
        "text": {
            "content": message,
        },
    }
    requests.post(config.dingtalk, json=params)



if __name__ == "__main__":
    run()
