# -*-coding:Latin-1 -*
import random
import os 
import subprocess
import sys , getopt
from os import listdir
from os.path import isfile, join
# utilisation python scripthandbrakev2.py "chemin de fichier" 
# le script va faire un listing des fichier dans le dossier et va convertir les video en x265

#ATTENTION il ne faut pas d'espace dans le chemin vers les fichier n'y dans les fichier, nulle part

# https://handbrake.fr/docs/en/latest/cli/cli-guide.html
def main(argv):
	handbrakecli = "HandbrakeCLI.exe"
#	option = " -f mkv -P -e x265 -q 20 -B 160"
	option = " -f mkv -P -e x265 -q 21 -E copy"
	inputfile = sys.argv[1]
	print 'nombre argument', len(sys.argv)
	outputfile = inputfile
	nouveauNom = ''
	if len(sys.argv) > 3:
		outputfile = sys.argv[3]
	elif len(sys.argv) > 2:
		nouveauNom = sys.argv[2]

	indice = 1
	onlyfiles = [f for f in listdir(inputfile) if isfile(join(inputfile, f))]
	print 'liste de fichiers', onlyfiles
	for f in onlyfiles:
		comandein =   inputfile + '\\' + f
		#test si nouveauNom
		if len(nouveauNom) == 0: 
			comandeout =   outputfile + '\\' + f + '.mkv'
		else:
			comandeout =   outputfile + '\\' + nouveauNom + '_' + str(indice) + '.mkv'
		commandeligne = handbrakecli + " -i " + comandein + " -o " + comandeout + option
		#subprocess.Popen lance les X commande ou a utiliser sur cluster ou cpu avec beaucoup de coeur
		#subprocess.Popen(commandeligne)
		proc = subprocess.Popen(commandeligne)
		proc.wait()
		indice +=1
		#pas de i++ en python
		print 'un fichier terminer'
	print 'terminer'
if __name__ == "__main__":
    main(sys.argv)

#os.system("pause")
