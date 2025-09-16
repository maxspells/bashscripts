from pathlib import Path

core_dir = Path.home()


def check_directory(directory,targetfile):
    for item in directory.interdir():
        i


for item in core_dir.iterdir():
    if item.is_dir():
        print(item)
