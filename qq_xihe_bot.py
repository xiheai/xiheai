import miraicle
from plugins import * 
import json
from threading import Thread
import os

# 读取配置文件
conf_file = open('qq_xihe_conf.json',encoding='utf-8')
conf = json.loads(conf_file.read())
conf_file.close()

# 机器人初始化
bot = miraicle.Mirai(qq=conf['bot_qq'], verify_key=conf['verify_key'], port=conf['port'])

def wx_bot():
    command = 'python3 wx_bot.py'
    os.system(command)

try:
    Thread(target=wx_bot).start()
    bot.run()
except KeyboardInterrupt:
    print('\nxihe 关闭咯~')