import os
import shutil


def folder_sorting(folder_path, final_destination):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()
            if file_extension:
                # Create the subfolder in the final destination based on file extension
                destination_subfolder = os.path.join(final_destination, file_extension[1:].upper())
                os.makedirs(destination_subfolder, exist_ok=True)
                
                # Move the file directly to the subfolder in the final destination
                shutil.move(file_path, os.path.join(destination_subfolder, filename))
            else:
                # Handle files without extensions if necessary
                pass

if __name__ == "__main__":
    folder_path = input("Enter the path where the files are\n")
    final_destination = input("Enter the path for the final destination: ")
    folder_sorting(folder_path, final_destination)

