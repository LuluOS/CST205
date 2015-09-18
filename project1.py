##Student: Luana Sawada
##      Student ID: 2585504
##      Otter ID: okin8904
##      https://github.com/LuluOS/CST205.git    
##Copyright (c) 2015, Luana Okino Sawada <lokinosawada@csumb.edu> or <losbcc@gmail.com>

import sys
  
#""" Quicksort """
#""" http://hetland.org/coding/python/quicksort.html """
def partition(list, start, end):
  pivot = list[end] # Partition around the last value
  bottom = start-1  # Start outside the area to be partitioned
  top = end

  done = 0
  while not done: # Until all elements are partitioned...
    while not done: # Until we find an out of place element...
      bottom = bottom+1 # ... move the bottom up.

      if bottom == top: # If we hit the top...
        done = 1  # ... we are done.
        break

      if list[bottom] > pivot:  # Is the bottom out of place?
        list[top] = list[bottom]  # Then put it at the top...
        break                      # ... and start searching from the top.

    while not done: # Until we find an out of place element...
      top = top-1   # ... move the top down.

      if top == bottom: # If we hit the bottom...
        done = 1    # ... we are done.
        break

      if list[top] < pivot: # Is the top out of place?
        list[bottom] = list[top]  # Then put it at the bottom...
        break # ...and start searching from the bottom.

  list[top] = pivot # Put the pivot in its place.
  return top  # Return the split point

def quicksort(list, start, end):
  if (start < end):                            # If there are two or more elements...
    split = partition(list, start, end)    # ... partition the sublist...
    quicksort(list, start, split-1)        # ... and sort both halves.
    quicksort(list, split+1, end)
  else:
    return

#""" Picking picture """
def pickFolder(vector):
  folder = pickAFolder()
  if folder is not None:

    for imageNumber in range(0,8):
      imagePath = folder + str(imageNumber + 1) + ".png"
      vector.append(makePicture(imagePath))

    return folder
  else:
    print ("!!! ERROR: invalid input for pickFolder() !!!")

#""" create the new picture """
def createNewPicture(xSize, ySize, nameOfImage, folder):
  #""" creating a new picture with the size of xSize X ySize """
  newPicture = makeEmptyPicture(xSize, ySize)
  #""" defining a path for the new picture """
  newPath = folder + str(nameOfImage) + ".png"

  pictureDetails = []
  pictureDetails.append(newPicture) #""" pictureDetails[0] = newPicture """
  pictureDetails.append(newPath) #""" pictureDetails[1] = newPath """   

  #""" saving the new picture in newPath """
  writePictureTo(newPicture, newPath)

  return pictureDetails
  
#"""save the new picture """
def saveNewPicture(newPicture, newPath):
  #""" saving the new picture in newPath """
  writePictureTo(newPicture, newPath)

  show(newPicture)
  return

#""" Analyze the pixels """
def analyzePixel(px, pic, x, y, red, blue, green):
  #""" navegating in the same pixel to compare each pixel from the 9 images """
  for picture in range (0, len(pic)):
    #""" px has the pixel from the position x,y """
    px.append(getPixel(pic[picture], x, y))

    #""" get the degree of red from the pixel """
    redDegree = getRed(px[picture])
    #""" store the redDegree in the red array """
    red.insert(picture, redDegree)
    
    #""" get the degree of blue from the pixel """
    blueDegree = getBlue(px[picture])
    #""" store the blueDegree in the blue array """
    blue.insert(picture, blueDegree)
    
    #""" get the degree of green from the pixel """
    greenDegree = getGreen(px[picture])
    #""" store the greenDegree in the red array """
    green.insert(picture, greenDegree)
  return

#""" Median """
#""" http://stackoverflow.com/questions/24101524/finding-median-of-list-in-python """
def median(lst,pxSize):
  quicksort(lst,0,pxSize)
  if (len(lst) < 1):
    return None
  if (len(lst) % 2 == 1):
    return lst[((len(lst)+1)/2)-1]
  else:  #""" array[start : end] => star -> (end-1) """
    return float(sum(lst[(len(lst)/2)-1:(len(lst)/2)+1]))/2.0 #""" (lst[4]+lst[5])/2 => average from the ones in the midle of the array"""

