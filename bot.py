import random


def main():
    samples = readSamples('list.txt')
    code = ""
    for i in range(1, random.randint(3, 5)):
        code += writeD(i, samples)
    code += "hush"
    writeTidal(code, 'my.tidal')
    print(code)


def readSamples(filename):
    with open(filename) as f:
        lines = f.readlines()
    return lines


def writeD(i, samples):
    d = "d" + str(i) + " $ sound \""
    for i in range(random.randint(1, 4)):
        d += random.choice(samples).strip() + " "
    d = d.strip()
    d += "\"\n\n"
    return d


def writeTidal(text, filename):
    with open(filename, 'w') as f:
        f.write(text)


main()
