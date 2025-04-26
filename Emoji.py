usertext=input('How are you')
newusertext=usertext.split(' ')
print(newusertext)
def EmojisDic():
    Emojis= {
                'Happy' : '😂',
                'Sad': '😓'
    }


    result=''
    for feelin in newusertext:
            result += Emojis.get(feelin, feelin) + ' '
    return result

print(EmojisDic())

