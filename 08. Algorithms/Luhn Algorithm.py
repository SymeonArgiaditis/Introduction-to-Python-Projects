def verify_card_number(number: str) -> str:
    raw_digits = number.replace(' ', '')
    raw_digits = raw_digits.replace('-', '')
    raw_digits = reversed(list(raw_digits))

    raw_digits = [int(x) for x in raw_digits if x.isdigit()]
    
    processed_digits = []
    for index, digit in enumerate(raw_digits):
        is_even_position = index % 2 != 0
        if is_even_position:
            doubled_value = digit*2
            if doubled_value > 9:
                processed_digits.append(doubled_value- 9)
            else:
                processed_digits.append(doubled_value)
        else:
            processed_digits.append(digit)

    total_sum = sum(processed_digits)
    if total_sum % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"

print(verify_card_number('453914889'))
