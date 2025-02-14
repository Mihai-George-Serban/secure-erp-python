import random
import string


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):
    list_id = []
    for i in range(number_of_small_letters):
        list_id.append(random.choice(string.ascii_lowercase))
    for i in range(number_of_capital_letters):
        list_id.append(random.choice(string.ascii_uppercase))
    for i in range(number_of_digits):
        list_id.append(random.choice(string.digits))
    for i in range(number_of_special_chars):
        list_id.append(random.choice(allowed_special_chars))
    random.shuffle(list_id)
    return "".join(list_id)
