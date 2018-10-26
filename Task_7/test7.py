counter = 0
with open("title.crew.tsv", "r") as file:
    for line in file:
        # print(len(line.split("\t")))
        stringOfWriters = line.split("\t")[2].strip()
        if "\N" in stringOfWriters:
            continue
        listOfWriters = stringOfWriters.split(",")
        numOfWriters = len(listOfWriters)
        print('Num of writers = {}'.format(numOfWriters))
