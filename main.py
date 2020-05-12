import csv

f = open("test.txt", "r")
line = f.readline()

csvf = open('output.csv', 'w')

while line:
    linedata = line.strip()
    after = linedata.replace('; ', ',')
    after = after.replace(';', '') + "\n"

    cnt = 0

    for i in after:
        if i == ",":
            cnt = cnt + 1
    
    if cnt == 0:
        after = "#" + after
    csvf.write(after)
    print(after)
    line = f.readline()

f.close()
