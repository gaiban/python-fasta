import sys
def read_fasta(filename):
    sequence = ''
    f = open(filename)
    for line in f:
        line = line.strip()
        if not '>' in line:
            # Append to the last sequence
            sequence = sequence + line
    f.close()
    return sequence
if len(sys.argv) <2:
	print("Need to provide filename as argument")
	exit(1)

print(read_fasta(sys.argv[1]))

