import os
import shutil
from pathlib import Path
from datetime import datetime, timedelta

def sort_downloads():
    # Define the Downloads path
    downloads_path = Path.home() / "Downloads"
    
    # Define what extensions belong to which category
    categories = {
        "Images": ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp'],
        "PDFs": ['.pdf'],
        "Videos": ['.mp4', '.mov', '.mkv', '.avi', '.wmv', '.flv']
    }

    print(f"Scanning folder: {downloads_path}\n")

    # Calculate the 14-day cutoff
    now = datetime.now()
    two_weeks_ago = now - timedelta(days=14)

    # Iterate through files in the Downloads folder
    for file_path in downloads_path.iterdir():
        # Only process files (this automatically ignores your new category folders)
        if file_path.is_file() and file_path.name != ".DS_Store":
            
            timestamp = file_path.stat().st_mtime
            file_date = datetime.fromtimestamp(timestamp)
            
            # Only proceed if the file is older than 14 days
            if file_date < two_weeks_ago:
                
                file_ext = file_path.suffix.lower()
                dest_category = "Others"
                for category, extensions in categories.items():
                    if file_ext in extensions:
                        dest_category = category
                        break
                
                # Destination folder is now directly inside Downloads
                dest_folder = downloads_path / dest_category
                dest_folder.mkdir(parents=True, exist_ok=True)
                
                # Determine final path and prevent overwriting files with the same name
                dest_path = dest_folder / file_path.name
                counter = 1
                while dest_path.exists():
                    dest_path = dest_folder / f"{file_path.stem}_{counter}{file_path.suffix}"
                    counter += 1
                    
                # Move the file
                print(f"Moving: {file_path.name} -> {dest_category}/")
                shutil.move(str(file_path), str(dest_path))

    print("\nAll done! Old files have been gracefully organized directly in your Downloads folder.")

if __name__ == "__main__":
    sort_downloads()