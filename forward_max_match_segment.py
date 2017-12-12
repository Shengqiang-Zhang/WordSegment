# -*- coding:utf-8 -*-

"""
基于词典的最大正向匹配分词算法
"""


def add_dict(dictfile):
    f_dict = open(dictfile, 'r', encoding="utf-8")
    print("开始初始化词典")
    max_length = 1
    count = 0
    dictionary = []
    for line in f_dict.readlines():
        dictionary.append(line.strip())
        count += 1
        if len(line) > max_length:
            max_length = len(line)
    print("完成词典初始化，添加词典条目数：" + str(count))
    print("最大分词长度：" + str(max_length))
    return dictionary, max_length


def segment(rawfile, dictfile, resultfile):
    dictionary, max_length = add_dict(dictfile)
    f_raw = open(rawfile, "r", encoding="utf-8")
    f_result = open(resultfile, "w", encoding="utf-8")

    for line in f_raw.readlines():
        while len(line) > 0:
            max_len = max_length
            if len(line) < max_len:
                max_len = len(line)

            # 取指定的最大长度的文本去词典里面匹配
            try_word = line[0:max_len]
            while try_word not in dictionary:
                if len(try_word) == 1:
                    break
                try_word = try_word[0:(len(try_word) - 1)]
            f_result.write(try_word + " ")
            line = line[len(try_word):]
            # f_result.write("\n")
    f_raw.close()
    f_result.close()


def main():
    segment("resource/origin.txt", "resource/dictfile_correct.txt", "resource/segment_dict_fmm.txt")


if __name__ == '__main__':
    main()
