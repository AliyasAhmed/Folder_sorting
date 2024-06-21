import os
import shutil

def folder_sorting(folder_path):
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            file_extension = os.path.splitext(filename)[1].lower()
            if file_extension:
                destination_folder = os.path.join(folder_path, file_extension[1:].upper())
                os.makedirs(destination_folder, exist_ok= True)
                shutil.move(os.path.join(folder_path, filename), os.path.join(destination_folder, filename))
if __name__=="__main__":
    folder_path = input("Enter the folder path\n")
    folder_sorting(folder_path)
