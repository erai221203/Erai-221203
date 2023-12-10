def isPalindrome(s):
    return s == s[::-1]
s =input('Enter any word:')
ans = isPalindrome(s)

if ans:
    print(s,"is a Palindrome")
else:
    print(s,"is not a palindrome")
