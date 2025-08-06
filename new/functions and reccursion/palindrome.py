def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])
word = input("Enter a word: ")
if is_palindrome(word):
    print("It is a palindrome")
else:
    print("Not a palindrome")
