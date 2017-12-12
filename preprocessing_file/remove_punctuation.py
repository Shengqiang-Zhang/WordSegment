import re


def rm_punctuation(file, rmfile):
    punc = "。，、,"
    f1 = open(file, "r", encoding='utf-8')
    f2 = open(rmfile, "w", encoding='utf-8')
    for line in f1.readlines():
        line_rmpunc = re.sub("[%s]+" % punc, "", line)
        f2.write(line_rmpunc)
    f1.close()
    f2.close()


def main():
    rm_punctuation("../resource/segment_dict_fmm.txt", "../resource/segment_dict_fmm_nopunc.txt")
    rm_punctuation("../resource/segment_noslash.txt", "../resource/segment_noslash_nopunc.txt")
    rm_punctuation("../resource/segment_dict_rmm.txt", "../resource/segment_dict_rmm_nopunc.txt")


if __name__ == '__main__':
    main()
