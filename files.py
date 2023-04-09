#open a file

myFile = open('myfile.txt', 'w')

#get some info
print('Name', myFile.name)
print('Is closed', myFile.closed)
print('Opening mode', myFile.mode)

#write to file

myFile.write('I am done with university')
myFile.write(' Like so done')
myFile.close()

#append 
myFile = open('myfile.txt', 'a')
myFile.write(' Ok not so')
myFile.close()

#Read from file
myFile = open('myfile.txt','r+')
text = myFile.read(20)
print(text)

