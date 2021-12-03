import time

start = time.process_time()

data = open("./7.in").read().split("\n")

print("took: %f seconds" % (time.process_time() - start))
