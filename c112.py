import os
import shutil

def organize_documents(downloads_path, to_dir, allowed_extensions):
    # List all files in the Downloads folder
    files = os.listdir(downloads_path)

    for file_name in files:
        # Get the file extension
        _, extension = os.path.splitext(file_name)

        # Check if the extension is blank or not in the allowed extensions list
        if not extension or extension.lower() not in allowed_extensions:
            continue

        # Create source and destination paths
        path1 = os.path.join(downloads_path, file_name)
        path2 = os.path.join(to_dir, "Document_Files")
        path3 = os.path.join(path2, file_name)

        # Check if the destination folder exists
        if os.path.exists(path2):
            print(f"Moving {file_name} to {path2}")
            shutil.move(path1, path3)
        else:
            # Create the destination folder
            os.makedirs(path2)
            print(f"Moving {file_name} to {path2}")
            shutil.move(path1, path3)

if __name__ == "__main__":
    # Specify the path to the "Downloads" folder
    downloads_path = "C:\Users\anish\Downloads"

    # Specify the path where the "Document_Files" folder will be created
    to_dir = "C:\Users\anish\Documents"

    # Specify the allowed document extensions
    allowed_extensions = ['.txt', '.doc', '.docx', '.pdf']

    # Organize the documents
    organize_documents(downloads_path, to_dir, allowed_extensions)
