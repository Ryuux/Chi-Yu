import os
import shutil

def organize_files(directory):
    files = [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]

    # Destination folders for each file type
    destination_folders = {
        '.txt': 'Text Files',
        '.docx': 'Word Documents',
        '.xlsx': 'Excel Documents',
        '.jpg': 'Images',
        '.mp3': 'Audio Files',
        '.mp4': 'Video Files',
        '.zip': 'Compressed Files'
    }

    file_types = set(os.path.splitext(file)[1] for file in files)
    valid_types = file_types.intersection(destination_folders.keys())

    for file_type in valid_types:
        destination_folder = os.path.join(directory, destination_folders[file_type])
        os.makedirs(destination_folder, exist_ok=True)

    for file in files:
        extension = os.path.splitext(file)[1]
        if extension in valid_types:
            source = os.path.join(directory, file)
            destination = os.path.join(directory, destination_folders[extension], file)
            shutil.move(source, destination)

    print('Files organized successfully.')

directory = input('Enter the directory you want to organize: ')
if os.path.isdir(directory):
    organize_files(directory)
    print('File organization completed.')
else:
    print('The specified directory is not valid.')