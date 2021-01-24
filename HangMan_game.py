## Hanged Man game for Campus self.py course.

HANGMAN_ASCII_ART = """
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/"""

MAX_TRIES = 6

HANGMAN_PHOTOS = {
    '1': """
    x-------x

""",
    '2': """
    x-------x
    |
    |
    |
    |
    |
""",
    '3': """
    x-------x
    |       |
    |       0
    |
    |
    |
""",
    '4': """
    x-------x
    |       |
    |       0
    |       |
    |
    |

""",
    '5': """
    x-------x
    |       |
    |       0
    |      /|\
    |
    |
""",
    '6': """
    x-------x
    |       |
    |       0
    |      /|\
    |      /
    |

""",
    '7': """
    x-------x
    |       |
    |       0
    |      /|\
    |      / \
    |
"""
}


def check_valid_input(user_guess, old_letters_guessed):
    """checks validation for user guess.
     :param base: user_guess
     :param exponent: old_letters_guessed
     :type base: str
     :type exponent: list
     :return: user guess validation
     :rtype: boolean
     """
    if len(user_guess) > 1 and user_guess.isalpha():
        return False
    elif len(user_guess) > 1:
        return False
    elif not user_guess.isalpha():
        return False
    else:
        return True


def try_update_letter_guessed(user_guess, old_letters_guessed):
    """checks if letter was already guessed.
     :param base: user_guess
     :param exponent: old_letters_guessed
     :type base: str
     :type exponent: list
     :return: if letter was guessed
     :rtype: boolean
     """
    if user_guess in old_letters_guessed:
        return False
    else:
        old_letters_guessed.append(user_guess)
        return True


def show_hidden_word(secret_word, old_letters_guessed):
    # we will declare == guessing_board = list('_ ' * len(secret_word)) before calling the function.
    """creates a guessing board with the guessed letters.
     :param base: secret_word
     :param exponent: old_letters_guessed
     :type base: str
     :type exponent: list
     :return: guessing board
     :rtype: list
     """
    guessing_board = list('-' * len(secret_word))
    for letter in secret_word:
        if letter in old_letters_guessed:
            index = secret_word.index(letter)
            guessing_board[index] = letter
    print("".join(guessing_board))


def check_win(secret_word, old_letters_guessed):
    """checks if the user guessed all the letters in the secret word.
     :param base: secret_word
     :param exponent: old_letters_guessed
     :type base: str
     :type exponent: list
     :return: user win
     :rtype: boolean
     """
    length = len(secret_word)
    check_len_for_win = 0
    for old_letter in old_letters_guessed:
        check_len_for_win += secret_word.count(old_letter)
    if length == check_len_for_win:
        print('WIN')
        return True
    else:
        return False


def print_hangman(num_of_tries):
    """print hangman as to num of tries"""
    print(HANGMAN_PHOTOS[str(num_of_tries)])


def choose_word(file_path, index):
    """takes a word for the game from a txt file of the user.
     :param base: file_path
     :param exponent: index
     :type base: path
     :type exponent: int
     :return: word
     :rtype: str
     """
    with open(file_path, 'r') as words_file:
        words_list = words_file.read().split(' ')
        unrepeat_words = []
        for word in words_list:
            if words_list.count(word) == 1:
                unrepeat_words.append(word)

    while index + 1 > len(words_list):
        words_list = words_list + words_list
    finel_index = index + 1
    return words_list[finel_index]


def main():
    # opening screen
    print(HANGMAN_ASCII_ART)

    # asks user for file path and index to get the word
    user_file_choise = input("Enter file path: ")
    user_index = int(input('Enter index: '))
    #generating the game word
    secret_word = choose_word(user_file_choise, user_index)

    old_letters_guessed = []
    num_of_tries = 1

    # presenting the guessing board, game and the hanged
    guessing_board = '_ ' * len(secret_word)
    print('we have our word! lets start playing. \n \n', guessing_board, '\n\n')
    print_hangman(num_of_tries)

    while not check_win(secret_word, old_letters_guessed):
        # check for loss
        if num_of_tries == 6:
            print('last 2 tries! \nTry your best')
        if num_of_tries > 7:
            print('LOSE\nsorry, you maxed your tries. \n \nthe word was:\t', secret_word)
            break

        user_guess = input('choose your letter: '.lower())

        if check_valid_input(user_guess, old_letters_guessed):
            # checks if the user already guessed the letter,
            if not try_update_letter_guessed(user_guess, old_letters_guessed):
                print('X \nyou already guesses that letter. \n\n')
                letters = 'Letters guessed --\n\n'

                # collect all of the letters that were guessed
                for letter in old_letters_guessed:
                    letters += letter + '\t-->\t'

                print(letters, '\n\n')
                continue

            else:
                if user_guess not in secret_word:
                    print('):\n')

                    # print the corrent sate of the hanged man and add this fail
                    print_hangman(num_of_tries)
                    num_of_tries += 1

                else:
                    print('Correct!')

                show_hidden_word(secret_word, old_letters_guessed)

        else:
            print('Letter is not valid. try again \n\n\n')


if __name__ == "__main__":
    main()