import os, csv, re
#File ops for CSV
dir_path = os.path.dirname(os.path.realpath(__file__))
filePath = os.path.join(dir_path, "contacts.csv")
filePathOut = os.path.join(dir_path, "unifiContacts.csv")

#sanitizes and converts phone numbers
def removeCharacters(inputNumber):
    outputNumber = re.sub(r"[^0-9]+", "", inputNumber) #removes all non-numbers and whitespace
    if outputNumber == "":
        return ""
    if outputNumber[0] == '1':
        outputNumber = outputNumber[1:]
    elif outputNumber[0:2] == "+1":
        outputNumber = outputNumber[2:]
    return outputNumber


#Converts CSV to 2D list
with open(filePath, newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

#creates final list
contactList = []

for i in range(len(data)):
    firstName = data[i][0]
    lastName = data[i][2]

    #skips entries without names
    if firstName == "" and lastName == "":
        print("A contact is missing a name and therefore had to be skipped.")
        continue
    #skips template user
    if firstName == "First Name":
        continue
    #pulls cell phone number first. If there isn't a cell phone number itterate through home and office phones until a number is found. 
    if data[i][20] != "":
        phoneNum = removeCharacters(data[i][20])
    else:
        for j in range(17, 19):
            if data[i][j] != "":
                phoneNum = removeCharacters(data[i][j])
                break

    #makes sure there is a phone number. If not it will be skipped
    if phoneNum == "":
        print('A contact "' + firstName + ' ' + lastName + " " + '" is missing a phone number and therefore had to be skipped.')
        continue
    
    #Adds current item to list
    contactList.append([firstName, lastName, phoneNum])

#outputs file
with open(filePathOut, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(contactList)

print("Done.")