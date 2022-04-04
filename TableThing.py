# By Marvin Omoruyi
# Last edited 28/03/2022

headers = [
      "Name",
      "Age",
      "Score"
      ]

dataList = [
      ["Dan", 22, 85],
      ["William", 26, 93],
      ["Jane", 24, 91],
      ["Stephanie", 22, 86]
      ]

spaceCount = 0
totalLength = 0
barrier = "|"
spaceInsufficient = False

print("This is the data of the list:")
print(dataList)
print()


for index, item in enumerate(headers):
      totalLength += len(barrier) + len(item) + (2*spaceCount)
      print(" "*spaceCount + item + " "*spaceCount, end=barrier)

print()
print("-"*totalLength)

#looping through the 1st dimension of the list

for index, item in enumerate(dataList):

      #looping through the 2nd dimension of the list
      for index2, item2 in enumerate(item):
            item2 = str(item2)
            tableLength = len(headers[index2]) + (2*spaceCount)
            spacesLeft = tableLength - len(item2)

            if spacesLeft < 0:
                  spacesLeft = abs(spacesLeft)
                  item2 = item2[:-spacesLeft]
                  spaceInsufficient = True
                  spacesLeft = 0
                  
            print(item2+" "*spacesLeft, end=barrier)
      print()

if spaceInsufficient:
      print("The space for all components in this table is insufficient. Please make the spaceCount constant larger.")
