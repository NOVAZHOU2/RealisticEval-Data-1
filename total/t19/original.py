# Generated by chatGPT (regex might need some work)

def contains_phone_number(output_to_test):
    pattern = r"\+?\d{1,3}[-\s]?\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{2,4}|\(\d{3}\)\s?\d{3}[-\s]?\d{4}"
    return regex(output_to_test, pattern)