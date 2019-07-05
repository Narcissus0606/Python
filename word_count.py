"""
案例：统计当前一个字符串“hello world!ni hao”
    统计每个单词出现频率
用到知识点：
String
{}
[]
"""
def main():
    print("Please input:")
    letter = input()
    print(count_word(letter))

def count_word(letter):
    list = letter.split(' ')
    dict_word = {}
    for word in list:
        if(word in dict_word):
            dict_word[word] = dict_word[word]+1
        else:
            dict_word[word] = 1
    return dict_word
          
main()
