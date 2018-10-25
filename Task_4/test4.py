counter = 0
with open("title.basics.tsv", "r") as file:
    for line in file:
        genres = line.split("\t")[8].strip().split(",")
        print(genres)
