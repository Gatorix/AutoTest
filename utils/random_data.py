import random
import string


def random_string_generator(str_size=12, start_with='autotest_'):
    return f'{start_with}{"".join(random.choice(string.ascii_letters) for _ in range(str_size))}'


def random_choice_in_list(choice_list):
    return random.choice(choice_list)


def random_id_generator(str_size=11, start_with=''):
    return f'{start_with}{random.choice(string.digits.replace("0", "1"))}' \
           f'{"".join(random.choice(string.digits) for _ in range(str_size))}'

def shorten_response_text(text: str):
    return f'{text[:50]}...{text[-50:]}' if len(text) > 100 else text
