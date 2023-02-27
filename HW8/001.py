# 1. Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и
# выводить на печать построчно последние строки в количестве lines (на всякий случай проверим,
# что задано положительное целое число). Протестируем функцию на файле «article.txt» со следующим
# содержимым:

# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела

'''
def read_last(lines, file):
    if lines <= 0:
        print('Введено не целое и не положительно число!')
    else:    
        with open(file, 'r', encoding='utf-8') as text:
            file_lines = text.readlines()[-lines:]
        for line in file_lines:
            print(line.strip())
      
read_last(5, 'article.txt')
'''

# 2. Документ «article.txt» содержит следующий текст:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела

# Требуется реализовать функцию longest_words(file), которая выводит слово, имеющее максимальную длину
#  (или список слов, если таковых несколько).

def longest_words(file):
    with open(file, encoding='utf-8') as text:
        words = text.read().split()
        max_len = len(max(words, key=len))
        l_words = [word for word in words if len(word) == max_len]
        if len(l_words) == 1:
            return l_words[0]
        return l_words
  
print(longest_words('article.txt'))
            


