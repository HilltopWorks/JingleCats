import ImageProcessor
import subprocess
import os


def build():
    os.chdir("PS1_Base_Project")
    p = subprocess.Popen("clean.bat")
    stdout, stderr = p.communicate()

    os.chdir("..")
    ImageProcessor.injectSelectText()
    ImageProcessor.injectStocks("STOCK_IMAGES", "STOCK_IMAGES_ORIGINAL")
    
    ImageProcessor.injectFailText()
    ImageProcessor.injectOptionsText()
    ImageProcessor.injectGuideText()
    ImageProcessor.injectBigText()
    

    os.chdir("PS1_Base_Project")
    p = subprocess.Popen("build.bat")
    stdout, stderr = p.communicate()


build()