def response(hey_bob):
    text = hey_bob.strip()

    if text == "":
        return "Fine. Be that way!"

    is_yelling = text.isupper() and any(c.isalpha() for c in text) 
    is_question = text.endswith("?")
    
    if is_yelling and is_question:
        return "Calm down, I know what I'm doing!"
    elif is_yelling:
        return "Whoa, chill out!"
    elif is_question:
        return "Sure."
    return "Whatever."