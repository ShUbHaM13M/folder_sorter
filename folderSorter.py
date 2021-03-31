import os
import shutil
import sys

sys.argv
print(sys.argv, len(sys.argv))

def folderSorter(path):
    os.chdir(path)

    for root, dirs, files in os.walk(path):

        try:
            if "Music" and "Videos" and "Archives" and "HTMLs" and "Documents" and "Photos" not in dirs:
                os.mkdir("Music")
                os.mkdir("Archives")
                os.mkdir("HTMLs")
                os.mkdir("Documents")
                os.mkdir("Photos")
                os.mkdir("Videos")
        except FileExistsError:
            pass

        
        for f in files:
            if f.endswith(".mp3"):
                try:
                    shutil.move(f, "./Music")
                except:
                    pass
            elif f.endswith(".zip") or f.endswith(".rar"):
                try:
                    shutil.move(f, "./Archives")
                except:
                    pass
            elif f.endswith(".mov") or f.endswith(".mp4") or f.endswith(".avi") or f.endswith(".mpeg"):
                try: shutil.move(f, "./Videos")
                except: pass
            elif f.endswith(".jpeg") or f.endswith(".png") or f.endswith("jpg"):
                try: shutil.move(f, "./Photos")
                except: pass
            elif f.endswith(".html") or f.endswith(".css") or f.endswith(".js"):
                try: shutil.move(f, "HTMLs")
                except: pass
            elif f.endswith(".txt") or f.endswith(".docx") or f.endswith(".pdf"):
            	try: shutil.move(f, "./Documents")
            	except: pass

if len(sys.argv) > 1:
	path = ''.join(sys.argv[1:])
else:
	path = os.path.abspath(os.getcwd())

folderSorter(path)