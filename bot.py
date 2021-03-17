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
    d += random.choice(["fast", "hurry"]) + " "
    d += str(random.choice([1, 2, 0.5])) + " $ sound \""
    for i in range(random.randint(1, 4)):
        if random.randint(0, 3) == 0:
            d += random.choice(["~", "."]) + " "
        else:
            d += random.choice(samples).strip() + ":"
            d += str(random.randint(0, 100))
            if random.randint(0, 2) == 0:
                d += random.choice(["*", "!", "/", "@"])
                d += str(random.randint(2, 4))
            d += " "
    d = d.strip(". ")
    d += "\" # legato 1\n\n"
    return d


def writeTidal(text, filename):
    with open(filename, 'w') as f:
        f.write(text)


main()
