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
        result = []
        while len(line) > 0:
            max_len = max_length
            if (len(line) < max_len):
                max_len = len(line)

            try_word = line[(len(line) - max_len):]
            while try_word not in dictionary:
                if (len(try_word) == 1):
                    break
                try_word = try_word[1:]
            result.append(try_word)
            # 从待分词文本中取出已经分词的文本
            line = line[0:(len(line) - len(try_word))]
        while len(result) > 0:
            word = result.pop()
            f_result.write(word + " ")
    f_raw.close()
    f_result.close()


def main():
    segment("resource/origin.txt", "resource/dictfile_correct.txt", "resource/segment_dict_rmm.txt")


if __name__ == '__main__':
    main()
