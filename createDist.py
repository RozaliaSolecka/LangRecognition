import argparse
import dictfunctions as df

NO_ALFACHARACTERS = [' ', '!', '\"', '#', '$', '%', '&', '\'', '(', ')', '*', '@', '[', '\\', ']', '^', '_', '`', '{',
                     '|', '}', '~', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '\n', '?', ',', '.', '/', '-',
                     '–',
                     '+', '=', ';', '<', '>', ':', '’', '”', '„', '']
MINIMAL_OCCURANCE = 20


def standardchar(c):
    if c not in NO_ALFACHARACTERS:
        return True
    else:
        return False


def appenddist(distribution, c):
    if c in distribution:
        distribution[c] += 1
    else:
        distribution[c] = 1


def createLangDistribution(line, distribution=None):
    if distribution is None:
        distribution = {}

    for c in line:
        if standardchar(c):
            appenddist(distribution, c.lower())
        else:
            pass

    distribution = df.removeBelowMinimal(distribution, MINIMAL_OCCURANCE)
    distribution = df.sortdict(distribution)
    avgdict = df.percetageDictCalc(distribution)
    
    return avgdict

def createDistroFormFile(startpath):

    distribution = {}

    with open(startpath, encoding='utf-8') as f:
        for line in f:
            createLangDistribution(line,distribution)

    distribution = df.removeBelowMinimal(distribution, MINIMAL_OCCURANCE)
    distribution = df.sortdict(distribution)
    avgdict = df.percetageDictCalc(distribution)

    return avgdict
    #Debug info
    #
    #for i in distribution:
    #    print("Keys: {0} Count:{1} Percentage {2:0.4f}%".format(i, distribution[i], avgdict[i]))
    #

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("fname", help="file path containing data lang",
                        type=str)
    args = parser.parse_args()
    createDistroFormFile(args.fname)
