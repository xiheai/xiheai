import itchat
import json
import asyncio
import websockets
import os
from threading import Thread
import time

itchat.auto_login(hotReload=True)

xiaobing_rep = ''

@itchat.msg_register([itchat.content.PICTURE,itchat.content.VOICE])
def download_files(msg):
    print(msg,'\n')
    print(msg.fileName)
    msg.download('data/'+ msg.fileName)
    itchat.send('@%s@%s' % (
        'img' if msg['Type'] == 'Picture' else 'fil', msg['FileName']),
        msg['FromUserName'])
    #return '%s received' % msg['Type']


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    if msg['ToUserName'] == 'filehelper':
        itchat.send(u'pong', 'filehelper')
        print('pong')

@itchat.msg_register(itchat.content.TEXT, isMpChat=True)
def mp_chat(msg):
    global xiaobing_rep
    if msg['FromUserName'] == itchat.search_mps(name='AI小冰')[0]['UserName']:
        print("小冰说：", msg['Content'])
        send_msg_to_qq_xihe(msg=msg)

    if msg['FromUserName'] == itchat.search_friends()['UserName']:
        print('我说：',msg['Content'])

# 发送信息给qq xihe
def send_msg_to_qq_xihe(msg):
    f = open('send_xihe.txt','w',encoding='utf-8')
    f.write(msg['Content'])
    f.close()

# print(itchat.search_mps(name='AI小冰')[0]['UserName'])
# print(itchat.search_friends()['UserName'])

def xiaobing_rev(time_delay = 0.1):
    while True:
        if os.path.exists('send_xiaobing.txt'):
            itchat.send_msg(get_xihe_msg(), itchat.search_mps(name='AI小冰')[0]['UserName'])
        else:
            time.sleep(time_delay)


def get_xihe_msg():
    f = open('send_xiaobing.txt',encoding='utf-8')
    xihe_send = f.read()
    f.close()
    os.remove("send_xiaobing.txt")
    return xihe_send


t = Thread(target=xiaobing_rev)
t.start()

itchat.run()
