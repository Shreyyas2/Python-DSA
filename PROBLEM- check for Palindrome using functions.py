#to check if the given string is palindrome

def is_palindrome(text):
    text=text.lower().replace(' ','')
    return text==text[::-1]
print(is_palindrome('w OW'))
print(is_palindrome('nICe'))
