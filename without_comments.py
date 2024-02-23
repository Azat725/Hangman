from random import choice

print("Hello to Hangman!")
print("You should guess the secret word, you have 5 guesses")

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

def choice_category() -> str:
    print("Choose a category")
    for category in word_dict.keys():
        print(f"- {category}")
    category = input("Category -> ").title()
    return category

category = choice_category()
secret_word = choice(word_dict[category])
display_word = ["_" for _ in secret_word]

print(' '.join(display_word))

guesses = 0
game_over = False

while not game_over:
    guess = input("Enter a letter -> ").lower()
    
    if guess not in secret_word:
        guesses += 1
        guesses_left = 5 - guesses
        print(f"Incorrect! Now you have {guesses_left} guesses left")
        
        if guesses == 5:
            print(f"You Looser! The word is {secret_word}")
            game_over = True
            break
        
    for index, letter in secret_word:
        if letter == guess:
            display_word[index] = guess
            
    print(f"Word -> {''.join(display_word)}")
    
    if "_" not in display_word:
        print(f"You Win! The Word is {secret_word}")
        game_over = True
        break
