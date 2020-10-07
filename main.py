#joshua fitzgerald 1374331

if __name__ == '__main__':
    user_word = input()
    normal = ""
    reverse = ""
    for char in user_word.lower():
        if char != ' ':
            normal += char
            reverse = char + reverse
    if normal == reverse:
        print(user_word + " is a palindrome")
    else:
        print(user_word + " is not a palindrome")