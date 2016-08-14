#!/usr/bin/env python
import re
import subprocess
import shutil
from os import path
from glob import glob
from thumbnail import *
from page import Page
from catalog import Catalog
from tqdm import tqdm


def getPaths(pattern):
    paths = glob(pattern)
    paths.sort()
    return paths

BUILD_DIR = "./build"
CATALOG_DIR = "./build/booth_catalog"

if __name__ == "__main__":
    shutil.rmtree(CATALOG_DIR)
    print("* Begin processing boothcuts...")
    catalog = Catalog()

    catalog.insertThumbnail(HeaderThumbnail("./catalog_images/1_head_1_sat.jpg"))
    catalog.insertSpecialThumbnails(getPaths("./images/special/sat*"))
    catalog.insertNormalThumbnails(getPaths("./images/normal/sat*"))
    catalog.insertThumbnail(HeaderThumbnail("./catalog_images/1_head_2_both.jpg"))
    catalog.insertSpecialThumbnails(getPaths("./images/special/both*"))
    catalog.insertNormalThumbnails(getPaths("./images/normal/both*"))
    catalog.insertThumbnail(HeaderThumbnail("./catalog_images/1_head_3_sun.jpg"))
    catalog.insertSpecialThumbnails(getPaths("./images/special/sun*"))
    catalog.insertNormalThumbnails(getPaths("./images/normal/sun*"))

    catalog.newPage()
    catalog.insertThumbnail(HeaderThumbnail("./catalog_images/1_head_poc_1_sat.jpg"))
    catalog.insertThumbnail(LeaderThumbnail("./catalog_images/sat_Pc1.jpg",1))
    catalog.insertPocThumbnails(getPaths("./images/poc/sat-Pc1*"))
    catalog.insertThumbnail(LeaderThumbnail("./catalog_images/sat_Pc3.jpg",1))
    catalog.insertPocThumbnails(getPaths("./images/poc/sat-Pc3*"))
    catalog.insertThumbnail(LeaderThumbnail("./catalog_images/sat_Pc4.jpg",1))
    catalog.insertPocThumbnails(getPaths("./images/poc/sat-Pc4*"))
    catalog.insertThumbnail(LeaderThumbnail("./catalog_images/sat_Pc5.jpg",1))
    catalog.insertPocThumbnails(getPaths("./images/poc/sat-Pc5*"))
    catalog.insertThumbnail(LeaderThumbnail("./catalog_images/sat_Pc6.jpg",1))
    catalog.insertPocThumbnails(getPaths("./images/poc/sat-Pc6*"))
    catalog.insertThumbnail(LeaderThumbnail("./catalog_images/sat_Pc7.jpg",1))
    catalog.insertPocThumbnails(getPaths("./images/poc/sat-Pc7*"))
    catalog.insertThumbnail(HeaderThumbnail("./catalog_images/1_head_poc_2_both.jpg"))
    catalog.insertThumbnail(HeaderThumbnail("./catalog_images/sun_before_Pc2.jpg"))
    catalog.insertThumbnail(HeaderThumbnail("./catalog_images/1_head_poc_3_sun.jpg"))
    catalog.insertThumbnail(LeaderThumbnail("./catalog_images/sun_Pc1.jpg",1))
    catalog.insertPocThumbnails(getPaths("./images/poc/sun-Pc1*"))
    catalog.insertThumbnail(LeaderThumbnail("./catalog_images/sun_Pc3.jpg",1))
    catalog.insertPocThumbnails(getPaths("./images/poc/sun-Pc3*"))
    catalog.insertThumbnail(LeaderThumbnail("./catalog_images/sun_Pc4.jpg",1))
    catalog.insertPocThumbnails(getPaths("./images/poc/sun-Pc4*"))
    catalog.insertThumbnail(LeaderThumbnail("./catalog_images/sun_Pc5.jpg",1))
    catalog.insertPocThumbnails(getPaths("./images/poc/sun-Pc5*"))
    catalog.insertThumbnail(LeaderThumbnail("./catalog_images/sun_Pc6.jpg",1))
    catalog.insertPocThumbnails(getPaths("./images/poc/sun-Pc6*"))
    catalog.save('./build/booth_catalog')

    print("* Catalog is done. Begin zipping")

    subprocess.call("zip -r build/catalog.zip ./build/booth_catalog",shell=True)
