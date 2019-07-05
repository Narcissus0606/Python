def main():
    print("Please input word:")
    word = input()
    try:
        with open("C:\\Users\\Narcissus\\Desktop\\word.txt","a") as f:
            f.write(" "+word)
    except Exception as e:
        print(e)

main()
