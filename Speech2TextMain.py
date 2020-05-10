from ServerInteract import speech2text_wav
from os import listdir
from os.path import isfile, join
import re
from bcolors import bcolors

SoundWavDir = "./wav/"
TextDir = "./text/"
BeginCount = 0
soundfiles = [f for f in listdir(SoundWavDir) if isfile(join(SoundWavDir, f))]

if __name__ == '__main__':

    for soundfile in soundfiles:
        file_index = re.findall(r"\d+", soundfile)[0]
        if int(file_index) < BeginCount:
            continue
        soundfile_path = SoundWavDir + "record%d.wav" % int(file_index)
        text_result = speech2text_wav(soundfile_path)

        print(bcolors.HEADER + "Writing Text to %d.txt." % int(file_index))
        with open(TextDir + "%d.txt" % int(file_index), "w") as f:
            f.write(text_result)
            f.close()