#""" return the array with the different numbers (non-repeatble) """
def diffNumbers(lst):
  array = []
  pivot = lst[0]
  array.append(pivot)
  for i in range(1,len(lst)):
    if (pivot != lst[i]):
      array.append(lst[i])
      pivot = lst[i]
  return array

#""" return how many times the number repeat in the lst array """
def diffQuantity(number, lst):
  count = 0
  for i in range(len(lst)):
    if (number == lst[i]):
      count = count + 1
  return count

#""" return the often number (MODE) """        
def mode(lst, pxSize):
  quicksort(lst,0,pxSize)
  numbers = diffNumbers(lst)

  often = 0
  bigger = 0
  goOn = 0
  quantity = []
  for i in range (len(numbers)):
    qnt = diffQuantity(numbers[i], lst)
    quantity.append(qnt)
    if (bigger < quantity[i]):
      bigger = quantity[i]
      often = numbers[i]
      goOn = 1
    else:
      if (bigger > quantity[i]):
        goOn = 2
      else:
        goOn = 0

  if (goOn == 0):
    return median(lst,pxSize)
  else:
    return often

#""" return the range of the lst """ 
def rangeArray(lst, pxSize):
  quicksort(lst,0,pxSize)

  rangeOf = lst[len(lst)-1] - lst[0]

  return rangeOf

def mean(lst):
  total = 0
  for i in range(len(lst)):
    total = total + lst[i]
  mean = total / len(lst)
  return mean

#""" check the color value and approximate it to black or white """
def approximateBnW(color):
  if (color >= 0) & (color <= 127): #""" if the color is near to black than white """
    color = 0 #""" color turn black """
  else:
      if (color > 128) & (color <= 255): #""" if the color is near to white than black """
        color = 255 #""" color turn white """
  return color

#""" return the array with all the same value """ 
def bnw(Red,Green,Blue):
  average = (Red + Green + Blue) / 3
  color = approximateBnW(average)

  vector = []
  Red = color
  Green = color
  Blue = color
  vector.append(Red) #""" vector[0] = Red """
  vector.append(Green) #""" vector[1] = Green """
  vector.append(Blue) #""" vector[2] = Blue """
  return vector

#""" return the RedNGrey colors """ 
def RedNGrey(Red,Green,Blue):
  vector = []
  average = (Green + Blue) / 2
  if (Red < average):
    Red = average
  Green = average
  Blue = average

  vector.append(Red) #""" vector[0] = Red """
  vector.append(Green) #""" vector[1] = Green """
  vector.append(Blue) #""" vector[2] = Blue """
  return vector

#""" return the GreenNGrey colors """ 
def GreenNGrey(Red,Green,Blue):
  vector = []
  average = (Blue + Red) / 2
  if (Green < average):
    Green = average
  Red = average
  Blue = average

  vector.append(Red) #""" vector[0] = Red """
  vector.append(Green) #""" vector[1] = Green """
  vector.append(Blue) #""" vector[2] = Blue """
  return vector

#""" return the BlueNGrey colors """ 
def BlueNGrey(Red,Green,Blue):
  vector = []
  average = (Green + Red) / 2
  if (Blue < average):
    Blue = average
  Red = average
  Green = average

  vector.append(Red) #""" vector[0] = Red """
  vector.append(Green) #""" vector[1] = Green """
  vector.append(Blue) #""" vector[2] = Blue """
  return vector

#""" return the GreyShades """
def grey(Red,Green,Blue):
  average = (Red + Green + Blue) / 3
  
  vector = []
  Red = average
  Green = average
  Blue = average

  vector.append(Red) #""" vector[0] = Red """
  vector.append(Green) #""" vector[1] = Green """
  vector.append(Blue) #""" vector[2] = Blue """
  return vector

