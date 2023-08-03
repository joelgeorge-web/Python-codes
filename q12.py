#given a string find the longest palindromic sequence in it

def longest_palindrome(s):
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    if s[0] == s[-1]:
        return 2 + longest_palindrome(s[1:-1])
    else:
        return max(longest_palindrome(s[1:]), longest_palindrome(s[:-1]))
    
if __name__ == "__main__":
    s = input("Enter the string: ")
    print(longest_palindrome(s))
