from cImage import*

def grayPixel(oldpixel):
    oldpixel.setRed(165)
    return oldpixel

def imageIntensityR(oldImage):
    oldW = oldImage.getWidth()
    oldH = oldImage.getHeight()

    newIm = EmptyImage(oldW, oldH)

    for row in range(oldH):
        for col in range(oldW):

            oldPixel = oldImage.getPixel(col,row)

            newIm.setPixel(col, row, grayPixel(oldPixel))

    return newIm

def makeNewColor(imageFile):
    oldImage = FileImage(imageFile)
    width = oldImage.getWidth()
    height = oldImage.getHeight()

    myWin = ImageWin("Red Intensity", width*2, height)
    oldImage.draw(myWin)

    newImage = imageIntensityR(oldImage)
    newImage.setPosition(width + 1, 0)
    newImage.draw(myWin)

    myWin.exitOnClick()

makeNewColor("butterfly.gif")
