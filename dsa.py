""" print ("Hi THERE".lower())
gap = "hi there"
zap= print(gap.upper())
 """
""" text = "X-DSPAM-Confidence:    0.8475"

pos = text.find('0')
print(pos)

result = text[22:]
print(result) """

""" fhand = open('TRY.txt', encoding="utf-8")
inp = fhand.read()
print(len(inp))

print(inp[:20]) """

""" fhand = open('TRY.txt', encoding="utf-8")
for line in fhand:
    if line.startswith(' '):
        print(line)
    else:
        print('unimportant lines') """

""" fhand = open('TRY.txt', encoding="utf-8")
for line in fhand:
    line = line.rstrip()
    if line.endswith(' '):
        print(line)
    else:
        print('nill') """


""" try:
    fhand = open(fname, encoding="utf-8" )
except:
    print('File cant found', fname)
    quit()
count = 0 
for line in fhand:
    if line.startswith(' '):
        count = count + 1 
print('There were', count, 'subject lines in', fname)
fname = input('Enter file name') """

fname = input("Enter file name: ")
fh = open(fname, encoding="utf-8")
for line in fh:
    print(line.upper())










