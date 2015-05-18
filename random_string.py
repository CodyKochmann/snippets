def random_string(length=32,upper=True,lower=True,digits=True):
    # Generates a random string with selectable characters
    # By: Cody Kochmann
    from random import choice
    letters = "qwertyuiopasdfghjklzxcvbnm"
    chars = ""
    if upper:
        chars+=letters.upper()
    if lower:
        chars+=letters
    if digits:
        chars+="1234567890"
    return(''.join(choice(chars) for _ in range(length)))
