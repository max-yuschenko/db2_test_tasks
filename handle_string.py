def handle_string(value):
    digits = sum(ch.isdigit() for ch in value)
    letters = sum(ch.isalpha() for ch in value)
