# -*-coding:Latin-1 -*
import random
import os 
import subprocess
import sys , getopt
from os import listdir
from os.path import isfile, join
# utilisation python scripthandbrakev2.py "chemin de fichier" 
# le script va faire un listing des fichier dans le dossier et va convertir les video en x265 
# https://handbrake.fr/docs/en/latest/cli/cli-guide.html
def main(argv):
	handbrakecli = "HandbrakeCLI.exe"
#	option = " -f mkv -P -e x265 -q 20 -B 160"
	option = " -f mkv -P -e x265 -q 21 -E copy"
	inputfile = sys.argv[1]
	print 'nombre argument', len(sys.argv)
	if len(sys.argv) > 2:
		outputfile = sys.argv[2]
	else:
		outputfile = inputfile


	onlyfiles = [f for f in listdir(inputfile) if isfile(join(inputfile, f))]
	print 'liste de fichiers', onlyfiles
	for f in onlyfiles:
		comandein =   inputfile + '\\' + f 
		comandeout =   outputfile + '\\' + f + '.mkv' 
		commandeligne = handbrakecli + " -i " + comandein + " -o " + comandeout + option
		#subprocess.Popen lance les X commande ou a utiliser sur cluster ou cpu avec beaucoup de coeur
		#subprocess.Popen(commandeligne)
		proc = subprocess.Popen(commandeligne)
		proc.wait()
		print 'un fichier terminer'
	print 'terminer'
if __name__ == "__main__":
    main(sys.argv)

#os.system("pause")

