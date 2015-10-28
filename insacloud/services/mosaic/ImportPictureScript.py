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
t = 3 # nb zoom level
z = 4 # mosaic = z*z tiles

# create 64x64 matrix
matrixA = [[0 for i in range(64)] for i in range(64)]

# Open Image :
imFormat =ImageFormatter.ImageFormatter("troll64x64.jpg")
# ?
color = imFormat.process_image()
# ?
image = imFormat.get_image()
#image.show()
pixel = image.load()

# Sur une suggestion de Lele :
# caca = Image.new('L', (64*64, 64*64))

# feed matrixA with 64x64 images
for x in range(image.size[0]):
    for y in range(image.size[1]):
        #Access pixel
        #print pixel[x,y]
        matrixA[x][y] = image # todo : get the "good" image

# generate

portion = int(64/z)
mosaic = Image.new('L', (512*z,512*z))
for i in range(0, z, 1):
    for j in range(0, z, 1):
        tile = Image.new('L', (64*portion,64*portion))
        for k in range(i*portion, (i+1)*portion, 1):
            for l in range(j*portion, (j+1)*portion, 1):
                tile.paste(matrixA[k][l], ((k%portion)*64, (l%portion)*64,((k%portion)+1)*64, ((l%portion)+1)*64))
        # tip = Image.fromlist(matrixB)
        tile = tile.resize((512,512), Image.ANTIALIAS)
        mosaic.paste(tile, ((i%z)*512, (j%z)*512,((i%z)+1)*512, ((j%z)+1)*512))
        tile.save("tile-"+str(i)+"-"+str(j)+".jpg", "JPEG")

mosaic = mosaic.resize((512,512), Image.ANTIALIAS)
mosaic.save("mosaic.jpg", "JPEG")

##################################

# for k in range(t, 0, -1):
#     print(k)
#     dim1 = int((len(matrixA)/z)*64)
#     matrixB = [[Image.new('L', (dim1,dim1)) for i in range(4)] for i in range(4)]
#     # dim2 = int(64*math.pow(z,k))
#     print(len(matrixA))
#     for x in range(0, len(matrixA)):
#         for y in range(0, len(matrixA)):
#             #paste(matrixA[x][y], (x*64, y*64,(x+1)*64, (y+1)*64))
#             i = int(y/len(matrixA)/z)
#             j = int(x/len(matrixA)/z)
#             #print str(x)+"-"+str(y)+"|"+str(j)+"-"+str(i)
#             matrixB[j][i].paste(image, (x*64, y*64,(x+1)*64, (y+1)*64))

#     matrixA = [[0 for i in range(4)] for i in range(4)]

#     for x in range(len(matrixB)):
#         for y in range(len(matrixB)):
#             matrixB[x][y] = matrixB[x][y].resize((64,64), Image.ANTIALIAS)
#             # Sauvegarde matrixB comme mosaic
#             matrixA[x][y] = matrixB[x][y]

#     matrixA[0][0].show()
#     matrixA[0][0].save("lol.jpg", "JPEG")



# im.show()