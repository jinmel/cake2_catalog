from PIL import Image,ImageDraw

class Page(object):
    def __init__(self):
        self.block_count = 0
        self.image = Image.open('./catalog_images/0_paper.jpg').convert("RGBA")

    def insertThumbnail(self,thumbnail):
        #shift to next row if thumbnail doesn't fit
        if self.block_count % thumbnail.getBlockSize()!= 0:
            self.block_count += (4 - (self.block_count % 4))

        if(self.block_count >= 20):
            raise Exception('block exceeded!')

        row = int(self.block_count / 4)
        col = self.block_count % 4

        x = 161 + col * 377
        y = 131 + row * 443
        self.image.paste(thumbnail.getImageContext(),(x,y))
        self.block_count += thumbnail.getBlockSize()

        return self

    def getImageContext(self):
        return self.image

    def save(self,path):
        self.image.save(path,"PNG",compress_level=0)

