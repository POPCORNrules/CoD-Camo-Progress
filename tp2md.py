import re
readme_header = [
	"# CW-Camo-Progress\n", "Taskpaper lists for my Cold War camo progress\n",
	"\n\n", "# Current Progress\n"
]
h2 = re.compile('(^\\W+)?(.*):')
unchecked = re.compile('(\\W+)?(-\\W)(.*)')
done = re.compile('(\\W+)?(-\\W\[\\W\]\\W)(.*)(\\W@done)')


def tptomarkdown(filename):
	file = open(filename, "r")
	filelines = file.readlines()
	filelines[0] = h2.sub(r'## \2', filelines[0])
	filestr = "".join(filelines)
	filestr = h2.sub(r'### \2', filestr)
	filestr = unchecked.sub(r'\n- [ ] \3', filestr)
	filestr = done.sub(r'\n- [x] \3', filestr)
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

