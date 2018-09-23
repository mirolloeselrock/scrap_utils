import subprocess
import os
import re
import ConfigParser

def getLength(ffmpeg_path, input_video):
    process = subprocess.Popen(ffmpeg_path + " " + "-i " + '"' + input_video + '"', stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    stdout, stderr = process.communicate()
    matches = re.search(r"Duration:\s{1}(?P<hours>\d+?):(?P<minutes>\d+?):(?P<seconds>\d+\.\d+?),", stdout, re.DOTALL).groupdict()
    return float(matches['seconds']) + 60 * float(matches['minutes']) + 3600 * float(matches['hours'])

def compressFiles():
    config = ConfigParser.RawConfigParser()   
    config.read("comp.cfg")
    FFMPEG_PATH = config.get("CONFIG", "FFMPEG_PATH")
    FFMPEG_CRF = config.get("CONFIG", "FFMPEG_CRF")
    FFMPEG_HILOS = config.get("CONFIG", "FFMPEG_HILOS")
    FFMPEG_PRESET = config.get("CONFIG", "FFMPEG_PRESET")
    RESOLUCION_ANCHO = config.get("CONFIG", "RESOLUCION_ANCHO")
    RESOLUCION_ALTO = config.get("CONFIG", "RESOLUCION_ALTO")
    DURACION_MAXIMA = int(config.get("CONFIG", "DURACION_MAXIMA"))
    SONIDO = config.get("CONFIG", "SONIDO")
    mypath = "./"
    onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
    soundStr = "-ac 1 " if SONIDO.lower() in ['true', '1', 'y', 'yes', 's', 'si'] else "-an"
    for file in onlyfiles:
        if file[-3:] == "mp4":
            length = getLength(FFMPEG_PATH, file) - DURACION_MAXIMA
            if length < 0:
                length = 0
            os.rename(file, file + ".bak")
            input = '-i "./{1}.bak" -ss {0} -profile:v high -level 3.1 -vcodec libx264 -crf {2} -vf "format=yuv420p,scale={3}:{4}:force_original_aspect_ratio=decrease,pad={3}:{4}:(ow-iw)/2:(oh-ih)/2,setsar=1" {5} -preset {6} -threads {7} "./{8}"'.format(length, file, FFMPEG_CRF, RESOLUCION_ANCHO, RESOLUCION_ALTO, soundStr, FFMPEG_PRESET, FFMPEG_HILOS, file)
            cmd = FFMPEG_PATH + " " + input     
            p = subprocess.Popen(cmd, shell=True)
            p.wait()

def main():
    compressFiles()

if __name__ == "__main__":
    main()