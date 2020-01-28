from gtts import gTTS 
# from playsound import playsound

language = 'en'


def TTF(filename, text):
        """
        Will save create and save a text to speech file
        Parameters:
        filename - str, name of file without extension
        text - str, what the file will say
        """
        voice = gTTS(text=text, lang = language, slow = False)
        voice.save(filename)

prompts ={}
# prompts['leftClear'] = 'The left side of the vehicle is now clear for exit'
# prompts['leftBlocked'] = 'The left side of the vehicle is not clear for exit'
# prompts['rightClear'] = 'The right side of the vehicle is now clear for exit'
# prompts['rightBlocked'] = 'The right side of the vehicle is not clear for exit'
prompts['wait'] = 'Wait'

for filename in prompts:
    name  = filename + '.mp3'
    TTF(name, prompts[filename])
#     playsound(name)
    break



