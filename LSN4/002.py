# Пользователь вводит тескт (строка). 
# Словом считается последовательность непробельных символов идущих подряд , слова разделены одним или 
# большим числом пробелов или символами конца строки. Определите, сколько различных слов содержится
# в этом тексте. 

text = set(input('Введите текст: ').split())
print(f'В нашем тексте {len(text)} уникальных слов')