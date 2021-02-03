import string

unvalid_char = 'a'


class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, username):
        self._username = username

    def __str__(self):
        global unvalid_char
        for c in self._username:
            if c in string.punctuation:
                unvalid_char = c

        return "the user name {} is not valid. contains the illegal character: {}".format(self._username, unvalid_char)


class UsernameTooShort(Exception):
    def __init__(self, username):
        self._username = username

    def __str__(self):
        return "the user name {} is too short.".format(self._username)


class UsernameTooLong(Exception):
    def __init__(self, username):
        self._username = username

    def __str__(self):
        return "the user name {} is too long.".format(self._username)


class PasswordMissingCharacter(Exception):
    def __init__(self, password):
        self._password = password

    def __str__(self):
        return "the password is missing characters."


class PasswordTooShort(Exception):
    def __init__(self, password):
        self._password = password

    def __str__(self):
        return "the password is too short."


class PasswordTooLong(Exception):
    def __init__(self, password):
        self._password = password

    def __str__(self):
        return "the password is too long."


is_upper = False
is_lower = False
is_number = False
is_special_char = 0


def is_all_chars_in_pass(password):
    global is_upper
    global is_lower
    global is_number
    global is_special_char
    for c in password:
        if c.isalpha():
            is_upper = True
        if c.islower():
            is_lower = True
        if c.isnumeric():
            is_number = True
        if c in string.punctuation:
            is_special_char = is_special_char + 1

    if is_upper and is_lower and is_number:
        if is_special_char == 1:
            return True
    else:
        return False


def check_input(username, password):
    for char in username:
        if not char.isalnum():
            if char is '_':
                continue
            else:
                raise UsernameContainsIllegalCharacter(username)

    if len(username) < 3:
        raise UsernameTooShort(username)

    if len(username) > 16:
        raise UsernameTooLong(username)

    if len(password) < 8:
        raise PasswordTooShort(password)

    if len(password) > 40:
        raise PasswordTooLong(password)

    if not is_all_chars_in_pass(password):
        raise PasswordMissingCharacter(password)

    print('OK')


def main():
    print('hello. plz type your username and password')
    username = input('username: ')
    password = input('password: ')
    check_input(username, password)


main()
#check_input("A_a1.", "12345678")

