import re
readme_header = [
    "# CW-Camo-Progress\n", "Taskpaper lists for my Cold War camo progress\n",
    "\n\n", "# Current Progress\n"
]
h2 = re.compile('^(\\W+)?(.*)\\:$', re.MULTILINE)
unchecked = re.compile('^(\\W+)?(-\\W)(.*)$', re.MULTILINE)
done = re.compile('^(\\W+)?(-\\W\\[\\W\\]\\W)(.*)(\\W@done)$', re.MULTILINE)


def tptomarkdown(filename):
    total = 0
    complete = 0
    file = open(filename, "r")
    filelines = file.readlines()
    for line in filelines:
        if "-" in line:
            total += 1
        if "@done" in line:
            complete += 1
    percent = str(round((complete/total)*100))
    filestr = "".join(filelines)
    filestr = h2.sub(r'### \2', filestr)
    filestr = unchecked.sub(r'- [ ] \3', filestr)
    filestr = done.sub(r'- [x] \3', filestr)
    file.close()
    return filestr, percent


dm_ultra = tptomarkdown("DM-Ultra.taskpaper")
dark_aether = tptomarkdown("Dark-Aether.taskpaper")

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
