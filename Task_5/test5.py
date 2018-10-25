counter = 0
with open("title.basics.tsv", "r") as file:
    for line in file:
        releaseYear = line.split("\t")[5].strip()
        print('Release = {}'.format(releaseYear))
