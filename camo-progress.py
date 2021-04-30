#!/bin/env python
import sys
import os

opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
camos = ["DM-Ultra", "Dark-Aether"]

cat = [
    "Assault-Rifles",
    "Pistols",
    "Launchers",
    "LMGs",
    "Melee",
    "Shotguns",
    "SMGs",
    "Sniper-Rifles",
    "Special",
    "Tactical-Rifles"
]

Assault_Rifles = [["XM4", "AK-47", "Krig 6", "QBZ-83", "FFAR 1", "Groza", "FARA 83"], [5]]
Pistols = [["1911", "Magnum", "Diamatti"], [3]]
Launchers = [["Cigma-2", "RPG-7"], [2]]
LMGs = [["Stoner 63", "RPD", "M60"], [3]]
Melee = [["Knife", "Sledgehammer", "Wakizashi", "E-Tool", "Machete"], [1]]
Shotguns = [["Hauer-77", "Gallo SA12", "Streetsweeper"], [2]]
SMGs = [["MP5", "Milano 821", "AK-74u", "KSP 45", "Bullfrog", "MAC-10", "LC10", "PPSh-41"], [5]]
Sniper_Rifles = [["Pellington 703", "LW3-Tundra", "M82", "ZRG 20mm", "Swiss K31"], [3]]
Special = [["M79", "R1 Shadowhunter", "Ballistic Knife"], [1]]
Tactical_Rifles = [["Type 63", "M16", "AUG", "DMR 14"], [4]]

dm = ["Spray:\n - Shards\n - Ambush\n - Frozen Lake\n - Debris\n - Prosper\n\n",
      "Stripes:\n - Gravel\n - Graze\n - Frost\n - Thrash\n - Bengal\n\n",
      "Classic:\n - Platoon\n - Ash\n - Checkpoint\n - Coercion\n - Ransom\n\n",
      "Geometric:\n - Blockade\n - Warsaw\n - Transform\n - Fraction\n - Bloodline\n\n",
      "Flora:\n - Frith\n - Old Growth\n - Nectar\n - Lumber\n - Cherry Blossom\n\n",
      "Science:\n - Teleport\n - Cosmonaut\n - Decipher\n - Integer\n - Policia\n\n",
      "Psychedelic:\n - Groovy\n - Seducer\n - Blush\n - Melancholy\n - Bliss"]

da = ["Grunge:\n - Stroke\n - Glacier\n - Grudge\n - Bloodshed\n - Rotten\n\n",
      "Liquid:\n - Wasteland\n - Amphibian\n - Boundary\n - Threshold\n - Banished\n\n",
      "Brushstroke:\n - Extortion\n - Degeneration\n - Downfall\n - Drench\n - Chemical\n\n",
      "Vintage:\n - Decadence\n - Bravado\n - Funkadelic\n - Boutique\n - Maniac\n\n",
      "Fauna:\n - Growl\n - Scavenger\n - Zebra\n - Blue Tiger\n - Rising Tiger\n\n",
      "Topography:\n - Acidic\n - Gunrunner\n - Forecast\n - Cartographer\n - Sunder\n\n",
      "Infection:\n - Corrosion\n - Entropy\n - Contamination\n - Glitch\n - Conviction"]

readme_header = ["# CW-Camo-Progress\n",
                 "Taskpaper lists for my Cold War camo progress\n",
                 "\n\n",
                 "# Current Progress\n"]


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
    mtotal = 0
    mcomplete = 0
    markdown = ''
    for category in cat:
        mtotal += 1
        catcomplete = 0
        unlocked = "false"
        temp = ''
        for name in eval(category.replace("-", "_"))[0]:
            filename = name.replace(" ", "-") + ".taskpaper"
            filetotal, filecomplete = taskcount(masterycamo + "/" + category + "/" + filename)
            total += filetotal
            complete += filecomplete
            if filecomplete == filetotal:
                catcomplete += 1
                temp += "- [x] " + name + "\n"
            else:
                temp += "- [ ] " + name + "\n"
            if catcomplete >= eval(category.replace("-", "_"))[1][0]:
                unlocked = "true"
        if unlocked == "true":
            mcomplete += 1
            header = "### " + category.replace("-", " ") + " (Unlocked)" + "\n"
        else:
            header = "### " + category.replace("-", " ") + "\n"
        markdown += header + temp
    percent = str(round((complete/total)*100))

    return markdown, percent, str(mtotal), str(mcomplete)


if "-i" in opts:
    print("Initializing Files...")
    for camo in camos:
        os.mkdir(camo)
        for category in cat:
            os.mkdir(camo + "/" + category)
            for gun in eval(category.replace("-", "_"))[0]:
                filename = str(gun).replace(" ", "-")
                tp = open(camo + "/" + category + "/" + filename + ".taskpaper", "x")
                if camo == "DM-Ultra":
                    tp.writelines(dm)
                elif camo == "Dark-Aether":
                    tp.writelines(da)
                tp.close()
    readme = open("README.md", "x")
    readme.writelines(readme_header)
    readme.close()
    print("Done.")

if "-u" in opts:
    print("Updating Files...")
    for camo in camos:
        for category in cat:
            for gun in eval(category.replace("-", "_"))[0]:
                filename = str(gun).replace(" ", "-")
                path = camo + "/" + category + "/" + filename + ".taskpaper"
                if not os.path.exists(path):
                    tp = open(path, "x")
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
        readme.write('## ' + camo.replace("-", " ") + ": " + data[3] + "/" + data[2] + " Categories" + ' ![' + data[1] + '%](https://progress-bar.dev/' + data[1] + '/?width=200)\n')
        readme.write(data[0])
        readme.write('\n\n')
        print(camo.replace("-", " ") + ' Completion: ' + data[1] + '%')
    readme.close()
