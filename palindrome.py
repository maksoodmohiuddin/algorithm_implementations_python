# Sentence is palindrome or not. Must be case insensitive, and ignore special characters.
def isPalindrome(input):
    start = 0
    end = len(input) - 1

    while start < end:
        start_str = input[start]
        end_str = input[end]

        if start_str.isalpha() and end_str.isalpha():
            if not start_str.__eq__(end_str):
                return False
        end -= 1
        start += 1

    return True

print isPalindrome("r#edivide%r")
print isPalindrome("r#edivide#r")
print isPalindrome("n@oo#n")
print isPalindrome("n#oo#n")
print isPalindrome("radar")
print isPalindrome("civic")
print isPalindrome("level")
print isPalindrome("rotor")
print isPalindrome("kayak")
print isPalindrome("reviver")
print isPalindrome("racecar")
print isPalindrome("redder")
print isPalindrome("madam")
print isPalindrome("refer")
