import itchat # itchat is hosted by github.com/littlecodersh/ItChat
import time
import datetime
import codecs
        
@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
# decorator, locate xi^2 in group chat messages
def text_reply(msg):
    # Declear global parameters
    global second
    global buffer
    global grouplist
    # Get new msg
    try:
        msgcontent = msg['ActualNickName']+" "+\
              msg['Text']+" "+datetime.datetime.now().strftime('%H:%M:%S')
    except:
        msgcontent = '#UNKOWN#'
    # Output to screen
    try:
        print(msgcontent)
    except:
        print('#ParsingError#')
    # Add to buffer
    buffer.append(msgcontent)
    # Output to file
    if len(buffer)>5:
        with codecs.open('WechatMessage.txt','a','utf-8') as rec:
            for i in buffer:
                try:
                    rec.write(i+'\r\n')
                except:
                    rec.write('error!\r\n')
                    print('==>ERROR!'+i)
            buffer = []
        # Save second
        with open('second.txt','w') as secrec:
            secrec.write(str(second))
    # Process start message
    if msg['Text'].strip()=='请州长夫人演唱':
        if (msg['ToUserName'].find('@@')>=0 and (msg['ToUserName'] in grouplist) == False):
            grouplist.append(msg['ToUserName'])
            itchat.send('进入囍bot模式！请发囍……', msg['ToUserName'])
        elif (msg['FromUserName'] in grouplist) == False:
            grouplist.append(msg['FromUserName'])
            itchat.send('进入囍bot模式！请发囍……', msg['FromUserName'])
    # Process end message
    if msg['Text'].strip()=='院士最帅！':
        if (msg['ToUserName'].find('@@')>=0):
            grouplist.remove(msg['ToUserName'])
        else:
            itchat.send('过奖过奖！', msg['FromUserName'])
            grouplist.remove(msg['FromUserName'])
    if (msg['FromUserName'] in grouplist) == False:
        return
    # Responses starts here:
    if msg['Text'].find('八月')>=0:
        itchat.send("%s和八月在一起！"%msg["ActualNickName"],msg['FromUserName'])
    elif msg['Text'].find('peiyangium')>=0 or msg['Text'].find('院士')>=0:
        if msg['Text'].find('z')>=0:
            itchat.send('你才是z!', msg['FromUserName'])
        elif msg['Text'].find('囍')>=0:
            itchat.send('@img@bad.png', msg['FromUserName'])
        else:
            itchat.send(u'给我自己+1 s', msg['FromUserName'])
            second += 1
            print(second)
            if second%10 == 0:
                itchat.send(u'已经加了%i秒了！'%second,msg['FromUserName'])
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
with open('second.txt','r') as secrec:
    second = int(secrec.read().strip())
buffer = []
itchat.auto_login(hotReload=True)
itchat.run()
