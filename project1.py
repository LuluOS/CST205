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
def pickPicture(vector):
  folder = pickAFolder()
  if folder is not None:
    photos = []

    for imageNumber in range(0,8):
      imagePath = folder + str(imageNumber + 1) + ".png"
      photos.append(makePicture(imagePath))
  
    return photos
  else:
    print ("!!! ERROR: invalid input for pickPicture() !!!")

#""" createNewPicture(xSize, ySize) """
def createNewPicture(xSize, ySize, nameOfImage):
  #""" creating a new picture with the size of xSize X ySize """
  newPicture = makeEmptyPicture(xSize, ySize)
  #""" defining a path for the new picture """
  newPath = "C:\\Users\\Luana\\Desktop\\CSUMB\\CST205-Multimedia\\Project1\\Project1Images\\"
  newPath = newPath + str(nameOfImage) + ".png"

  pictureDetails = []
  pictureDetails.append(newPicture) #""" pictureDetails[0] = newPicture """
  pictureDetails.append(newPath) #""" pictureDetails[1] = newPath """   

  #""" saving the new picture in newPath """
  writePictureTo(newPicture, newPath)

  return pictureDetails
  
#"""saveNewPicture(newPicture, newPath)"""
def saveNewPicture(newPicture, newPath):
  #""" saving the new picture in newPath """
  writePictureTo(newPicture, newPath)

  show(newPicture)
  return

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
  flag = 0
  quantity = []
  for i in range (len(numbers)):
    qnt = diffQuantity(numbers[i], lst)
    quantity.append(qnt)
    if (bigger < quantity[i]):
      bigger = quantity[i]
      often = numbers[i]
      flag = 1
    else:
      if (bigger > quantity[i]):
        flag = 2
      else:
        flag = 0

  if (flag == 0):
    return median(lst,pxSize)
  else:
    return often

#""" return the range of the lst """ 
def rangeArray(lst, pxSize):
  quicksort(lst,0,pxSize)

  rangeOf = lst[len(lst)-1] - lst[0]

  return rangeOf

#""" return the range of the lst """ 
def bnw(lst, pxSize):
  quicksort(lst,0,pxSize)
  m = median(lst,pxSize)

  #print ("M = %d" %m)
  if (m >= 0) & (m <= 127):
    m = 0
  else:
      if (m >= 128) & (m <= 255):
        m = 255
     
  return m

#""" Filtering with the median """
def medianFilter(pic, ySize, xSize):
  pictureDetails = createNewPicture(xSize, ySize, "medianFilter")

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
def modeFilter(pic, ySize, xSize):
  pictureDetails = createNewPicture(xSize, ySize, "modeFilter")

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
def rangeFilter(pic, ySize, xSize):
  pictureDetails = createNewPicture(xSize, ySize, "rangeFilter")

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

#""" Filtering with the range """
def BnWFilter(pic, ySize, xSize):
  pictureDetails = createNewPicture(xSize, ySize, "rangeFilter")

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
      
      mRed = bnw(red, pxSize)
      mGreen = bnw(green, pxSize)
      mBlue = bnw(blue, pxSize)

      #""" put all RGB color together """
      color = makeColor(mRed, mGreen, mBlue)
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
  #""" add the pictures in the end of the array """
  pic = pickPicture(pic)

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
  
  return configuration
  
#""" Main """
configuration = iniciate()
if (configuration): #""" check if the array is different from null """
  number = requestNumber("Choose a filter: 1-MedianFilter, 2-ModeFilter, 3-RangeFilter, 4-BlackNWhiteFilter")
  if (number == 1):
    medianFilter(configuration[0], configuration[2], configuration[1])
  else: 
    if (number == 2):
      modeFilter(configuration[0], configuration[2], configuration[1])
    else:
      if (number == 3):
        rangeFilter(configuration[0], configuration[2], configuration[1])
      else:
        if (number == 4):
          BnWFilter(configuration[0], configuration[2], configuration[1])
else:
  print ("!!! ERROR: couldn't iniciate !!!")