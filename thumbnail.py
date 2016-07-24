from PIL import Image,ImageDraw,ImageFont,ImageOps
import re

class Thumbnail(object):
    def __init__(self,path,block_size):
        self._image = Image.open(path).convert("RGBA")
        self._block_size = block_size

    def getImageContext(self):
        return self._image

    def getBlockSize(self):
        return self._block_size


class ThumbnailWithLocation(Thumbnail):

    def __init__(self,path,block_size):
        super().__init__(path,block_size)

    def process(self):
        draw = ImageDraw.Draw(self._image)
        if(self._block_size == 2):
            draw.rectangle([(0,0),(163,83)],fill=(0,0,0))
        else:
            draw.rectangle([(0,0),(83,83)],fill=(0,0,0))

        font = ImageFont.truetype('./08SeoulNamsanB.ttf',size=45)

        text = self.getLocation()

        if(self._block_size == 2):
            if(len(text) == 4):
                draw.text((38,21),text,font=font)
            else:
                draw.text((26,21),text,font=font)
        else:
            if(len(text) == 2):
                draw.text((19,21),text,font=font)
            else:
                draw.text((9,21),text,font=font)

        del draw

        self._image = ImageOps.expand(self._image,border=1,fill=(0,0,0))

        return self

    def getLocation(self):
        raise NotImplementedError

class BoothThumbnail(ThumbnailWithLocation):
    prog = re.compile(".+\/(.+)-(.+)-(.+)\.(png|jpg|jpeg|JPG|PNG|JPEG)")

    def __init__(self,path):
        super().__init__(path,1)
        result = self.prog.match(path)
        self.day = result.group(1)
        self.section = result.group(2)
        self.code = result.group(3)
        self.isSpecial = (self._image.size != (366,419))

        #resize image if it doesn't fit to regular size
        if self.isSpecial:
            self._image = self._image.resize((744,419))
            self._block_size = 2

    def getLocation(self):
        if(self.isSpecial):
            return self.section + '-' + self.code
        else:
            return self.code


class PocThumbnail(ThumbnailWithLocation):
    prog = re.compile(".+\/(.+)-(.+)\.(png|jpg|jpeg|JPG|PNG|JPEG)")

    def __init__(self,path):
        super().__init__(path,1)
        result = self.prog.match(path)
        self.section = result.group(1)
        self.code = result.group(2)

    def getLocation(self):
        return self.code


class LetterThumbnail(Thumbnail):
    def __init__(self,letter):
        path = './catalog_images/' + letter.lower() + '.jpg'
        super().__init__(path,1)


class HeaderThumbnail(Thumbnail):
    def __init__(self,path):
        super().__init__(path,4)


class LeaderThumbnail(Thumbnail):
    def __init__(self,path,size=2):
        super().__init__(path,size)
