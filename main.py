import pysrt
from googletrans import Translator
from os import listdir
from os.path import isfile, join


path = 'legendas'
files = [f for f in listdir(path) if isfile(join(path, f))]


translator = Translator()

for arch in files:
    subs = pysrt.open(str(path+'\\'+arch), encoding='iso-8859-1')
    count = 0
    print(str(path+'\\'+arch))
    for sub in subs:
        print(count)
        print(subs[count].text)
        tt = translator.translate('hello', src='en', dest='pt')
        print(tt.text)
        #subs[count].text = tt.text
        #subs.save(encoding='utf-8')
        count +=1

