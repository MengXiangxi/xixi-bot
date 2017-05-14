import itchat # itchat is hosted by github.com/littlecodersh/ItChat
        
@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
# decorator, locate xi^2 in group chat messages
def text_reply(msg):
    if msg['Text'].find('囍')>=0: # find xi^2
        print(msg['Text'])
        itchat.send(u'囍', msg['FromUserName']) # reply xi^2


itchat.auto_login(hotReload=True)
itchat.run()
