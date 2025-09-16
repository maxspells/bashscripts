import platform
from pathlib import Path
from shutil import move


os = platform.system()


def get_home_directory():
    if os == "Windows":
        print("it be windows lol")  # TODO adding windows support later maybe
    elif os == "Linux":
        return Path.home()
    elif os == "Darwin":
        print("It be macOS")  # TODO adding mac support later maybe
    else:
        print("Unknown system")
        return "Unknown"


def get_downloads_directory():
    """Returns the directory of the downloads folder"""
    downloads_path = get_home_directory() / "Downloads"
    if downloads_path.exists():
        return downloads_path
    else:
        print("No Downloads directory found!")


def sort_file(file):
    targ = get_target_directory(file)
    if targ is not None:
        check_dir(file)
        filepath = home / targ / str(file.name)
        print(f"Moving {file.name} to {filepath}")
        move(file, filepath)


def check_dir(file):
    """Checks if the target directory exists,
    if it doesn't, it will create it"""
    tar_dir = str(get_target_directory(file))
    dirpath = home / tar_dir
    if not dirpath.exists():
        print(f"{tar_dir} not found, creating {dirpath}")
        dirpath.mkdir()


def get_category(file):
    suffix = file.suffix.lower()
    for category, suffix_list in file_categories.items():
        if suffix in suffix_list:
            return category
    return "unknown"


# TODO Make this a switch prolly
# TODO and uh failsafe for other os other than Linux
def get_target_directory(file):
    if get_category(file) == "archives":
        return "Archives"
    if get_category(file) == "documents":
        return "Documents"
    if get_category(file) == "executables":
        return "Executables"
    if get_category(file) == "images":
        return "Pictures"
    if get_category(file) == "videos":
        return "Videos"
    if get_category(file) == "audio":
        return "Music"
    if get_category(file) == "fonts":
        return "Fonts"
    if get_category(file) == "code":
        return "Code"
    if get_category(file) == "temp":
        return "temp"


def main():
    if home != "Unknown":  # If something fails and the home folder isn't
        # identified, nothing happens
        for file in downloads.iterdir():
            if file.is_file():  # and not a directory
                sort_file(file)


file_categories = {
    "archives": [
        ".zip",
        ".rar",
        ".7z",
        ".tar",
        ".tar.gz",
        ".tgz",
        ".xz",
        ".bz2",
        ".gz",
        ".deb",
        ".rpm",
        ".iso",
    ],
    "documents": [
        ".txt",
        ".md",
        ".rtf",
        ".pdf",
        ".doc",
        ".docx",
        ".xls",
        ".xlsx",
        ".ppt",
        ".pptx",
        ".odt",
        ".ods",
        ".json",
        ".jsonc",
        ".xml",
        ".yaml",
        ".yml",
        ".html",
        ".css",
        ".js",
        ".py",
        ".java",
        ".c",
        ".cpp",
    ],
    "executables": [".exe", ".msi", ".dmg", ".pkg", ".app", ".AppImage", ".bin", ".sh"],
    "images": [
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".bmp",
        ".tiff",
        ".svg",
        ".webp",
        ".heic",
    ],
    "videos": [
        ".mp4",
        ".mkv",
        ".mov",
        ".avi",
        ".wmv",
        ".flv",
        ".webm",
        ".mpeg",
        ".mpg",
    ],
    "audio": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a", ".wma"],
    "fonts": [".ttf", ".otf", ".woff", ".woff2"],
    "code": [
        ".py",
        ".java",
        ".js",
        ".ts",
        ".c",
        ".cpp",
        ".h",
        ".cs",
        ".go",
        ".rb",
        ".php",
        ".sh",
        ".bat",
    ],
    "temp": [".tmp", ".log", ".bak", ".crdownload", ".part"],
}

home = get_home_directory()
target_dirs = {  # TODO these aren't implemented at all yet uh implement them
    "Archives": {"Linux": home / "Archives"},
    "Documents": {"Linux": home / "Documents"},
    "Executables": {"Linux": home / "Executables"},
    "Pictures": {"Linux": home / "Pictures"},
    "Videos": {"Linux": home / "Videos"},
    "Music": {"Linux": home / "Music"},
    "Fonts": {"Linux": home / "Fonts"},
    "Code": {"Linux": home / "code"},
    "temp": {"Linux": home / "temp"},
}

downloads = get_downloads_directory()
main()
