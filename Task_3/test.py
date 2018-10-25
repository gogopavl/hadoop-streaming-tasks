counter = 0
with open("name.basics.tsv", "r") as file:
    for line in file:
        # print(len(line.split("\t")))
        prof = line.split("\t")[4]
        if "actor" in prof or "actress" in prof:
            counter += 1
            # print(line)
print(counter)
