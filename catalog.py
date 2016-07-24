from PIL import Image
from os import path
from os import mkdir
from page import Page
from thumbnail import *
from tqdm import tqdm

class Catalog(object):
    def __init__(self):
        self.pages = []
        self.pages.append(Page())

    def insertThumbnail(self,thumbnail):
        assert(isinstance(thumbnail,Thumbnail))
        last_page = self.pages[-1]
        try:
            last_page.insertThumbnail(thumbnail)
        except Exception as e:
            new_page = Page()
            self.pages.append(new_page)
            new_page.insertThumbnail(thumbnail)

    def insertNormalThumbnails(self,paths):
        current_section = ""
        for path in paths:
            thumbnail = BoothThumbnail(path).process()
            if thumbnail.section != current_section:
                current_section = thumbnail.section
                self.insertThumbnail(LetterThumbnail(current_section))
            self.insertThumbnail(thumbnail)

    def insertSpecialThumbnails(self,paths):
        self.insertThumbnail(LeaderThumbnail("./catalog_images/2_ori.jpg"))
        for path in paths:
            thumbnail = BoothThumbnail(path).process()
            self.insertThumbnail(thumbnail)

    def insertPocThumbnails(self,paths):
        for path in paths:
            thumbnail = PocThumbnail(path).process()
            self.insertThumbnail(thumbnail)

    def newPage(self):
        self.pages.append(Page())

    def save(self,directory):
        mkdir(directory)
        for i in tqdm(range(len(self.pages))):
            page = self.pages[i]
            save_path = path.join(directory,str(i) + ".png")
            page.save(save_path)


