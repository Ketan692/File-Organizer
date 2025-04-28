import os
import shutil
import argparse
import json


def load_file_types(json_path='extentions.json'):
    with open(json_path, 'r') as f:
        return json.load(f)

def organize(folder_path, dry_run=False):
    file_types = load_file_types()
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()
            moved = False
            
            for folder_name, extensions in file_types.items():
                if file_extension in extensions:
                    target_folder = os.path.join(folder_path, folder_name)
                    if not os.path.exists(target_folder):
                        os.makedirs(target_folder)
                    if dry_run:
                        print(f"[DRY RUN] Would move: {filename} → {folder_name}/{filename}")
                    else:
                        shutil.move(file_path, target_folder)
                        print(f"Moved: {filename} → {folder_name}/{filename}")
                    moved = True
                    break
            
            if not moved:
                other_folder = os.path.join(folder_path, 'Other')
                if not os.path.exists(other_folder):
                    os.makedirs(other_folder)
                if dry_run:
                    print(f"[DRY RUN] Would move: {filename} → Other/{filename}")
                else:
                    shutil.move(file_path, other_folder)
                    print(f"Moved: {filename} → Other/{filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Organize files in a folder.')
    parser.add_argument('folder', type=str, help='Path to the folder to organize')
    parser.add_argument('--dry-run', action='store_true', help='Preview changes without moving files')
    args = parser.parse_args()

    folder_path = args.folder
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        organize(folder_path, dry_run=args.dry_run)
        if args.dry_run:
            print(f"Dry run complete. No files were moved.")
        else:
            print(f"Files in '{folder_path}' have been organized.")
    else:
        print(f"Error: '{folder_path}' is not a valid directory.")


