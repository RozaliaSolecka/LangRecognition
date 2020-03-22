LANGS = ["bul", "ces", "dan", "deu", "ell", "eng", "est", "fin", "fra", "gle", "hrv", "hun",
         "ita", "lav", "lit", "mlt", "nld", "pol", "por", "ron", "slk", "slv", "spa", "swe"]


def maketraindata():
    print("Start")
    startpath = 'wili-2018\\'
    filesfict = {}
    langlines = []
    langnames = []
    with open(startpath + "x_train.txt", 'rb') as f:
        for line in f:
            langlines.append(line)
    with open(startpath + "y_train.txt") as f:
        langnamesraw = f.readlines()

    for line in langnamesraw:
        langnames.append(line.rstrip('\n'))

    for x in range(len(langlines)):
        if langnames[x] in LANGS:
            if langnames[x] in filesfict:
                filesfict[langnames[x]].write(langlines[x])
            else:
                newfile = open('traindata\\' + langnames[x] + ".txt", "wb")
                filesfict[langnames[x]] = newfile
                filesfict[langnames[x]].write(langlines[x])

    for key in filesfict:
        filesfict[key].close()
    print("Processing Complete!")


def maketestdata():
    print("Start")
    startpath = 'wili-2018\\'
    print("Start")
    langlines = []
    langnames = []
    with open(startpath + "x_test.txt", 'rb') as f:
        for line in f:
            langlines.append(line)
    with open(startpath + "y_test.txt") as f:
        langnamesraw = f.readlines()

    for line in langnamesraw:
        langnames.append(line.rstrip('\n'))

    newtestx = open("testdata\\" + "NewTrainX.txt", "wb")
    newtesty = open("testdata\\" + "NewTrainY.txt", "w")

    for x in range(len(langlines)):
        if langnames[x] in LANGS:
            newtestx.write(langlines[x])
            newtesty.write(langnamesraw[x])
    newtestx.close()
    newtesty.close()
    print("Processing Complete!")


def main():
    maketraindata()
    maketestdata()


if __name__ == "__main__":
    main()
