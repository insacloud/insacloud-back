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

    # generate tiles and mosaic
    # might be functionalized (huge nb of vars+)
    for i in range(0, self.nbTilesPerDim, 1): # 
        for j in range(0, self.nbTilesPerDim, 1):
            tile = Image.new('L', (self.imageDim*self.tileDim,self.imageDim*self.tileDim))
            for k in range(i*self.tileDim, (i+1)*self.tileDim, 1):
                for l in range(j*self.tileDim, (j+1)*self.tileDim, 1):
                    # build tile with merging images
                    tile.paste(self.mosaicMatrix[k][l], ((k%self.tileDim)*self.imageDim, (l%self.tileDim)*self.imageDim,((k%self.tileDim)+1)*self.imageDim, ((l%self.tileDim)+1)*self.imageDim))
            # resize tile image
            tile = tile.resize((self.imageDim,self.imageDim), Image.ANTIALIAS)
            # build mosaic with merging tiles
            self.mosaic.paste(tile, ((i%self.nbTilesPerDim)*self.imageDim, (j%self.nbTilesPerDim)*self.imageDim,((i%self.nbTilesPerDim)+1)*self.imageDim, ((j%self.nbTilesPerDim)+1)*self.imageDim))
            # export mosaic image
            path = imagesPath+"tile_"+str(event_id)+"-"+str(i)+"-"+str(j)+".jpg"
            tile.save(path, "JPEG")

            mosaic = Mosaic()
            mosaic.event = Event.objects.get(pk=event_id)
            mosaic.level = 1
            mosaic.row = i
            mosaic.column = j
            mosaic.image = path
            mosaic.save()

    # resize mosaic image
    self.mosaic = self.mosaic.resize((self.imageDim,self.imageDim), Image.ANTIALIAS)
    # export mosaic image
    path = imagesPath+"mosaic_"+str(event_id)+".jpg"
    self.mosaic.save(path, "JPEG")
    mosaic = Mosaic()
    mosaic.level = 0
    mosaic.event = Event.objects.get(pk=event_id)
    mosaic.image = path
    mosaic.save()