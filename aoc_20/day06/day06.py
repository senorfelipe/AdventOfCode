import time

start = time.process_time()

yes_count_any = 0
data = open("./6.in").read().split('\n\n')

for group in data:
    group = group.replace("\n", "")
    yes_count_any += len({letter for letter in group})


print("awnser 1: %d" % yes_count_any)

# ----------------------------------------- #
yes_count_every = 0
for group in data:
    awnsers = {letter for letter in group.replace("\n", "")}
    for person in group.split("\n"):
        awnsers_person = {a for a in person}
        awnsers = awnsers.intersection(awnsers_person)
    yes_count_every += len(awnsers)

print("awnser 2: %d" % yes_count_every)

print("took: %f seconds" % (time.process_time() - start))
