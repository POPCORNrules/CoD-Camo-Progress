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
    filelines[0] = h2.sub(
        r'## \2 ![' + percent + '%](https://progress-bar.dev/' + percent + '/?s&width=200&color=babaca)', filelines[0])
    filestr = "".join(filelines)
    filestr = h2.sub(r'### \2', filestr)
    filestr = unchecked.sub(r'- [ ] \3', filestr)
    filestr = done.sub(r'- [x] \3', filestr)
    file.close()
    return filestr


dm_ultra = tptomarkdown("DM-Ultra.taskpaper")
dark_aether = tptomarkdown("Dark-Aether.taskpaper")

readme = open("README.md", "w")
readme.writelines(readme_header)
readme.close()
readme = open("README.md", "a")
readme.write(dm_ultra)
readme.write('\n\n\n')
readme.write(dark_aether)
readme.close()
