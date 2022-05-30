couple_words = int(input('Введите количество пар слов: '))
main_dict = {}

for i_num in range(couple_words):
    word_fst, snd_word = input(f' {i_num + 1} пара: ').split(' - ')
    main_dict[word_fst] = snd_word

synonim = input('\nВведите слово: ').lower()

print('Синоним:', main_dict.get(synonim) or ''.join([word_fst \
                                                     for word_fst, snd_word in main_dict.items() if
                                                     snd_word == synonim]) or 'Такого слова в словаре нет')