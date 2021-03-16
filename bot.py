import random


def main():
    samples = readSamples('sampleList.txt')
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
    d = "d" + str(i) + " $ "
    rand = random.randint(0, 2)
    if rand == 0:
        d += "fast "
    elif rand == 1:
        d += "slow "
    elif rand == 2:
        d += "hurry "
    d += str(random.randint(1, 2)) + " $ sound \""
    for i in range(random.randint(1, 4)):
        if random.randint(0, 3) == 0:
            rand = random.randint(0, 1)
            if rand == 0:
                d += "~ "
            elif rand == 1:
                d += ". "
        else:
            d += random.choice(samples).strip() + ":" + \
                str(random.randint(0, 100))
            if random.randint(0, 2) == 0:
                rand = random.randint(0, 3)
                if rand == 0:
                    d += "*"
                elif rand == 1:
                    d += "!"
                elif rand == 2:
                    d += "/"
                elif rand == 3:
                    d += "@"
                d += str(random.randint(2, 4))
            d += " "
    d = d.strip(". ")
    d += "\"\n\n"
    return d


def writeTidal(text, filename):
    with open(filename, 'w') as f:
        f.write(text)


main()
