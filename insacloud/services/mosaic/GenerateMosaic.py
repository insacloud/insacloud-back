from services.mosaic.ImageFormatter import ImageFormatter
from PIL import Image
import math
import random
from services.models import Mosaic, Event

class GenerateMosaic:
    def __init__(self, poster, pictures):
        # Algo var
        self.imageDim = 512 # all images will have imageDim*imageDim pixels
        self.mosaicDim = 64 # mosaic will have mosaicDim*mosaicDim images
        self.nbTilesPerDim = 4 # mosaic will have nbTilesPerDim*nbTilesPerDim tiles
        self.tileDim = int(self.mosaicDim/self.nbTilesPerDim) # tile will have tileDim*tileDim images
        self.mosaic = Image.new('L', (self.imageDim*self.nbTilesPerDim, self.imageDim*self.nbTilesPerDim)) # mosaic is generated by merging tiles
        self.zoom = 2
        # create mosaicDim*mosaicDim matrix
        mosaicMatrix = None
        # TODO - Build this dictionnary
        self.hueMap = {}
        self.poster = Image.open(poster.path)
        self.pixel = self.poster.load()
        self.mosaicMatrix = [[0 for i in range(self.mosaicDim)] for i in range(self.mosaicDim)]

        for picture in pictures:
          if picture.hue not in self.hueMap:
            self.hueMap[picture.hue]=[]
          self.hueMap[picture.hue].append(Image.open(picture.image.path))

    def find_closest_available_hue(self, targetHue, hueMap):
        if(str(targetHue) in hueMap):
            return hueMap[str(targetHue)][random.randint(0,len(hueMap[str(targetHue)])-1)]
        min=256
        k = None
        for key in hueMap:
            hue = int(key)
            if(abs(hue - targetHue) < min):
                min = abs(hue - targetHue)
                k = key
        return hueMap[k][random.randint(0,len(hueMap[k])-1)]

    def get_tile_or_picture(self, event_id, imagesPath, zoomLevel, row, column):
        if(zoomLevel == self.zoom + 1):
            return self.mosaicMatrix[row][column]
        return self.generate_tile(event_id, imagesPath, zoomLevel, row, column)


    def generate_tile(self, event_id, imagesPath, zoomLevel, row, column):

        tile = Image.new('L', (self.imageDim * self.nbTilesPerDim,self.imageDim * self.nbTilesPerDim)) 
        for i in range (row * self.nbTilesPerDim, (row+1) * self.nbTilesPerDim, 1):
            for j in range (column * self.nbTilesPerDim, (column+1) * self.nbTilesPerDim, 1):
                leftUpperX  = (i % self.nbTilesPerDim) * self.imageDim
                leftUpperY  = (j % self.nbTilesPerDim) * self.imageDim
                rightLowerX = (i % self.nbTilesPerDim + 1) * self.imageDim
                rightLowerY = (j % self.nbTilesPerDim + 1) * self.imageDim
                tile.paste(self.get_tile_or_picture(event_id, imagesPath, zoomLevel+1, i, j), (leftUpperX, leftUpperY, rightLowerX, rightLowerY))
        tile = tile.resize((self.imageDim,self.imageDim), Image.ANTIALIAS)
        if(zoomLevel):
            name = "tile_ev" + str(event_id) + "-" + "z" + str(zoomLevel) + "-" + str(row)+"_"+str(column)+".jpg"
        else: 
            name = "mosaic" + str(event_id) + ".jpg"
        path = imagesPath + name
        tile.save(path, "JPEG")
        mosaic = Mosaic()
        mosaic.event = Event.objects.get(pk=event_id)
        mosaic.level = zoomLevel
        mosaic.row = row
        mosaic.column = column
        mosaic.image.name = name
        mosaic.save()
        return tile
    
    def generate(self, event_id, imagesPath):
        # feed mosaicMatrix with mosaicDim*mosaicDim images
        ratio = self.imageDim/self.mosaicDim
        for x in range(self.mosaicDim):
            for y in range(self.mosaicDim):
                hueSum = 0
                # calculate average hue for matrix cell
                for i in range(int(x*ratio), int((x+1)*ratio), 1):
                  for j in range(int(y*ratio), int((y+1)*ratio), 1):
                    hueSum += self.pixel[i,j]
                hue = hueSum/(ratio*ratio)
                self.mosaicMatrix[x][y] = self.find_closest_available_hue(hue, self.hueMap)

        
        self.generate_tile(event_id, imagesPath, 0,0,0)
    

    # generate tiles and mosaic
    # might be functionalized (huge nb of vars+)
    # for i in range(0, self.nbTilesPerDim, 1): 
    #     for j in range(0, self.nbTilesPerDim, 1):          
    #         tile = Image.new('L', (self.imageDim*self.tileDim,self.imageDim*self.tileDim)) 
    #         tileMatrix = [[Image.new('L', (self.imageDim*self.nbTilesPerDim,self.imageDim*self.nbTilesPerDim)) for i in range(self.nbTilesPerDim)] for i in range(self.nbTilesPerDim)] 
    #         for k in range(i*self.tileDim, (i+1)*self.tileDim, 1): 
    #             for l in range(j*self.tileDim, (j+1)*self.tileDim, 1): 
    #                 m = int((k%self.tileDim) / self.nbTilesPerDim) 
    #                 n = int((l%self.tileDim) / self.nbTilesPerDim)  
    #                 q = k % self.nbTilesPerDim  # 0..3
    #                 r = l % self.nbTilesPerDim 
    #                 tileMatrix[m][n].paste(self.mosaicMatrix[k][l],(q*self.imageDim,r*self.imageDim,(q+1)*self.imageDim,(r+1)*self.imageDim))
    #                 # build tile with merging images
    #                 tile.paste(self.mosaicMatrix[k][l], ((k%self.tileDim)*self.imageDim, (l%self.tileDim)*self.imageDim,((k%self.tileDim)+1)*self.imageDim, ((l%self.tileDim)+1)*self.imageDim))
    #         # resize tile image
    #         tile = tile.resize((self.imageDim,self.imageDim), Image.ANTIALIAS)
    #         for x in range(0, self.nbTilesPerDim, 1):
    #             for y in range(0, self.nbTilesPerDim, 1):
    #                 tileMatrix[x][y] = tileMatrix[x][y].resize((self.imageDim,self.imageDim), Image.ANTIALIAS)
    #                 name = "tile_"+ str(event_id)+"-"+str(i * self.nbTilesPerDim + x)+"-"+str(j * self.nbTilesPerDim + y)+".jpg"
    #                 path = imagesPath + name
    #                 tileMatrix[x][y].save(path, "JPEG")
    #                 mosaic = Mosaic()
    #                 mosaic.event = Event.objects.get(pk=event_id)
    #                 mosaic.level = 2
    #                 mosaic.row = i * self.nbTilesPerDim + x
    #                 mosaic.column = j * self.nbTilesPerDim + y
    #                 mosaic.image.name = name
    #                 mosaic.save()

    #         # build mosaic with merging tiles
    #         self.mosaic.paste(tile, ((i%self.nbTilesPerDim)*self.imageDim, (j%self.nbTilesPerDim)*self.imageDim,((i%self.nbTilesPerDim)+1)*self.imageDim, ((j%self.nbTilesPerDim)+1)*self.imageDim))
    #         # export mosaic image
    #         name = "tile_"+str(event_id)+"-"+str(i)+"-"+str(j)+".jpg"
    #         path = imagesPath+name
    #         tile.save(path, "JPEG")

    #         mosaic = Mosaic()
    #         mosaic.event = Event.objects.get(pk=event_id)
    #         mosaic.level = 1
    #         mosaic.row = i
    #         mosaic.column = j
    #         mosaic.image.name = name
    #         mosaic.save()

    # # resize mosaic image
    # self.mosaic = self.mosaic.resize((self.imageDim,self.imageDim), Image.ANTIALIAS)
    # # export mosaic image
    # name = "mosaic_"+str(event_id)+".jpg"
    # path = imagesPath+name
    # self.mosaic.save(path, "JPEG")
    # mosaic = Mosaic()
    # mosaic.level = 0
    # mosaic.event = Event.objects.get(pk=event_id)
    # mosaic.image.name = name
    # mosaic.save()