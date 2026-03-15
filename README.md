# Downloads Auto-Sorter

A lightweight Python script that keeps your Downloads folder clean by automatically organizing files into category folders (Images, PDFs, Videos, Others). To prevent moving files you are currently working on, it only sorts files that are **older than 14 days**.

## How It Works
The script scans your default Downloads folder and moves files into subfolders based on their extensions:
* **Images:** `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.svg`, `.webp`
* **PDFs:** `.pdf`
* **Videos:** `.mp4`, `.mov`, `.mkv`, `.avi`, `.wmv`, `.flv`
* **Others:** Everything else

## How to Run Manually
1. Make sure you have [Python](https://www.python.org/downloads/) installed.
2. Clone or download this repository.
3. Open your terminal or command prompt and run:
   ```bash
   python sort_downloads.py


## How to Automate (Run every Sunday at Midnight)

You can set this script to run silently in the background so you never have to organize your Downloads folder manually again.

### For Mac & Linux (using Cron)
1. Open your Terminal.
2. Type `crontab -e` and press **Enter**.
3. Add the following line to the bottom of the file (be sure to replace the paths with your actual system paths):
   ```text
   0 0 * * 0 /usr/bin/python3 /path/to/your/sort_downloads.py

4. Save and exit the editor.

## For Windows (using Task Scheduler)

1. Open the Start Menu, search for Task Scheduler, and open it.

2. Click Create Basic Task... on the right sidebar.

3. Name the task "Downloads Auto-Sorter" and click Next.

4. Set the Trigger to Weekly, select Sunday, and set the time to 12:00:00 AM.

5. Set the Action to Start a program.

6. In the Program/script box, type python.

7. In the Add arguments box, type the full path to where you saved the script, enclosed in quotation marks (e.g., "C:\Users\YourName\Documents\sort_downloads.py").

8. Click Finish.

Have Fun.
