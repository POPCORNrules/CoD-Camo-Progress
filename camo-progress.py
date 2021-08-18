#!/bin/env python3
import sys
import os

opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
camos = [
    "DM-Ultra",
    "Dark-Aether"
]

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

Assault_Rifles = [["XM4", "AK-47", "Krig 6", "QBZ-83", "FFAR 1", "Groza", "FARA 83", "C58", "EM2"], [5]]
Pistols = [["1911", "Magnum", "Diamatti", "AMP63"], [3]]
Launchers = [["Cigma-2", "RPG-7"], [2]]
LMGs = [["Stoner 63", "RPD", "M60", "MG 82"], [3]]
Melee = [["Knife", "Sledgehammer", "Wakizashi", "E-Tool", "Machete", "Baseball Bat", "Mace", "Cane"], [1]]
Shotguns = [["Hauer-77", "Gallo SA12", "Streetsweeper"], [2]]
SMGs = [["MP5", "Milano 821", "AK-74u", "KSP 45", "Bullfrog", "MAC-10", "LC10", "PPSh-41", "OTs 9", "TEC-9"], [5]]
Sniper_Rifles = [["Pellington 703", "LW3-Tundra", "M82", "ZRG 20mm", "Swiss K31"], [3]]
Special = [["M79", "R1 Shadowhunter", "Ballistic Knife", "Nail Gun"], [1]]
Tactical_Rifles = [["Type 63", "M16", "AUG", "DMR 14", "CARV.2"], [4]]

DM_Ultra = ["Spray:\n\t- Shards\n\t- Ambush\n\t- Frozen Lake\n\t- Debris\n\t- Prosper\n\n",
            "Stripes:\n\t- Gravel\n\t- Graze\n\t- Frost\n\t- Thrash\n\t- Bengal\n\n",
            "Classic:\n\t- Platoon\n\t- Ash\n\t- Checkpoint\n\t- Coercion\n\t- Ransom\n\n",
            "Geometric:\n\t- Blockade\n\t- Warsaw\n\t- Transform\n\t- Fraction\n\t- Bloodline\n\n",
            "Flora:\n\t- Frith\n\t- Old Growth\n\t- Nectar\n\t- Lumber\n\t- Cherry Blossom\n\n",
            "Science:\n\t- Teleport\n\t- Cosmonaut\n\t- Decipher\n\t- Integer\n\t- Policia\n\n",
            "Psychedelic:\n\t- Groovy\n\t- Seducer\n\t- Blush\n\t- Melancholy\n\t- Bliss"]

Dark_Aether = ["Grunge:\n\t- Stroke\n\t- Glacier\n\t- Grudge\n\t- Bloodshed\n\t- Rotten\n\n",
               "Liquid:\n\t- Wasteland\n\t- Amphibian\n\t- Boundary\n\t- Threshold\n\t- Banished\n\n",
               "Brushstroke:\n\t- Extortion\n\t- Degeneration\n\t- Downfall\n\t- Drench\n\t- Chemical\n\n",
               "Vintage:\n\t- Decadence\n\t- Bravado\n\t- Funkadelic\n\t- Boutique\n\t- Maniac\n\n",
               "Fauna:\n\t- Growl\n\t- Scavenger\n\t- Zebra\n\t- Blue Tiger\n\t- Rising Tiger\n\n",
               "Topography:\n\t- Acidic\n\t- Gunrunner\n\t- Forecast\n\t- Cartographer\n\t- Sunder\n\n",
               "Infection:\n\t- Corrosion\n\t- Entropy\n\t- Contamination\n\t- Glitch\n\t- Conviction"]

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

if "-u" in opts:
    print("Updating Files...")
    for camo in camos:
        if not os.path.exists(camo):
            print("Creating " + camo + "/")
            os.mkdir(camo)
        for category in cat:
            if not os.path.exists(camo + "/" + category):
                print("Creating " + camo + "/" + category + "/")
                os.mkdir(camo + "/" + category)
            for gun in eval(category.replace("-", "_"))[0]:
                filename = str(gun).replace(" ", "-")
                name = camo + "/" + category + "/" + filename + ".taskpaper"
                if not os.path.exists(name):
                    print("Creating " + name)
                    tp = open(name, "x")
                    tp.writelines(eval(camo.replace("-", "_")))
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
