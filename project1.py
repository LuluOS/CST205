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
  if start < end:                            # If there are two or more elements...
    split = partition(list, start, end)    # ... partition the sublist...
    quicksort(list, start, split-1)        # ... and sort both halves.
    quicksort(list, split+1, end)
  else:
    return

#""" Median """
#""" http://stackoverflow.com/questions/24101524/finding-median-of-list-in-python """
def median(lst):
    lst = sorted(lst)
    if len(lst) < 1:
            return None
    if len(lst) %2 == 1:
            return lst[((len(lst)+1)/2)-1]
    else:
            return float(sum(lst[(len(lst)/2)-1:(len(lst)/2)+1]))/2.0

#""" Main """
#""" declare a new array from picture """
pic = []
#""" add the pictures in the end of the array """
pic.append(makePicture("C:\\Users\\Luana\\Dropbox\\CSUMB\\CST205-Multimedia\\Project1\\Project1Images\\1.png"))
pic.append(makePicture("C:\\Users\\Luana\\Dropbox\\CSUMB\\CST205-Multimedia\\Project1\\Project1Images\\2.png"))
pic.append(makePicture("C:\\Users\\Luana\\Dropbox\\CSUMB\\CST205-Multimedia\\Project1\\Project1Images\\3.png"))
pic.append(makePicture("C:\\Users\\Luana\\Dropbox\\CSUMB\\CST205-Multimedia\\Project1\\Project1Images\\4.png"))
pic.append(makePicture("C:\\Users\\Luana\\Dropbox\\CSUMB\\CST205-Multimedia\\Project1\\Project1Images\\5.png"))
pic.append(makePicture("C:\\Users\\Luana\\Dropbox\\CSUMB\\CST205-Multimedia\\Project1\\Project1Images\\6.png"))
pic.append(makePicture("C:\\Users\\Luana\\Dropbox\\CSUMB\\CST205-Multimedia\\Project1\\Project1Images\\7.png"))
pic.append(makePicture("C:\\Users\\Luana\\Dropbox\\CSUMB\\CST205-Multimedia\\Project1\\Project1Images\\8.png"))
pic.append(makePicture("C:\\Users\\Luana\\Dropbox\\CSUMB\\CST205-Multimedia\\Project1\\Project1Images\\9.png"))

#""" showing all the 9 pictures """
#for i in range (0, len(pic)):
# show(pic[i])

ySize = getHeight(pic[0]) #""" get the size of x-axes """
xSize = getWidth(pic[0]) #""" get the size of y-axes """
#print ("xSize = %d" %xSize)
#print ("ySize = %d" %ySize)

#""" creating a new picture with the size of xSize X ySize """
newPicture = makeEmptyPicture(xSize, ySize)
#""" defining a path for the new picture """
newPath = "C:\\Users\\Luana\\Dropbox\\CSUMB\\CST205-Multimedia\\Project1\\Project1Images\\new.png"
#""" saving the new picture in newPath """
writePictureTo(newPicture, newPath)

for y in range (0, ySize):
  for x in range (0, xSize):
    #""" declare a new vectors """
    red = []
    blue = []
    green = []
    px = []

    #""" navegating in the same pixel to compare each pixel from the 9 images """
    for picture in range (0, len(pic)):
      #print ("(%d,%d) picture = %d" %(x,y,picture))
      #""" px has the pixel from the position x,y """
      px.append(getPixel(pic[picture], x, y))
      
      #""" get the degree of red from the pixel """
      redDegree = getRed(px[picture])
      #""" store the redDegree in the red array """
      red.insert(picture, redDegree)
      #print ("red[%d] = %d" %(picture,red[picture]))
      
      #""" get the degree of blue from the pixel """
      blueDegree = getBlue(px[picture])
      #""" store the blueDegree in the blue array """
      blue.insert(picture, blueDegree)
      #print ("blue[%d] = %d" %(picture,blue[picture]))
      
      #""" get the degree of green from the pixel """
      greenDegree = getGreen(px[picture])
      #""" store the greenDegree in the red array """
      green.insert(picture, greenDegree)
      #print ("green[%d] = %d" %(picture,green[picture]))
      
    npx = getPixel(newPicture, x, y)
    pxSize = len(px)-1
    #print ("pxSize = %d" %pxSize)

    quicksort(red,0,pxSize)
    #print ("After myQuicksort: "),
    #print red
    #print median(red)
    mRed = median(red)

    quicksort(green,0,8)
    #print ("After myQuicksort: "),
    #print green
    #print median(green)
    mGreen = median(green)

    quicksort(blue,0,8)
    #print ("After myQuicksort: "),
    #print blue
    #print median(blue)
    mBlue = median(blue)

    color = makeColor(mRed, mGreen, mBlue)
    setColor(npx, color)
    
    #""" deleting the px array """
    del px

#""" saving the new picture in newPath """
writePictureTo(newPicture, newPath)

show(newPicture)
