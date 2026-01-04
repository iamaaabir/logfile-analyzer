fileName = input('Enter a file name: ')

try:
    fh = open(fileName, 'r')
except:
    print ('Not a valid file name. File name is practice.txt')
    quit()

topSenders = dict()

for line in fh:
    if not line.startswith('From '):
        continue

    words = line.split()
    email = words[1]
    topSenders[email] = topSenders.get(email, 0) + 1

for k, v in sorted(topSenders.items()):
    print ('Email: ', k)
    print ('Freq: ', v)

print('\n\t The most frequent email: ')

freqEmail = None
freqCount = None

for k, v in topSenders.items():
    if freqEmail is None or v > freqCount:
        freqEmail = k
        freqCount = v

print ('Email address: ', freqEmail, 'Freq: ', freqCount)





