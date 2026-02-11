import os
import shutil
from datetime import datetime


DRY_RUN = True

base_folder = "/Users/adityasharma/file_organize"
python_files = "/Users/adityasharma/file_organize/Python_files"
documents = "/Users/adityasharma/file_organize/Documents"
pictures = "/Users/adityasharma/file_organize/Pictures"
others = "/Users/adityasharma/file_organize/Others"

LOG_FILE = os.path.join(base_folder, "organizer_log.txt")

if not os.path.exists(python_files):
    os.makedirs(python_files)
    print("python_files are created sucessfully!")

if not os.path.exists(documents):
    os.makedirs(documents)
    print("documets folder are created sucessfully!")

if not os.path.exists(pictures):
    os.makedirs(pictures)
    print("pictures folder are created sucessfully!")

if not os.path.exists(others):
    os.makedirs(others)
    print("others folder are created sucessfully!")

else:
    print("folders already exist")


for root , dirc, files in os.walk(base_folder):

    if root.startswith(python_files) or \
       root.startswith(documents) or \
       root.startswith(pictures) or \
       root.startswith(others):
        continue

    for file in files:
        full_path = os.path.join(root,file)

        if file == "organizer_log.txt":
         continue
    
        if file.endswith(".py"):
            python_path = os.path.join(python_files,file)
        
            if DRY_RUN:
                print("[DRY RUN] would move",file,"->",python_path)
            else:

                shutil.move(full_path,python_path)

                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                message = f"{current_time} | Moved {file} -> {python_path}"
                print(message)

                with open(LOG_FILE, "a") as log:
                    log.write(message + "\n")

        elif file.endswith(".docx"):        
            documents_path = os.path.join(documents,file)

            if DRY_RUN:
                print("[DRY RUN] would move",file,"->",documents_path)
            else:
                shutil.move(full_path,documents_path) 

                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")                
                message = f"{current_time} | Moved {file} -> {documents_path}"
                print(message)

                with open(LOG_FILE, "a") as log:
                    log.write(message + "\n")

        elif file.endswith(".jpg"):        
            pictures_path = os.path.join(pictures,file)

            if DRY_RUN:
                print("[DRY RUN] would move",file,"->",pictures_path)
            else:
                shutil.move(full_path,pictures_path)

                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                message = f"{current_time} | Moved {file} -> {pictures_path}"
                print(message)

                with open(LOG_FILE, "a") as log:
                    log.write(message + "\n")

        else:        
            others_path = os.path.join(others,file)

            if DRY_RUN:
                print("[DRY RUN] would move",file,"->",others_path)
            else:
                shutil.move(full_path,others_path)

                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                message = f"{current_time} | Moved {file} -> {others_path}"
                with open(LOG_FILE, "a") as log:
                   log.write(message + "\n")

    
print(" all files organized sucessfully!")
        
