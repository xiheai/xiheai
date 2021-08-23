import miraicle
import asyncio
import sys
import os
import time
import json

admin = {
    "name" : "HailayLin",
    "qq" : 784298357
}

group = 189594977

# 发送信息给小冰
def send_msg_to_wx_xiaobing(msg: miraicle.FriendMessage):
    f = open('send_xiaobing.txt','w',encoding='utf-8')
    f.write(msg.plain)
    f.close()

# 获取小冰消息
def get_xiaobing_msg():
    f = open('send_xihe.txt',encoding='utf-8')
    xiaobing_rep = f.read()
    f.close()
    os.remove('send_xihe.txt')
    return xiaobing_rep

@miraicle.Mirai.receiver('FriendMessage')
def hello_to_friend(bot: miraicle.Mirai, msg: miraicle.FriendMessage):
    send_msg_to_wx_xiaobing(msg=msg)
    for _ in range(40):
        if os.path.exists('send_xihe.txt'):
            bot.send_friend_msg(qq=msg.sender, msg=get_xiaobing_msg())
            time.sleep(0.2)
        else:
            time.sleep(0.2)

@miraicle.Mirai.receiver('GroupMessage')
def hello_to_group(bot: miraicle.Mirai, msg: miraicle.FriendMessage):
    if msg.at_me():
        send_msg_to_wx_xiaobing(msg=msg)
        for _ in range(40):
            if os.path.exists('send_xihe.txt'):
                bot.send_group_msg(group=msg.group, msg=get_xiaobing_msg())
                time.sleep(0.2)
            time.sleep(0.2)
