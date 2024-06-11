import re
regex = re.compile('\s+')
regex_num = re.compile('\d+')

text = """112 ИНФ  Информатика
 213 МАТ  Математика  
 156 АНГ  Английский"""

print(regex.split(text))
print(regex_num.findall(text),'\n',text)

s = regex_num.search(text)  
print('Первый индекс: ', s.start())  
print('Последний индекс: ', s.end())  
print(text[s.start():s.end()])
print(s.group())  
