def count_vowels_consonants(sentence):
        vowels = "аеёиоуыэюя"
        consonants = "бвгджзйклмнпрстфхцчшщ"
        vowel_count = 0
        consonant_count = 0
        for i in sentence:
            if i.lower() in vowels:
                vowel_count += 1
            if i.lower() in consonants:
                consonant_count += 1
        print("Количество гласных букв:", vowel_count)
        print("Количество согласных букв:", consonant_count)

sentence ='Привет'
count_vowels_consonants(sentence)
