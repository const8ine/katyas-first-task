import os.path

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

dataFilePath = os.path.join(THIS_FOLDER,'data.txt')
dataFile = open(dataFilePath ,'r')
resultFile = os.path.join(THIS_FOLDER,'result.txt');
i = 1

strPosition = raw_input('Enter the character number to begin with: ')
strPosition = int(strPosition)
trimmedString = dataFile.read().strip()


for startCharacter in trimmedString:
	i += 1
	if i >= strPosition:
		exportFile = open(resultFile ,'w')
		exportFile.write(trimmedString[strPosition:]);

print('The result is saved in /result.txt')