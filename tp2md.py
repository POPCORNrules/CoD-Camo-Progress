#!/bin/env python
import sys
import os
import re

opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
camos = [ "DM-Ultra", "Dark-Aether" ]

cat = [
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

Assault_Rifles = [ "AK-47", "FFAR-1", "Krig-6", "QBZ-83", "XM4" ]
Handguns = [ "1911", "Diamatti", "Magnum" ]
Launchers = [ "Cigma-2", "RPG-7" ]
LMGs = [ "M60", "RPD", "Stoner-63" ]
Melee = [ "Knife" ]
Shotguns = [ "Gallo-SA-12", "Hauer-77" ]
SMGs = [ "AK-74u", "Bullfrog", "KSP-45", "Milano-821", "MP5" ]
Sniper_Rifles = [ "LW3-Tundra", "M82", "Pellington-703" ]
Special = [ "M79" ]
Tactical_Rifles = [ "AUG", "DMR-14", "M16", "Type-63" ]

dm = [ "Spray:\n- Shards\n- Ambush\n- Frozen Lake\n- Debris\n- Prosper\n\n",
       "Stripes:\n- Gravel\n- Graze\n- Frost\n- Thrash\n- Bengal\n\n",
       "Classic:\n- Platoon\n- Ash\n- Checkpoint\n- Coercion\n- Ransom\n\n",
       "Geometric:\n- Blockade\n- Warsaw\n- Transform\n- Fraction\n- Bloodline\n\n",
       "Flora:\n- Frith\n- Old Growth\n- Nectar\n- Lumber\n- Cherry Blossom\n\n",
       "Science:\n- Teleport\n- Cosmonaut\n- Decipher\n- Integer\n- Policia\n\n",
       "Psychedelic:\n- Groovy\n- Seducer\n- Blush\n- Melancholy\n- Bliss" ]

da = [ "Grunge:\n- Stroke\n- Glacier\n- Grudge\n- Bloodshed\n- Rotten\n\n",
       "Liquid:\n- Wasteland\n- Amphibian\n- Boundary\n- Threshold\n- Banished\n\n",
       "Brushstroke:\n- Extortion\n- Degeneration\n- Downfall\n- Drench\n- Chemical\n\n",
       "Vintage:\n- Decadence\n- Bravado\n- Funkadelic\n- Boutique\n- Maniac\n\n",
       "Fauna:\n- Growl\n- Scavenger\n- Zebra\n- Blue Tiger\n- Rising Tiger\n\n",
       "Topography:\n- Acidic\n- Gunrunner\n- Forecast\n- Cartographer\n- Sunder\n\n",
       "Infection:\n- Corrosion\n- Entropy\n- Contamination\n- Glitch\n- Conviction" ]

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

def readfolder(masterycamo):
    total = 0
    complete = 0
    markdown = ''
    for folder in cat:
        header = folder.replace("-"," ")
        markdown += "# " + header + "\n"
        _, _, filenames = next(walk(masterycamo + "/" + folder))
        for filename in filenames:
            filetotal, filecomplete = taskcount(masterycamo + "/" + folder + "/" + filename)
            total += filetotal
            complete += filecomplete
            name = filename.replace(".taskpaper", "")
            if filecomplete == filetotal:
                markdown += "- [x] " + name + "\n"
            else:
                markdown += "- [ ] " + name + "\n"
    percent = str(round((complete/total)*100))
    return markdown, percent

if "-i" in opts:
    print("Initializing Files...")
    for camo in camos:
        os.mkdir(camo)
        for catagory in cat:
            os.mkdir(camo + "/" + catagory)
            for gun in eval(catagory.replace("-","_")):
               tp = open(camo + "/" + catagory + "/" + gun + ".taskpaper","x")
               if camo == "DM-Ultra":
                   tp.writelines(dm)
               elif camo == "Dark-Aether":
                   tp.writelines(da)
               tp.close()
    print("Done.")

else:
    readme = open("README.md", "w")
    readme.writelines(readme_header)
    readme.close()
    readme = open("README.md", "a")
    for camo in camos:
        data = readfolder(camo)
        readme.write('## '+ camo.replace("-" ," ") + ' ![' + data[1] + '%](https://progress-bar.dev/' + data[1] + '/?width=200)\n')
        readme.write(data[0])
        readme.write('\n\n')
        print(camo.replace("-" ," ") + ' Completion: ' + data[1] + '%')
    readme.close()