#""" Filtering with the median """
def medianFilter(pic, ySize, xSize, folder):
  pictureDetails = createNewPicture(xSize, ySize, "MedianFilter", folder)

  #"""Navigating in y-axes """
  for y in range (0, ySize):
    #"""Navigating in x-axes """
    for x in range (0, xSize):
      #""" declare a new vectors """
      red = []
      blue = []
      green = []
      px = []

      analyzePixel(px, pic, x, y, red, blue, green)
        
      npx = getPixel(pictureDetails[0], x, y)
      pxSize = len(px)-1
      
      mRed = median(red,pxSize)
      mGreen = median(green,pxSize)
      mBlue = median(blue,pxSize)

      #""" put all RGB color together """
      color = makeColor(mRed, mGreen, mBlue)
      #""" set pixel npx with the color """
      setColor(npx, color)

      #""" deleting the px array """
      del px

    repaint(pictureDetails[0])

  saveNewPicture(pictureDetails[0], pictureDetails[1])
  
  return

#""" Filtering with the mode with the number which appears most """
def modeFilter(pic, ySize, xSize, folder):
  pictureDetails = createNewPicture(xSize, ySize, "ModeFilter", folder)

  #"""Navigating in y-axes """
  for y in range (0, ySize):
    #"""Navigating in x-axes """
    for x in range (0, xSize):
      #""" declare a new vectors """
      red = []
      blue = []
      green = []
      px = []

      analyzePixel(px, pic, x, y, red, blue, green)
      
      npx = getPixel(pictureDetails[0], x, y)
      pxSize = len(px)-1
      
      mRed = mode(red, pxSize)
      mGreen = mode(green, pxSize)
      mBlue = mode(blue, pxSize)

      #""" put all RGB color together """
      color = makeColor(mRed, mGreen, mBlue)
      #""" set pixel npx with the color """
      setColor(npx, color)

      #""" deleting the px array """
      del px

    repaint(pictureDetails[0])

  saveNewPicture(pictureDetails[0], pictureDetails[1])
  
  return

#""" Filtering with the range """
def rangeFilter(pic, ySize, xSize, folder):
  pictureDetails = createNewPicture(xSize, ySize, "RangeFilter", folder)

  #"""Navigating in y-axes """
  for y in range (0, ySize):
    #"""Navigating in x-axes """
    for x in range (0, xSize):
      #""" declare a new vectors """
      red = []
      blue = []
      green = []
      px = []

      analyzePixel(px, pic, x, y, red, blue, green)
      
      npx = getPixel(pictureDetails[0], x, y)
      pxSize = len(px)-1
      
      mRed = rangeArray(red, pxSize)
      mGreen = rangeArray(green, pxSize)
      mBlue = rangeArray(blue, pxSize)

      #""" put all RGB color together """
      color = makeColor(mRed, mGreen, mBlue)
      #""" set pixel npx with the color """
      setColor(npx, color)

      #""" deleting the px array """
      del px

    repaint(pictureDetails[0])

  saveNewPicture(pictureDetails[0], pictureDetails[1])

  return

def meanFilter(pic, ySize, xSize, folder):
  pictureDetails = createNewPicture(xSize, ySize, "MeanFilter", folder)

  #"""Navigating in y-axes """
  for y in range (0, ySize):
    #"""Navigating in x-axes """
    for x in range (0, xSize):
      #""" declare a new vectors """
      red = []
      blue = []
      green = []
      px = []

      analyzePixel(px, pic, x, y, red, blue, green)
      
      npx = getPixel(pictureDetails[0], x, y)
      pxSize = len(px)-1
      
      mRed = mean(red)
      mGreen = mean(green)
      mBlue = mean(blue)

      #""" put all RGB color together """
      color = makeColor(mRed, mGreen, mBlue)
      #""" set pixel npx with the color """
      setColor(npx, color)

      #""" deleting the px array """
      del px

    repaint(pictureDetails[0])

  saveNewPicture(pictureDetails[0], pictureDetails[1])

  return  

