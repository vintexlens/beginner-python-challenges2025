usertext=input('How are you')
newusertext=usertext.split(' ')
#def Emojis():
Emojis= {
            'Happy' : '😂',
            'Sad': '😓'
}


result=''
for feelin in newusertext:
        result += Emojis.get(feelin, feelin) + ' '

print(result)

