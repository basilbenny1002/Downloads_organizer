# This script organizes files in the user's download folder by moving them into categorized subdirectories based on their file extensions.
# imports necessary libraries
import os
import shutil
import pathlib

# Extentions dictionary(faster than previous version using multiple lists)
file_extensions = {
    #Image 
    "jpg": "images",
    "jpeg": "images",
    "png": "images",
    "gif": "images",
    "bmp": "images",
    "tiff": "images",
    "webp": "images",
    "svg": "images",
    "ico": "images",
    "heic": "images",
    "raw": "images",
    "psd": "images",
    #Videos
    "mp4": "videos",
    "avi": "videos",
    "mov": "videos",
    "wmv": "videos",
    "flv": "videos",
    "mkv": "videos",
    "webm": "videos",
    "m4v": "videos",
    "mpeg": "videos",
    "mpg": "videos",
    "3gp": "videos",
    #Audio
    "mp3": "audio",
    "wav": "audio",
    "ogg": "audio",
    "flac": "audio",
    "aac": "audio",
    "wma": "audio",
    "m4a": "audio",
    "aiff": "audio",
    "alac": "audio",
    #Documents
    "pdf": "documents",
    "doc": "documents",
    "docx": "documents",
    "txt": "documents",
    "rtf": "documents",
    "odt": "documents",
    "tex": "documents",
    "ppt": "documents",
    "pptx": "documents",
    "xls": "documents",
    "xlsx": "documents",
    "csv": "documents",
    "md": "documents",
    "epub": "documents",
    #Executables
    "exe": "executables",
    "msi": "executables",
    "bat": "executables",
    "sh": "executables",
    "app": "executables",
    "com": "executables",
    "cmd": "executables",
    "vbs": "executables",
    "deb": "executables",
    "rpm": "executables",
    #Compressed
    "zip": "compressed",
    "rar": "compressed",
    "7z": "compressed",
    "tar": "compressed",
    "gz": "compressed",
    "bz2": "compressed",
    "xz": "compressed",
    "tgz": "compressed",
    #Source Code
    "py": "source_code",
    "java": "source_code",
    "cpp": "source_code",
    "c": "source_code",
    "h": "source_code",
    "js": "source_code",
    "html": "source_code",
    "css": "source_code",
    "php": "source_code",
    "rb": "source_code",
    "swift": "source_code",
    "go": "source_code",
    "rs": "source_code",
    "ts": "source_code",
    #Databases
    "sql": "databases",
    "db": "databases",
    "sqlite": "databases",
    "mdb": "databases",
    "accdb": "databases",
    "dbf": "databases",
    #Fonts
    "ttf": "fonts",
    "otf": "fonts",
    "woff": "fonts",
    "woff2": "fonts",
    "eot": "fonts",
    #3D Models
    "obj": "models_3d",
    "fbx": "models_3d",
    "stl": "models_3d",
    "blend": "models_3d",
    "3ds": "models_3d",
    "dae": "models_3d",
    #Vector Graphics
    "ai": "vector_graphics",
    "eps": "vector_graphics",
    "cdr": "vector_graphics",
    #Backups
    "bak": "backups",
    "old": "backups",
    "backup": "backups"
}

# Define paths for the source (downloads) and destination folders
# Each file type will have its own destination folder
downloads_path = os.path.expanduser("~/Downloads")
IMAGES_PATH = os.path.join(downloads_path, "Images")
VIDEOS_PATH = os.path.join(downloads_path, "Videos")
AUDIO_PATH = os.path.join(downloads_path, "Audio")
EXECUTABLES_PATH = os.path.join(downloads_path, "Executables")
COMPRESSED_PATH = os.path.join(downloads_path, "Compressed")
DOCUMENTS_PATH = os.path.join(downloads_path, "Documents")
CODE_PATH = os.path.join(downloads_path, "Code")
DATABASES_PATH = os.path.join(downloads_path, "Databases")
FONTS_PATH = os.path.join(downloads_path, "Fonts")
MODELS_PATH = os.path.join(downloads_path, "3D Models")
VECTOR_GRAPHICS_PATH = os.path.join(downloads_path, "Vector Graphics")
BACKUPS_PATH = os.path.join(downloads_path, "Backups")

#A dictionary containing key value as the file type and data value as the path to where the file needs to be moved to
path_dictionary = {"images": IMAGES_PATH, "videos": VIDEOS_PATH, "audio": AUDIO_PATH, "documents": DOCUMENTS_PATH,
                   "executables": EXECUTABLES_PATH, "compressed": COMPRESSED_PATH, "source_code": CODE_PATH,
                   "databases": DATABASES_PATH, "fonts": FONTS_PATH, "models_3d": MODELS_PATH,
                   "vector_graphics": VECTOR_GRAPHICS_PATH, "backups": BACKUPS_PATH}


def create_dir(path: str):
    """
    Makes a directory with the passed in parameter
    :param path:
    :return:
    """
    try:
        os.makedirs(path)
    except :
        pass


def move_files(source_path: str, destination_path: str):
    """
    Moves a file from the source path to destination path and creates a directory if destination path doesn't exist
    :param source_path:
    :param destination_path:
    :return:
    """
    try:
        shutil.move(source_path, destination_path)
    except FileNotFoundError:
        create_dir(destination_path)
        try:
            shutil.move(source_path, destination_path)
        except:
            pass


# Iterate through all items in the downloads folder
for files in os.listdir(downloads_path):
    joined_path = os.path.join(downloads_path, files)  # Joins the downloads path and the file name
    extension = str(pathlib.Path(joined_path).suffix).replace('.', '')  # Gets the extension of the file
    if os.path.isfile(path=os.path.join(downloads_path, files)):  # Checks if the path is of a file or a directory
        try:
            move_files(joined_path, path_dictionary[file_extensions[extension]]) #Moves the file to the directory obtained from path_dictionary and file_extentions dictionary
        except:
            pass
