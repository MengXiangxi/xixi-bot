import itchat # itchat is hosted by github.com/littlecodersh/ItChat
        
@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
# decorator, locate xi^2 in group chat messages
def text_reply(msg):
    if msg['Text'].find('peiyangium')>=0 or msg['Text'].find('院士')>=0:
        if msg['Text'].find('囍')>=0:
            itchat.send_img('bad.png', msg['FromUserName'])
        itchat.send(u'给我自己+1 s', msg['FromUserName'])
    elif msg['Text'].find('囍')>=0: # find xi^2
        print(msg['Text'])
        n = msg['Text'].count(u'囍')
        if n>1:
            itchat.send(u'囍'*(n+1), msg['FromUserName']) # reply xi^2
        else:
            itchat.send(u'囍', msg['FromUserName'])


itchat.auto_login(hotReload=True)
itchat.run()
