import ImageProcessor
import subprocess
import os
import VideoHill

VIDEOS = {"ENDING":42,
          "COMP":39,
          "OPEN":47}

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
    
    

    os.chdir("mkpsxiso")
    subprocess.call(["mkpsxiso.exe", "JC.xml", "-y"])

    #p = subprocess.Popen("build.bat")
    #stdout, stderr = p.communicate()

    os.chdir("..")
    FMV_PATHS = [r"FMV/OPEN_EDIT.avi", r"FMV/ENDING_EDIT.avi", r"FMV/COMP_EDIT.avi"]
    INDICES = [47, 42, 39]

    #VideoHill.replaceAllPS1Video(r"mkpsxiso/JC.bin", FMV_PATHS, INDICES)

build()