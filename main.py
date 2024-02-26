# Импортируем фукцию choice, для выбора рандомного слова из списка слов
from random import choice

# Выводим приветственное сообщение
print("Hello to Hangman!")
print("You should guess the secret word, you have 5 guesses")

# Создаем словарь с ключами - категориями слов, значение - список слов
# Animals - ключ
# Список со словами - значение
word_dict = {
    "Animals": [
        "elephant", 
        "tiger", 
        "dog", 
        "cat", 
        "lion"
    ],
    "Fruits": [
        "apple", 
        "banana", 
        "orange", 
        "pear", 
        "strawberry"
    ]
}

# Определяем функцию для выбора категорий
def choice_category() -> str:
    print("Choose a category")
    # Проходимся циклом for по ключам словоря - категориям и выводим их на экран
    for category in word_dict.keys():
        print(f"- {category}")
    # Получаем выбранную пользователем категорию и приводим ее к верхнему регистру 
    category = input("Category -> ").title()
    return category

# Вызываем функцию для выбора категорий 
category = choice_category()
# Берем рандомное слово из выбранной категории 
secret_word = choice(word_dict[category])
# Создаем список для отображения отгаданных букв в слове
display_word = ["_" for _ in secret_word]

# Выводим на экран загаданное слово с пустыми местами для букв
print(' '.join(display_word))

# Иницилизируем переменную - счетчик для подсчета неверных попыток 
guesses = 0
max_guesses = 5
# Инициализируем переменную для отслеживания завершения игры
game_over = False

while not game_over and guesses < max_guesses:
    # Пользователь вводит букву и преобразуем ее в нижний регистр
    guess = input("Enter a letter -> ").lower()
    
    # Проверяем, содержится ли угаданная буква в секретном слове
    if guess not in secret_word:
        # Если буква не угадана, увеличиваем счетчик неверных попыток
        guesses += 1
        
        if guesses == 1:
            print("You hear the crowd")
        elif guesses == 2:
            print("You are being taken to the podium")
        elif guesses == 3:
            print("You're saying the last words.")
        elif guesses == 4:
            print("They're putting a rope around your neck")
        
        # Если количество неверных попыток достигло 5, сообщаем о поражении и показываем загаданное слово
        if guesses == max_guesses:
            print(f"You were hanged! The word is {secret_word}, but it won't help you")
            game_over = True
            break
        
    # Проверяем каждую букву в секретном слове
    for index, letter in enumerate(secret_word):
        # Если угаданная буква равна букве в секретном слове, обновляем отображаемое слово
        if letter == guess:
            display_word[index] = guess
            
    # Выводим отображаемое слово с угаданными буквами и пустыми местами
    print(f"Word -> {''.join(display_word)}")
    
    # Проверяем, все ли буквы угаданы; если да, сообщаем о победе и показываем секретное слово
    if "_" not in display_word:
        print(f"You Win! The Word is {secret_word}")
        game_over = True