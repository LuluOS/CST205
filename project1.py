"""Project1"""
pic = []
pic.append(makePicture("C:\\Users\\Luana\\Dropbox\\CSUMB\\CST205-Multimedia\\Project1\\Project1Images\\1.png"))
pic.append(makePicture("C:\\Users\\Luana\\Dropbox\\CSUMB\\CST205-Multimedia\\Project1\\Project1Images\\2.png"))
pic.append(makePicture("C:\\Users\\Luana\\Dropbox\\CSUMB\\CST205-Multimedia\\Project1\\Project1Images\\3.png"))
pic.append(makePicture("C:\\Users\\Luana\\Dropbox\\CSUMB\\CST205-Multimedia\\Project1\\Project1Images\\4.png"))
pic.append(makePicture("C:\\Users\\Luana\\Dropbox\\CSUMB\\CST205-Multimedia\\Project1\\Project1Images\\5.png"))
pic.append(makePicture("C:\\Users\\Luana\\Dropbox\\CSUMB\\CST205-Multimedia\\Project1\\Project1Images\\6.png"))
pic.append(makePicture("C:\\Users\\Luana\\Dropbox\\CSUMB\\CST205-Multimedia\\Project1\\Project1Images\\7.png"))
pic.append(makePicture("C:\\Users\\Luana\\Dropbox\\CSUMB\\CST205-Multimedia\\Project1\\Project1Images\\8.png"))
pic.append(makePicture("C:\\Users\\Luana\\Dropbox\\CSUMB\\CST205-Multimedia\\Project1\\Project1Images\\9.png"))
#newpic = 

#showing all the 9 pictures
#for i in range (0, len(pic)):
# show(pic[i])

ySize = getHeight(pic[0]) #get the size of x-axes
xSize = getWidth(pic[0]) #get the size of the y-axes
#print ("xSize = %d" %xSize)
#print ("ySize = %d" %ySize)

px = [9]
#for y in range (0, ySize):  
#  for x in range (0, xSize):
x = 0
y = 0
red = []
for picture in range (0, len(pic)):
  print ("(%d,%d) picture = %d" %(x,y,picture))
  #px contem o pixel da posicao x,y
  #px.append(getPixel(pic[picture], x, y))
  px = getPixel(pic[picture], x, y)
  redDegree = getRed(px)
  red.insert(picture, redDegree)
  print ("red[%d] = %d" %(picture,red[picture]))