dict_word = {}

def read_file(path):
    try:
        with open(path,"r") as f:
            data = f.readlines()
    except Exception as e:
        print(e)
    return data

def count_word(data):
    for line in data:
        list = line.split(" ")
        for word in list:
            if(word in dict_word):
                dict_word[word] = dict_word[word]+1
            else:
                dict_word[word] = 1

def write_file(path):
    try:
        with open(path,"a") as f:
            for key in dict_word:
                f.write(key+"->"+str(dict_word[key])+"\r\n")
    except Exception as e:
        print(e)

def main(letter_path,word_path):
    count_word(read_file(letter_path))
    write_file(word_path)

main("C:\\Users\\Narcissus\\Desktop\\word.txt","C:\\Users\\Narcissus\\Desktop\\0705.txt")









