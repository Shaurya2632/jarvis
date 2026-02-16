import re

def is_contains(text, *words):
    return all(word in text for word in words)

def is_contains_any(text, *words):
    return any(word in text for word in words)

def replacer(text, *pairs):
    for old, new in pairs:
        text = text.replace(old, new)
    return text

def safe_eval(expression):
    if not re.match(r"^[\d+\-*/().\s]+$", expression):
        raise ValueError("Invalid mathematical expression")
    return eval(expression)