#""" Black and White Filtering """
def BnWFilter(pic, ySize, xSize, folder):
  pictureDetails = createNewPicture(xSize, ySize, "BnWFilter", folder)

  #"""Navigating in y-axes """
  for y in range (0, ySize):
    #"""Navigating in x-axes """
    for x in range (0, xSize):
      #""" declare a new vectors """
      red = []
      blue = []
      green = []
      px = []
      bnwColor = []

      analyzePixel(px, pic, x, y, red, blue, green)
      
      npx = getPixel(pictureDetails[0], x, y)
      pxSize = len(px)-1
      
      mRed = median(red, pxSize)
      mGreen = median(green, pxSize)
      mBlue = median(blue, pxSize)

      bnwColor = bnw(mRed,mGreen,mBlue)

      #""" put all RGB color together """
      color = makeColor(bnwColor[0], bnwColor[1], bnwColor[2])
      #""" set pixel npx with the color """
      setColor(npx, color)

      #""" deleting the px array """
      del px

    repaint(pictureDetails[0])

  saveNewPicture(pictureDetails[0], pictureDetails[1])

  return

#""" Red and Grey Filtering """
def RedNGreyFilter(pic, ySize, xSize, folder):
  pictureDetails = createNewPicture(xSize, ySize, "RedNGreyFilter", folder)

  #"""Navigating in y-axes """
  for y in range (0, ySize):
    #"""Navigating in x-axes """
    for x in range (0, xSize):
      #""" declare a new vectors """
      red = []
      blue = []
      green = []
      px = []
      redNgreyColor = []

      analyzePixel(px, pic, x, y, red, blue, green)
      
      npx = getPixel(pictureDetails[0], x, y)
      pxSize = len(px)-1
      
      mRed = median(red, pxSize)
      mGreen = median(green, pxSize)
      mBlue = median(blue, pxSize)

      redNgreyColor = RedNGrey(mRed,mGreen,mBlue)

      #""" put all RGB color together """
      color = makeColor(redNgreyColor[0], redNgreyColor[1], redNgreyColor[2])
      #""" set pixel npx with the color """
      setColor(npx, color)

      #""" deleting the px array """
      del px

    repaint(pictureDetails[0])

  saveNewPicture(pictureDetails[0], pictureDetails[1])

  return

#""" Green and Grey Filtering """
def GreenNGreyFilter(pic, ySize, xSize, folder):
  pictureDetails = createNewPicture(xSize, ySize, "GreenNGreyFilter", folder)

  #"""Navigating in y-axes """
  for y in range (0, ySize):
    #"""Navigating in x-axes """
    for x in range (0, xSize):
      #""" declare a new vectors """
      red = []
      blue = []
      green = []
      px = []
      greenNgreyColor = []

      analyzePixel(px, pic, x, y, red, blue, green)
      
      npx = getPixel(pictureDetails[0], x, y)
      pxSize = len(px)-1
      
      mRed = median(red, pxSize)
      mGreen = median(green, pxSize)
      mBlue = median(blue, pxSize)

      greenNgreyColor = GreenNGrey(mRed,mGreen,mBlue)

      #""" put all RGB color together """
      color = makeColor(greenNgreyColor[0], greenNgreyColor[1], greenNgreyColor[2])
      #""" set pixel npx with the color """
      setColor(npx, color)

      #""" deleting the px array """
      del px

    repaint(pictureDetails[0])

  saveNewPicture(pictureDetails[0], pictureDetails[1])

  return

#""" Blue and Grey Filtering """
def BlueNGreyFilter(pic, ySize, xSize, folder):
  pictureDetails = createNewPicture(xSize, ySize, "BlueNGreyFilter", folder)

  #"""Navigating in y-axes """
  for y in range (0, ySize):
    #"""Navigating in x-axes """
    for x in range (0, xSize):
      #""" declare a new vectors """
      red = []
      blue = []
      green = []
      px = []
      blueNgreyColor = []

      analyzePixel(px, pic, x, y, red, blue, green)
      
      npx = getPixel(pictureDetails[0], x, y)
      pxSize = len(px)-1
      
      mRed = median(red, pxSize)
      mGreen = median(green, pxSize)
      mBlue = median(blue, pxSize)

      blueNgreyColor = BlueNGrey(mRed,mGreen,mBlue)

      #""" put all RGB color together """
      color = makeColor(blueNgreyColor[0], blueNgreyColor[1], blueNgreyColor[2])
      #""" set pixel npx with the color """
      setColor(npx, color)

      #""" deleting the px array """
      del px

    repaint(pictureDetails[0])

  saveNewPicture(pictureDetails[0], pictureDetails[1])

  return

