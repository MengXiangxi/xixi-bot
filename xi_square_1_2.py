mport itchat # itchat is hosted by github.com/littlecodersh/ItChat
import time
import datetime
        
@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
# decorator, locate xi^2 in group chat messages
def text_reply(msg):
    try:
        print(msg['ActualNickName'],\
              msg['Text'],datetime.datetime.now().strftime('%H:%M:%S'))
    except:
        print('#UNKOWN#')
    if msg['Text'].strip()=='请州长夫人演唱':
        if (msg['ToUserName'].find('@@')>=0 and (msg['ToUserName'] in grouplist) == False):
            grouplist.append(msg['ToUserName'])
            itchat.send('进入囍bot模式！请发囍……', msg['ToUserName'])
        elif (msg['FromUserName'] in grouplist) == False:
            grouplist.append(msg['FromUserName'])
            itchat.send('进入囍bot模式！请发囍……', msg['FromUserName'])
    if msg['Text'].strip()=='院士最帅！':
        if (msg['ToUserName'].find('@@')>=0):
            grouplist.remove(msg['ToUserName'])
        else:
            itchat.send('过奖过奖！', msg['FromUserName'])
            grouplist.remove(msg['FromUserName'])
    if (msg['FromUserName'] in grouplist) == False:
        return
    if msg['Text'].find('peiyangium')>=0 or msg['Text'].find('院士')>=0:
        if msg['Text'].find('z')>=0:
            itchat.send('你才是z!', msg['FromUserName'])
        elif msg['Text'].find('囍')>=0:
            itchat.send('@img@bad.png', msg['FromUserName'])
        else:
            itchat.send(u'给我自己+1 s', msg['FromUserName'])
    elif msg['Text'].find('囍')>=0: # find xi^2
        n = msg['Text'].count(u'囍')
        if msg['Text'].find('院')>=0 or msg['Text'].find('培')>=0 or msg['Text'].find('孟')>=0:
            itchat.send('@img@bad.png', msg['FromUserName'])
        elif msg['Text'].find('z')>=0:
            itchat.send('你才是z!', msg['FromUserName'])
        elif n>1 and n<10:
            itchat.send(u'囍'*(n+1), msg['FromUserName']) # reply xi^2
        elif n>1:
            itchat.send('@img@lengmo.jpg', msg['FromUserName'])
        else:
            itchat.send(u'囍', msg['FromUserName'])

grouplist = []
itchat.auto_login(hotReload=True)
itchat.run()
