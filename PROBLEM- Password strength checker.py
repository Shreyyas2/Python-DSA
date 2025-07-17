#Password strength checker
def for_security(password):
    if len(password)<6:
        return "Length is Too Short"
    if not any(char.isdigit() for char in password):
        return "No Digits Entered"
    if not any(char.islower() for char in password):
        return "Password should contain atlest one lowercase character"
    if not any(char.isupper() for char in password):
        return "Password should contain atlest one uppercase character"
    if not any(char in '!@$#' for char in password):
        return "Password should contain atlest one special character"
    return "Entered Password is Strong"


print(for_security('Weak1pass'))
print(for_security('Str0ng@Pass'))