#""" Green and Grey Filtering """
def GreyFilter(pic, ySize, xSize, folder):
  pictureDetails = createNewPicture(xSize, ySize, "GreyFilter", folder)

  #"""Navigating in y-axes """
  for y in range (0, ySize):
    #"""Navigating in x-axes """
    for x in range (0, xSize):
      #""" declare a new vectors """
      red = []
      blue = []
      green = []
      px = []
      greyColor = []

      analyzePixel(px, pic, x, y, red, blue, green)
      
      npx = getPixel(pictureDetails[0], x, y)
      pxSize = len(px)-1
      
      mRed = median(red, pxSize)
      mGreen = median(green, pxSize)
      mBlue = median(blue, pxSize)

      greyColor = grey(mRed,mGreen,mBlue)

      #""" put all RGB color together """
      color = makeColor(greyColor[0], greyColor[1], greyColor[2])
      #""" set pixel npx with the color """
      setColor(npx, color)

      #""" deleting the px array """
      del px

    repaint(pictureDetails[0])

  saveNewPicture(pictureDetails[0], pictureDetails[1])

  return

def iniciate():
  #""" declare a new array to have returnable values """
  configuration = []

  #""" declare a new array from picture """
  pic = []
  
  #""" pick all the photos and return the path of the folder """
  folder = pickFolder(pic)
  
  #""" showing all the 9 pictures """
  #for i in range (0, len(pic)):
  # show(pic[i])

  #""" check if pic is not null """
  if pic is not None:
    ySize = getHeight(pic[0]) #""" get the size of x-axes """
    xSize = getWidth(pic[0]) #""" get the size of y-axes """
    
    configuration.append(pic) #""" configuration[0] = pic """
    configuration.append(xSize) #""" configuration[1] = xSize """
    configuration.append(ySize) #""" configuration[2] = ySize """
    configuration.append(folder) #""" configuration[3] = folder """
  
  return configuration
  
#""" Main """
again = True
configuration = iniciate()
while (again == True):
  
  goOn = True
  if (configuration): #""" check if the array is different from null """
    while (goOn == True): #""" If the user select a number that is not accept as a input everything above is gonna repeat """
      number = requestInteger("Choose a filter:\n 1-MedianFilter, 2-ModeFilter,\n 3-RangeFilter, 4-MeanFilter,\n 5-BlackNWhiteFilter, 6-RedNGrey,\n 7-GreenNGrey, 8-BlueNGrey,\n 9-Grey")
      if (number == 1):
        goOn = False
        medianFilter(configuration[0], configuration[2], configuration[1], configuration[3])
      else: 
        if (number == 2):
          goOn = False
          modeFilter(configuration[0], configuration[2], configuration[1], configuration[3])
        else:
          if (number == 3):
            goOn = False
            rangeFilter(configuration[0], configuration[2], configuration[1], configuration[3])
          else:
            if (number == 4):
              goOn = False
              meanFilter(configuration[0], configuration[2], configuration[1], configuration[3])
            else:
              if (number == 5):
                goOn = False
                BnWFilter(configuration[0], configuration[2], configuration[1], configuration[3])
              else:
                if (number == 6):
                  goOn = False
                  RedNGreyFilter(configuration[0], configuration[2], configuration[1], configuration[3])
                else:
                  if (number == 7):
                    goOn = False
                    GreenNGreyFilter(configuration[0], configuration[2], configuration[1], configuration[3])
                  else: 
                    if (number == 8):
                      goOn = False
                      BlueNGreyFilter(configuration[0], configuration[2], configuration[1], configuration[3])
                    else:
                      if (number == 9):
                        goOn = False
                        GreyFilter(configuration[0], configuration[2], configuration[1], configuration[3])
                      else:
                        goOn = True
  else:
    print ("!!! ERROR: couldn't iniciate !!!")

  confirmation = requestInteger("Do you wanna create another filter for the same images? \n1-Yes 2-No")
  if (confirmation == 1):
    again = True
  else:
    again = False
