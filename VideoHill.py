import os
import subprocess


def replaceAllPS1Video(binpath, avipaths, indices):

    subprocess.call(["java", "-jar", "jpsxdec.jar", "-f", binpath, "-x", "gameIndex.idx"])

    for d in range(len(avipaths)):
        replacePS1Video(binpath, avipaths[d], indices[d], getIndex = False)


    return

def replacePS1Video(binPath, aviPath, indexNumber, paddims=(304,240), getIndex = False):
    aviFileName = os.path.basename(aviPath)
    aviDir = aviPath.replace(aviFileName, "")

    frameDirName = aviFileName + "_FRAMES"
    framesPath = os.path.join(aviDir, frameDirName)
    os.makedirs(framesPath, exist_ok=True)
    
    #Convert video to frames
    subprocess.call(["ffmpeg", "-i", aviPath, "-vf", f"scale={str(paddims[0])}:{str(paddims[1])}:force_original_aspect_ratio=decrease,pad={str(paddims[0])}:{str(paddims[1])}:(ow-iw):0,setsar=1" , framesPath + r"/%04d.png"])
    n_frames = len(os.listdir(framesPath))

    if getIndex:
        #get index of game
        subprocess.call(["java", "-jar", "jpsxdec.jar", "-f", binPath, "-x", "gameIndex.idx"])

    #Construct xml file
    xmlFileName = aviFileName.upper().replace(".AVI", ".XML")
    xmlPath = os.path.join(aviDir, xmlFileName)

    xmlFile = open(xmlPath, "w")

    xmlFile.write("<?xml version=\"1.0\"?>\n<str-replace version=\"0.3\">\n")
    for f in range(n_frames):
        xmlFile.write("\t<replace frame=\"" + str(f+1) + "\">" + framesPath + "/" + str(f+1).zfill(4) + ".png</replace>\n")
    xmlFile.write("</str-replace>")
    xmlFile.close()
    #inject frames
    subprocess.call(["java", "-jar", "jpsxdec.jar", "-x", "gameIndex.idx", "-i", str(indexNumber), "-replaceframes", xmlPath])
    return