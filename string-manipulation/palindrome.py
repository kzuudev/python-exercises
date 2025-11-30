

def palindrome(string):

    for i in range(len(string)):
        for j in range(len(string)):
            if string[i] == string[j - 1]:
                print(f"The {string} is a palindrome")
                return True
            else:
                print(f"The {string} is not palindrome")
                return False

word = "noon"
print(palindrome(word))