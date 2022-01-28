#!/bin/env python3
import sys
import os

opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
camos = [
    "Atomic",
    "Dark-Aether"
]

cat = [
    "Assault-Rifles",
    "SMGs",
    "Shotguns",
    "LMGs",
    "Marksman-Rifles",
    "Sniper-Rifles",
    "Handguns",
    "Launchers",
    "Melee"
]
half_camo = ["Launchers", "Melee"]

Assault_Rifles = [["STG44", "Automaton", "Itra Burst", "BAR", "AS44", "NZ-41", "Volkssturmgewehr", "Cooper Carbine"], [7]]
SMGs = [["MP-40", "Sten", "M1928", "Owen Gun", "Type 100", "PPSh-41", "Welgun"], [6]]
Shotguns = [["Einhorn Revolving", "Combat Shotgun", "Gracy Auto", "Double Barrel"], [4]]
LMGs = [["MG42", "DP27", "Type 11", "Bren"], [4]]
Marksman_Rifles = [["M1 Garand", "SVT-40", "G-43"], [3]]
Sniper_Rifles = [["Type 99", "3-Line Rifle", "Kar98k", "Gorenko Anti-Tank Rifle"], [3]]
Handguns = [["Ratt", "Top Break", "1911", "Klauser", "Machine Pistol"], [5]]
Launchers = [["M1 Bazooka", "Panzerschreck", "Panzerfaust", "MK11 Launcher"], [4]]
Melee = [["Combat Shield", "FS Fighting Knife", "Katana", "Sawtooth"], [2]]

Atomic =   ["Pack Tactics:\n\t- The Depths\n\t- Osprey\n\t- Tributaries\n\t- Candybar\n\t- Reptilian\n\t- Snakebit\n\t- Low Foliage\n\t- Sandspout\n\t- Winter's Blood\n\t- Brackish\n\n",
            "Surgical:\n\t- Wild Wood\n\t- Drought\n\t- Flashbang\n\t- Bitter Cold\n\t- Riverdog\n\t- Rustbelt\n\t- Fungus\n\t- Termite\n\t- Quarry\n\t- Selva\n\n",
            "Predatory Ambition:\n\t- Charter\n\t- Heatwave\n\t- Dead Ivy\n\t- Creek\n\t- Abstract\n\t- Moss\n\t- Seedspitter\n\t- Landlocked\n\t- Mistmaker\n\t- Sunsetter\n\n",
            "Reptilian:\n\t- Slow Crawl\n\t- Verdant\n\t- Swarmer\n\t- Chlorine\n\t- Stoplight\n\t- Eroded\n\t- Bedrock\n\t- Dark Scale\n\t- Ironrot\n\t- Dormant\n\n",
            "Deadeye:\n\t- Mosaic\n\t- Speckled Green\n\t- Metro\n\t- Frozen Glass\n\t- Red Ruin\n\t- Drivepoint\n\t- Desert Tree\n\t- Autumn\n\t- Embersmoke\n\t- Verdure\n\n",
            "Berserker:\n\t- Gamma Frog\n\t- Crypsis\n\t- Arid\n\t- Hole Digger\n\t- Takeover\n\t- Overhang\n\t- Emergent Layer\n\t- Cold Plunge\n\t- Polluted\n\t- Phantasmal\n\n",
            "Wildcat:\n\t- Bosk\n\t- Iceburg\n\t- Papertrail\n\t- Blood Pact\n\t- Stratoshpere\n\t- Gamehunter\n\t- Snowcat\n\t- Cheetah\n\t- Exotic Killer\n\t- Fashonista\n\n",
            "Survivalist:\n\t- Bloom\n\t- Lotus\n\t- Fern\n\t- Flowerbed\n\t- Greenthumb\n\t- Topiaries\n\t- New Leaf\n\t- Chlorophyll\n\t- Harvester\n\t- Blue Palm\n\n",
            "Mindgames:\n\t- Scarlet Skull\n\t- Head Collecter\n\t- Night Terrors\n\t- Delirium\n\t- Death Envy\n\t- Ancient Winds\n\t- Fire Haze\n\t- Chocolate Thunder\n\t- Mount Olympus\n\t- Hyperlapse\n\n",
            "Death Artist:\n\t- Smelter\n\t- Metallurgy\n\t- Whirlpool\n\t- Shifting Sands\n\t- Melted\n\t- Expressionist\n\t- Vulpes\n\t- Archeologist\n\t- Cabana\n\t- Bloodspatter"]

Dark_Aether =  ["Pack Tactics:\n\t- Cyanide\n\t- Invertebrate\n\t- Magma\n\t- Deluge\n\t- Macroscopic\n\t- Eggplant\n\t- Coagulation\n\t- Contamination\n\t- Saffron Grime\n\t- Hydroshere\n\n", 
                "Surgical:\n\t- Mildew\n\t- Substratum\n\t- Oxidized\n\t- Atrophy\n\t- Infestation\n\t- Anaglyph\n\t- Erosion\n\t- Abrasion\n\t- Molecular\n\t- Putrescence\n\n", 
                "Predatory Ambition:\n\t- Grayscale\n\t- Cold Front\n\t- Sulfuric\n\t- Irresolute\n\t- Inclement\n\t- Tallow\n\t- Forlorn\n\t- Hybernation\n\t- Mirage\n\t- Ablution\n\n", 
                "Reptilian:\n\t- Terrapin\n\t- Kinixys\n\t- Mutant\n\t- Rubriventris\n\t- Sycophantic\n\t- Pit Viper\n\t- Blue Racer\n\t- Leucistic\n\t- Virulence\n\t- Halftone\n\n", 
                "Deadeye:\n\t- Disintegration\n\t- Fracture\n\t- Penny\n\t- Armorial\n\t- Cathedral\n\t- Millstone\n\t- Corpuscle\n\t- Glaucous\n\t- Obtruder\n\t- Hemoglobin\n\n", 
                "Berserker:\n\t- Burrow\n\t- Arboreal\n\t- Amphibian\n\t- Atramentous\n\t- Aposematic\n\t- Wenge Bog\n\t- Marshland\n\t- Malignant\n\t- Amethyst\n\t- Intestinal\n\n", 
                "Wildcat:\n\t- Thicket\n\t- Rosewood\n\t- Timberwolf\n\t- Nocturnal\n\t- Sovereign\n\t- Lynx\n\t- Hunter\n\t- Azure\n\t- Chartreuse\n\t- Mauvelous\n\n", 
                "Survivalist:\n\t- Rosary\n\t- Bracken\n\t- Anemone\n\t- Oleander\n\t- Coreopsis\n\t- Kallima\n\t- Umbrage\n\t- Gloom\n\t- Unearthly\n\t- Monstera\n\n", 
                "Mindgames:\n\t- Reckon\n\t- Cranial\n\t- Reverie\n\t- Think Tank\n\t- Torment\n\t- Dust Bowl\n\t- Nimbus\n\t- Smog\n\t- Cantankerous\n\t- Stratus\n\n", 
                "Death Artist:\n\t- Pernicious\n\t- Iridescent\n\t- Aurum\n\t- Transfusion\n\t- Immiscible\n\t- Stigma\n\t- Blot\n\t- Imprint\n\t- Monsoon\n\t- Lambent"]

readme_header = ["# CoD-Camo-Progress\n",
                 "Taskpaper lists for my Vanguard camo progress\n",
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

def main():
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
                        if category in half_camo:
                            tp.writelines(eval(camo.replace("-", "_"))[0:5])
                        else:
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

if __name__ == '__main__':
    main()
