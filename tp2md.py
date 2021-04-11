#!/bin/env python
import re
from os import walk
folders = [
    "Assault-Rifles",
    "Handguns",
    "Launchers",
    "LMGs",
    "Melee",
    "Shotguns",
    "SMGs",
    "Sniper-Rifles",
    "Special",
    "Tactical-Rifles"
]
readme_header = [
    "# CW-Camo-Progress\n",
    "Taskpaper lists for my Cold War camo progress\n",
    "\n\n",
    "# Current Progress\n"
]
h2 = re.compile('^(\\W+)?(.*)\\:$', re.MULTILINE)
unchecked = re.compile('^(\\W+)?(-\\W)(.*)$', re.MULTILINE)
done = re.compile('^(\\W+)?(-\\W\\[\\W\\]\\W)(.*)(\\W@done)$', re.MULTILINE)


def taskcount(filename):
    total = 0
    complete = 0
    file = open(filename, "r")
    filelines = file.readlines()
    for line in filelines:
        if "-" in line:
            total += 1
        if "@done" in line:
            complete += 1
    file.close()
    return total, complete

def readfolder(foldername):
    total = 0
    complete = 0
    markdown = ''
    for folder in folders:
        header = folder.replace("-"," ")
        markdown += "# " + header + "\n"
        _, _, filenames = next(walk(foldername + "/" + folder))
        for filename in filenames:
            filetotal, filecomplete = taskcount(foldername + "/" + folder + "/" + filename)
            total += filetotal
            complete += filecomplete
            name = filename.replace(".taskpaper", "")
            weapon = name.replace("-"," ")
            if filecomplete == filetotal:
                markdown += "- [x]" + name + "\n"
            else:
                markdown += "- [ ]" + name + "\n"
    percent = str(round((complete/total)*100))
    return markdown, percent

dm_ultra = readfolder("DM-Ultra")
dark_aether = readfolder("Dark-Aether")

readme = open("README.md", "w")
readme.writelines(readme_header)
readme.close()
readme = open("README.md", "a")
readme.write('## Gold Camo ![' + dm_ultra[1] + '%](https://progress-bar.dev/' +
             dm_ultra[1] + '/?width=200&color=babaca)\n')
readme.write(dm_ultra[0])
readme.write('\n\n\n')
readme.write('## Golden Viper Camo ![' + dark_aether[1] + '%](https://progress-bar.dev/' +
             dark_aether[1] + '/?width=200&color=babaca)\n')
readme.write(dark_aether[0])
readme.close()
