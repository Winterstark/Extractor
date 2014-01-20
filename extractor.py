#set your 7-Zip exe path here::
SZIP = ""

#if the archive contains at least this many files or
#folders then extract them into a new folder::
NEW_DIR_LIMIT = 5


import sys
import subprocess
import shutil
import os
import glob
from win32com.shell import shell, shellcon


path = sys.argv[1]

parent_dir = os.path.dirname(path)
new_dir = parent_dir + "\\!extracted - " + os.path.splitext(os.path.basename(path))[0]

subprocess.call([SZIP, "x", path, "-o" + new_dir])

files = os.listdir(new_dir)

if len(files) < NEW_DIR_LIMIT:
    for src_dir, dirs, files in os.walk(new_dir):
        dst_dir = src_dir.replace(new_dir, parent_dir)
        if not os.path.exists(dst_dir):
            os.mkdir(dst_dir)
        for file_ in files:
            src_file = os.path.join(src_dir, file_)
            dst_file = os.path.join(dst_dir, file_)
            if os.path.exists(dst_file):
                os.remove(dst_file)
            shutil.move(src_file, dst_dir)

    #delete new dir
    shutil.rmtree(new_dir)

#send archive to bin
shell.SHFileOperation((0, shellcon.FO_DELETE, path, None, shellcon.FOF_ALLOWUNDO | shellcon.FOF_NOCONFIRMATION, None, None))

#check if archive has multiple files; delete them too
if ".rar" in path:
    for file in glob.glob(path.replace(".rar", ".r*")):
        shell.SHFileOperation((0, shellcon.FO_DELETE, file, None, shellcon.FOF_ALLOWUNDO | shellcon.FOF_NOCONFIRMATION, None, None))
