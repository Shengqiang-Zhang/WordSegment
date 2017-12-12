
def cal_fscore(my_segfile, standard_segfile):
    # calculate f-score
    f_math = open(standard_segfile, "r", encoding='UTF-8')
    f_pkunlp = open(my_segfile, "r", encoding='UTF-8')

    totalseg = 0
    for line in f_math.readlines():
        totalseg += len(line.split())

    totalseg_pkunlpsegmentor = 0
    for line in f_pkunlp.readlines():
        totalseg_pkunlpsegmentor += len(line.split())

    total_correct_seg = 0
    total_error_seg = 0
    f_math.seek(0)
    f_pkunlp.seek(0)
    for line_math, line_pkunlp in zip(f_math.readlines(), f_pkunlp.readlines()):
        dict_math = {}
        dict_pkunlp = {}
        for words in line_math.strip().split():
            if words in dict_math:
                dict_math[words] += 1
            else:
                dict_math[words] = 1
        for words in line_pkunlp.strip().split():
            if words in dict_pkunlp:
                dict_pkunlp[words] += 1
            else:
                dict_pkunlp[words] = 1

        for words in dict_pkunlp:
            if words in dict_math:
                if dict_math[words] >= dict_pkunlp[words]:
                    total_correct_seg += dict_pkunlp[words]
                else:
                    total_correct_seg += dict_math[words]
                    total_error_seg += dict_pkunlp[words] - dict_math[words]
            else:
                total_error_seg += dict_pkunlp[words]

    # print(totalseg)
    # print(totalseg_pkunlpsegmentor)
    # print(total_correct_seg + total_error_seg)

    P_score = total_correct_seg / totalseg_pkunlpsegmentor
    R_score = total_correct_seg / totalseg
    F_score = 2 * total_correct_seg / (totalseg_pkunlpsegmentor + totalseg)
    print("Precious = ", P_score)
    print("Recall = ", R_score)
    print("F-Score = ", F_score)
    f_math.close()
    f_pkunlp.close()


def main():
    print("用词典正向最大匹配法，包含标点符号：")
    cal_fscore("resource/segment_dict_fmm.txt", "resource/segment_noslash.txt")
    print("用词典正向最大匹配法，去除标点符号后：")
    cal_fscore("resource/segment_dict_fmm_nopunc.txt", "resource/segment_noslash_nopunc.txt")
    print("用词典逆向最大匹配法，包含标点符号：")
    cal_fscore("resource/segment_dict_rmm.txt", "resource/segment_noslash.txt")
    print("用词典逆向最大匹配法，去除标点符号后：")
    cal_fscore("resource/segment_dict_rmm_nopunc.txt", "resource/segment_noslash_nopunc.txt")


if __name__ == '__main__':
    main()
