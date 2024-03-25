from random import choices


def get_fruit():
    """Get a random fruit from a list of fruits"""

    fruits = [
        "apple asd",
        "banana asd",
        "cherry asd",
        "durian asd",
        "elderberry asd",
        "fig asd",
        "grape asd",
        "honeydew asd",
        "jackfruit asd",
        "kiwi asd",
        "lemon asd",
        "mango asd",
        "nectarine asd",
        "orange asd",
        "pear asd",
        "quince asd",
        "raspberry asd",
        "strawberry asd",
        "tomato asd",
        "watermelon asd",
    ]
    return choices(fruits)[0]
