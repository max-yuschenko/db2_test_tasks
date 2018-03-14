def handle_numbers(number1, number2, number3):
    return len([i for i in range(number1, number2 + 1) if i % number3 == 0])
