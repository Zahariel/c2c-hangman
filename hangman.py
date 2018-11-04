hangman_parts = [ "head", "left arm", "torso", "right arm", "left leg", "right leg" ]
num_wrong_guesses_allowed = len(hangman_parts)
words = [
    "apple",
    "butterfly",
    "car",
    "pajama",
    "kayak",
    "zigzag",
    "zombie",
    "oxygen",
    "able",
    "baby",
    "lock",
    "ornament",
    "quality",
    "liquid",
    "suggestion",
    "weather",
    "twist"
    ]

def draw_hangman(num_wrong_guesses):
    if num_wrong_guesses > num_wrong_guesses_allowed:
        num_wrong_guesses = num_wrong_guesses_allowed

    hangman_characters = {
        "head" : "  O",
        "left arm" : " /",
        "torso" : "|",
        "right arm" : "\\",
        "left leg" : " /",
        "right leg" : " \\"
    }
    hangman_newlines = [ "head", "right arm", "right leg" ]

    output = " _____\n |   |\n | "
    num_newlines = 0
    for i in range(num_wrong_guesses):
        output = output + hangman_characters[hangman_parts[i]]
        if hangman_parts[i] in hangman_newlines:
            output = output + "\n | "
            num_newlines = num_newlines + 1
    for i in range(len(hangman_newlines) - num_newlines):
        output = output + "\n |"
    output = output + "____\n\n"
    print(output)

def check_if_done(guesses, word):
    for letter in word:
        if letter not in guesses:
            return False
    return True


word = "test"
wrong_guesses = 0
all_guesses = []
done = False

while not done and wrong_guesses < num_wrong_guesses_allowed:
    draw_hangman(wrong_guesses)
    guess = input("Guess a letter: ")
    all_guesses.append(guess)
    if guess in word:
        print("That's right!")
        done = check_if_done(all_guesses, word)
    else:
        print("Nope, sorry!")
        wrong_guesses = wrong_guesses + 1

if wrong_guesses == num_wrong_guesses_allowed:
    draw_hangman(wrong_guesses)
    print("You've been hanged! The word was", word)
else:
    print("Nice going! You got it!")

