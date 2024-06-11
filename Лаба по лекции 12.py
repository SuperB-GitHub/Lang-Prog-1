import re
def zadan1():
    regex = re.compile('abcdefghijklmnopqrstuv18340')
    text1='abcdefghijklmnopqrstuv18340'
    text2='abcdefghijklmnoasdfasdpqrstuv18340'
    print(regex.search(text1).group())
    print(regex.search(text2))

def zadan2():
    # regex=re.compile()
    txt1='e02fd0e4-00fd-090A-ca30-0d00a0038ba0'
    txt2='e02fd0e400fd090Aca300d00a0038ba0'
    print(re.findall('-',txt1))
    print(re.findall('-',txt2))

zadan2()