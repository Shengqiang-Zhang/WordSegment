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


def handle_dictfile(rawfile, resultfile):
    f_raw = open(rawfile, "r", encoding="utf-8")
    f_result = open(resultfile, "w", encoding="utf-8")

    dictionary = []
    for line in f_raw.readlines():
        line = line.replace("\\", " ")
        line = line.replace("  ", " ")
        line = line.strip().split(" ")
        for i in line:
            dictionary.append(i)

    for word in dictionary:
        f_result.write(word + "\n")

def main():
    rm_punctuation("../resource/notExamination.txt", "../resource/rawdictfile_nopunc.txt")
    handle_dictfile("../resource/rawdictfile_nopunc.txt", "../resource/dictfile.txt")
    handle_dictfile("../resource/segment_noslash_nopunc.txt", "../resource/dictfile_correct.txt")

if __name__ == '__main__':
    main()