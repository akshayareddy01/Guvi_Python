def is_palindrome():
    s = input("Enter a string: ")
    l = len(s)
    flag = 0
    for i in range(l // 2):
        if s[i] != s[l - 1 - i]:
            flag = 1
            break

    if flag == 0:
        print("Is Palindrome")
    else:
        print("Is Not a Palindrome")

is_palindrome()
