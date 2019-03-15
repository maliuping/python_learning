#!/usr/bin/python


results = []

inputfile = open('mlp.txt')
lines = inputfile.readlines()
print(lines)
inputfile.close()

for line in lines:
	print(line)
	data = line.split()
	sum = 0
	for score in data[1:]:
		sum += int(score)

	result = "%s\t:%d\n"%(data[0],sum)
	print(result)
	results.append(result)

print(results)

outfile = open("datum.txt","w")
outfile.writelines(results)
outfile.close()

