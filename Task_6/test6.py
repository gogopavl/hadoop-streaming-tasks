counter = 0
total = 0


with open("title.ratings.tsv", "r") as file:
    for line in file:
        votes = float(line.split("\t")[2].strip())
        # print("{0:.2f}".format(round(float(votes),2)))
        total += votes
        counter += 1

result = total / counter
print("{0:.2f}".format(round(float(result),2)))
