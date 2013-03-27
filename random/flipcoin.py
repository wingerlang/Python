import random

times, heads = 250000, 0
print("Flipping a coin %d number of times..." % (times))

for i in range(times):
	head = random.randint(0,1)
	if head:
		heads += 1

percentHeads, percentTails = heads / times, (times-heads) / times
print("RESULT!")
print("HEADS: %d  TAILS: %d" % (heads, times-heads))
print("HEADS: %f  TAILS: %f" % (percentHeads, percentTails))