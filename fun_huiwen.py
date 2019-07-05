def boolean_num(n):
    temp_str = str(n)[::-1]
    if(int(temp_str) == n):
        print("This is a huiwen number!")
    else:
        print("This is not a huiwen number!")

boolean_num(121)
