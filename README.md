# scripthandbrake
this is a litle python script who check the folder and list file then use handbrakeCLI to convert all video in x265.

use
on windows (in the folder that contain handbrakeCLI.exe and scripthandbrakev2.py)
python scripthandbrakev2.py "path\directory"
(be careful windows don't allow space in path or file)

if you want to change filename use
python scripthandbrakev2.py "path\directory" "newFilename"

if you want to change filename and directory use
python scripthandbrakev2.py "path\directory" "newFilename" "path\otherdirectory"

on linux and probably macos
python ./scripthandbrakev2-linux.py path/directory

the file scripthanbrakev2.py must be in the directory where HandbrakeCLI is (only for windows), else it will not run 
it work on windows and linux (ubuntu) with python 2.7
