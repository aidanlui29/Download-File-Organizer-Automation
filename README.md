# Download-File-Organizer-Automation

## Objective
The Download Folder Organizer Automation project was created to automatically organize files in the Downloads directory. The program scans files, sorts them into categorized folders (Documents, Images, Videos, Audio, Others), and detects duplicates using SHA-256 hashing. A log file is also generated to track all file movements, making the process efficient and auditable. This project was designed to improve workflow organization and demonstrate practical automation skills.

### Skills Learned
- Python scripting for automation and file management  
- File hashing for duplicate detection using SHA-256  
- Logging and audit tracking for system activity  
- Directory management using `os`, `shutil`, and `pathlib`  
- Strengthened problem-solving and debugging skills

### Tools Used
- Python  
- Cursor (AI-powered code editor)  
- Windows 11 environment  
- Built-in Python libraries (`os`, `shutil`, `hashlib`, `logging`, `pathlib`)

## Steps
1. Configure the target paths: set the Downloads directory as the working folder, define a Duplicates folder, and specify a log file to record actions.  
2. Define file categories and extensions (Documents, Images, Videos, Audio, Others) to determine where each file should be moved.  
3. Iterate through items in the Downloads directory, skipping any folders. For each file, compute a SHA-256 hash to check for duplicates.  
4. If a file is a duplicate, move it to the Duplicates folder and record the action in the log. Otherwise, determine its category by extension and move it into the matching subfolder, logging the move.  
5. When processing completes, confirm that the cleanup is done (console message) and review the log file for a record of all operations.
