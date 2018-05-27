from gtts import gTTS
from playsound import playsound as sound

user = input('what is you name')


tts = gTTS(text='hello ' + user, lang='en')
tts.save("hello.mp3")

sound('hello.mp3')

great = input('enter something nice')

tts = gTTS(text='i hope you had a fine day ' + great + ' ' + user, lang='en')
tts.save("greating.mp3")

sound('greating.mp3')