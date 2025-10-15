# Напишите программу, которая добавляет ‘ing’ в конец слов (к каждому слову) в тексте
# “Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl,
# facilisis vitae semper at, dignissim vitae libero” и после этого выводит получившийся
# текст на экран. Знаки препинания не должны оказаться внутри слова. Если после слова
# идет запятая или точка, этот знак препинания должен идти после того же слова,
#  но уже преобразованного.

my_text = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, " \
    "facilisis vitae semper at, dignissim vitae libero"
my_list = my_text.split()

fin_text = []
for word in my_list:
    if word[-1] in [",", "."]:  # поиск слов у которых на конце знаки припинания
        # Добавляем 'ing' к словам, пропуская знаки препинания.
        new_word = fin_text.append(word[:-1] + "ing" + word[-1])
    else:
        # Добавляем 'ing' к словам, у которых нет знаков препинания.
        fin_text.append(word + "ing")

print(' '.join(fin_text))
