from services.mosaic.ImageFormatter import ImageFormatter
from PIL import Image
import math
import random
from services.models import Mosaic, Event

class GenerateMosaic:
    def __init__(self, poster, pictures):
        # Algo var
        self.imageDim = 512 # all images will have imageDim*imageDim pixels
        self.nbTilesPerDim = 4 # mosaic will have nbTilesPerDim*nbTilesPerDim tiles
        self.zoom = 2
        self.mosaicDim = int(math.pow(self.nbTilesPerDim, (self.zoom+1))) # mosaic will have mosaicDim*mosaicDim images
        
        mosaicMatrix = None
        self.hueMap = {}
        self.poster = Image.open(poster.path) 
        self.poster.resize((self.mosaicDim,self.mosaicDim), Image.ANTIALIAS) #the poster should be divided in mosaicDim*mosaicDim patch, here a patch is a pixel
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

        tile = Image.new('L', (self.imageDim * self.nbTilesPerDim, self.imageDim * self.nbTilesPerDim)) 
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

        for x in range(self.mosaicDim):
            for y in range(self.mosaicDim):
                self.mosaicMatrix[x][y] = self.find_closest_available_hue(self.pixel[x,y], self.hueMap)

        
        self.generate_tile(event_id, imagesPath, 0,0,0)    