import re



def translate(text):
    Vowels_letters = "aeiouy"
    text = re.sub(r'([aeiouy])\1{2}',r'\1',text)
    text = re.sub('([^ aeiouy])[aeiouy]',r'\1',text)
    print text

translate("hoooowe yyyooouuu duoooiiine")