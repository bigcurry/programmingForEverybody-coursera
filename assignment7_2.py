# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
numbers = []
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    numbers.append(line[line.find('0'):])

num_sum = 0
for number in numbers:
	num_sum += float(number)

print 'Average spam confidence: %s' % str(num_sum / len(numbers))