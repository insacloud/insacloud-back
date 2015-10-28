import ImageFormatter
from PIL import Image
import math

#databaseName = "events.db"
# event1 = "Concert_Mika_2012"
#
# dbMan = DatabaseManager.SqliteManager(databaseName)
#
# dbMan.create_event(event1)
#
# dbMan.insert_picture(event1, ["80", "Mika1.jpg"])

# Algo var
t = 3
z = 4

matrixA = [[0 for i in range(64)] for i in range(64)]

# Open Image :
imFormat =ImageFormatter.ImageFormatter("troll64x64.jpg")
color = imFormat.process_image()
image = imFormat.get_image()
#image.show()
pixel = image.load()

# Sur une suggestion de Lele :
caca = Image.new('L', (64*64, 64*64))

for x in range(image.size[0]):
    for y in range(image.size[1]):
        #Access pixel
        #print pixel[x,y]
        matrixA[x][y] = image


for k in range(t, 0, -1):
    print k
    dim1 = (len(matrixA)/z)*64
    matrixB = [[Image.new('L', (dim1,dim1)) for i in range(4)] for i in range(4)]
    dim2 = int(64*math.pow(z,k))
    print len(matrixA)
    for x in range(0, len(matrixA)):
        for y in range(0, len(matrixA)):
            #paste(matrixA[x][y], (x*64, y*64,(x+1)*64, (y+1)*64))
            i = int(y/len(matrixA)/z)
            j = int(x/len(matrixA)/z)
            #print str(x)+"-"+str(y)+"|"+str(j)+"-"+str(i)
            matrixB[j][i].paste(image, (x*64, y*64,(x+1)*64, (y+1)*64))

    matrixA = [[0 for i in range(4)] for i in range(4)]

    for x in range(len(matrixB)):
        for y in range(len(matrixB)):
            matrixB[x][y] = matrixB[x][y].resize((64,64), Image.ANTIALIAS)
            # Sauvegarde matrixB comme mosaic
            matrixA[x][y] = matrixB[x][y]

    matrixA[0][0].show()



# im.show()
