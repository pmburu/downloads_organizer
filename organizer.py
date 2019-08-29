import os
from pathlib import Path

'''A dictionary for creating specific subfolders.
In this dictionary, a list of all file extensions in 
all the specific subfolders is reflected.'''

subfolders = {
    'Media': {
        'Images': ['.jpeg', '.jpg', '.png', '.tiff', '.gif'],
        'Videos': ['.mp4', '.mpegav', '.avi', '.flv', '.webm', '.mov'],
        'Audio': ['.mp3', '.m4a'],
    },
    'Photoshop': ['.psd'],
    'Illustrator': ['.ai', '.eps'],
    'Docs': {
        'Word': ['.doc', '.docx'],
        'Excel': ['.xls', '.xlsx'],
        'PPT': ['.ppt', '.pptx'],
        'PDF': ['.pdf'],
    },
    'Plaintext': ['.txt', '.in', '.out'],
    'Databases': ['.sql', '.json'],
    'Executables': ['.dmg'],
    'Archives': ['.zip', '.rar'],
    'Python': ['.py'],
}

formats_in_files = {
    file_format: directory
    for directory, file_formats in subfolders.items()
    for file_format in file_formats
}

# Organizing the items in their respective subfolders using the function below

def organizer():
    for file_folder_entry in os.scandir():
        if file_folder_entry.is_dir():
            continue
    
        file_folder_path = Path(file_folder_entry.name)
        file_format = file_folder_path.suffix.lower()
        if file_format in formats_in_files:
            directory_path = Path(formats_in_files[file_format])
            directory_path.mkdir(exist_ok=True)
            file_folder_path.rename(directory_path.joinpath(file_folder_path))
    
    # If the subfolder formart doesnt exist we create an 'Others' folder for it
    
    try:
        os.mkdir('Other')
    except:
        pass
    
    for dir in os.scandir():
        try:
            if dir.is_dir():
                os.rmdir(dir)
            else:
                os.rename(os.getcwd() + '/' + str(Path(dir)), os.getcwd() + '/Other/' + str(Path(dir)))
        except:
            pass
        
if __name__ == '__main__':
    organizer()


