# def isPalindrome(st):
#     return st == st[::-1]

# def isPalindrome(st):
#     for i in range(int(len(st)/2)):
#         if st[i] == st[len(st)-i-1]:
#             return True
#         else:
#             return False

def isPalindrome(st):
    rev = ''.join(reversed(st))
    if rev == st:
        return True
    else:
        return False
def isSymmetrical(st):
    length = len(st)
    mid = length//2
    if length%2==0:
        return st[:mid] == st[mid:]
    else:
        return st[:mid] == st[mid+1:]
prompt = input("Enter the string to check: ")
if isPalindrome(prompt):
    print('The given string is palindrome.')
else:
    print("The given string is not palindrome.")
if isSymmetrical(prompt):
    print("The given string is symmetrical.")
else:
    print("The given string is not symmetrical.")

#amaama input for both true