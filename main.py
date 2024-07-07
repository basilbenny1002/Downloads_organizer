
# This script organizes files in the user's download folder by moving them into categorized subdirectories based on their file extensions.
#imports necessary libraries
import os
import shutil
import pathlib

# Define lists of file extensions for various file types
# These will be used to categorize files in the download folder
# Image file extensions
images = ["jpg", "jpeg", "png", "gif", "bmp", "tiff", "webp", "svg", "ico", "heic", "raw", "psd"]

# Video file extensions
videos = ["mp4", "avi", "mov", "wmv", "flv", "mkv", "webm", "m4v", "mpeg", "mpg", "3gp"]

# Audio file extensions
audio = ["mp3", "wav", "ogg", "flac", "aac", "wma", "m4a", "aiff", "alac"]

# Document file extensions
documents = ["pdf", "doc", "docx", "txt", "rtf", "odt", "tex", "ppt", "pptx", "xls", "xlsx", "csv", "md", "epub"]

# Executable file extensions
executables = ["exe", "msi", "bat", "sh", "app", "com", "cmd", "vbs", "deb", "rpm"]

# Compressed file extensions
compressed = ["zip", "rar", "7z", "tar", "gz", "bz2", "xz", "tgz"]

# Source code file extensions
source_code = ["py", "java", "cpp", "c", "h", "js", "html", "css", "php", "rb", "swift", "go", "rs", "ts"]

# Database file extensions
databases = ["sql", "db", "sqlite", "mdb", "accdb", "dbf"]

# Font file extensions
fonts = ["ttf", "otf", "woff", "woff2", "eot"]

# 3D model file extensions
models_3d = ["obj", "fbx", "stl", "blend", "3ds", "dae"]

# Vector graphics file extensions
vector_graphics = ["ai", "eps", "cdr"]

# Backup file extensions
backups = ["bak", "old", "backup"]


USER_NAME = os.getlogin() #Get username of the user
# Define paths for the source (downloads) and destination folders
# Each file type will have its own destination folder
downloads_path = fr"C:\users\{USER_NAME}\downloads"
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
VECTOR_GRAPHICS_PATH =  os.path.join(downloads_path, "Vector Graphics")
BACKUPS_PATH =  os.path.join(downloads_path, "Backups")

def create_dir(path:str):
    global dirc
    """
    Makes a directory with the passed in parameter
    :param path:
    :return:
    """
    try:
        os.makedirs(path)
    except Exception as e:
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
        except Exception as r:
            pass
# Iterate through all items in the downloads folder
for files in os.listdir(downloads_path):
    joined_path = os.path.join(downloads_path, files) #Joins the downloads path and the file name
    extention = str(pathlib.Path(joined_path).suffix).replace('.', '') #Gets the extention of the file
    if os.path.isfile(path=os.path.join(downloads_path, files)): #Checks if the path is of a file or a directory
        #Check if the extention is present in any of included extentions and moves the file to teh appropriate location
        if extention in images:
            move_files(joined_path, IMAGES_PATH)
        elif extention in videos:
            move_files(joined_path, VIDEOS_PATH)
        elif extention in documents:
            move_files(joined_path, DOCUMENTS_PATH)
        elif extention in audio:
            move_files(joined_path, AUDIO_PATH)
        elif extention in compressed:
            move_files(joined_path, COMPRESSED_PATH)
        elif extention in executables:
            move_files(joined_path, EXECUTABLES_PATH)
        elif extention in source_code:
            move_files(joined_path, CODE_PATH)
        elif extention in models_3d:
            move_files(joined_path, MODELS_PATH)
        elif extention in backups:
            move_files(joined_path, BACKUPS_PATH)
        elif extention in vector_graphics:
            move_files(joined_path, VECTOR_GRAPHICS_PATH)
        elif extention in databases:
            move_files(joined_path, DATABASES_PATH)
        elif extention in fonts:
            move_files(joined_path, FONTS_PATH)


