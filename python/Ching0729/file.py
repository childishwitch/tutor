import glob
import os

def listDir():
	print('listDir function: list all the files in the current directory')

	print('list files use glob: it is a list type')
	fileList = glob.glob('*.csv')
	print(fileList)

def readFile(fileStr):
	print('readFile function')

	print('read all the content')
	inFile = open(fileStr,'r')
	print(inFile.read())
	inFile.close()

	print('use \'readlines\' to read list of lines')
	inFile = open(fileStr,'r')
	for line in inFile.readlines():
		print(line)
	inFile.close()

	print('use \'split\' to split lines')
	inFile = open(fileStr,'r')
	for line in inFile.read().split('\n'):
		print(line)
	inFile.close()

	print('with open for large data')
	with open(fileStr) as inFile:
		for line in inFile:
			print(line)
def writeFile(fileStr,writeStr):
	print('writeFile function')
	writeFile = open(fileStr,'w')
	print('write '+writeStr+' to '+fileStr)
	writeFile.write(writeStr)
	writeFile.close()

def subString(myStr):
	print('subString function')
	print('use row')
	#substring
	year = myStr[7:11]
	if year == '2016' or year == '2017':
		print('test num: '+myStr[4:7])
	
	print('use split')
	#split
	splitStr = (myStr.split('_'))[0]
	print('splitStr: '+splitStr)
	
	print('use replace')
	#remove
	rStr = splitStr.replace('SQRC','')
	rStr = rStr.replace('2017','')
	print('replacedStr: '+rStr)
if __name__ == '__main__':
	print('listDir')
	listDir()

	print('readFile')
	readFile('csvIn.csv')

	print('writeFile')
	writeFile('csvOut.csv','write this line')

	print('subString')
	myStr = 'SQRC1532017_Feb_20_1739.csv'
	subString(myStr)
