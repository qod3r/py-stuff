def palindrome(s):
    s = s.lower().replace(" ", "")
    return ("Палиндром" if s == s[::-1] else "Не палиндром")


print(palindrome(input()))
