from random import randint  # import randint


def getRandomCharacter(ch1, ch2):
    """Generate a random character between ch1 and ch2."""
    return chr(randint(ord(ch1), ord(ch2)))


def getRandomLowerCaseLetter():
    """Generate a random lowercase letter."""
    return getRandomCharacter('a', 'z')


def getRandomUpperCaseLetter():
    """Generate a random uppercase letter."""
    return getRandomCharacter('A', 'Z')


def getRandomDigitCharacter():
    """Generate a random digit character."""
    return getRandomCharacter('0', '9')


def getRandomASCIICharacter():
    """Generate a random character."""
    return getRandomCharacter(chr(0), chr(127))
