# 📁 Recursive File Organizer (Python)

A recursive file organizer built using Python that automatically sorts files into categorized folders based on their file extensions.

This project demonstrates filesystem handling, recursion, logging, and safe automation design.

---

## 🚀 Features

- 🔄 Recursive folder traversal (handles subfolders automatically)
- 📂 Organizes files by extension:
  - `.py` → Python_files
  - `.docx` → Documents
  - `.jpg` → Pictures
  - Others → Others
- 🛡️ DRY_RUN mode for safe testing (no actual file movement)
- 📝 Timestamped logging system
- 🚫 Skips destination folders to prevent infinite loops
- 🚫 Skips log file to avoid self-processing

---

## 🛠 Technologies Used

- Python
- `os` module
- `shutil` module
- `datetime` module

---

## 📌 How It Works

The script:

1. Walks through all folders recursively using `os.walk()`
2. Identifies files based on extension
3. Moves them into categorized folders
4. Logs all operations with timestamps
5. Supports DRY_RUN mode for safe preview

---

## 🔧 Configuration

At the top of the script:

```python
DRY_RUN = True
```
True - Only show what would happen
False - Actually moves files

## 📂 Example

### Before

```
file_organize/
│── test.py
│── image.jpg
│── project1/
│   └── notes.docx
```

### After

```
file_organize/
│
├── Python_files/
│   └── test.py
├── Pictures/
│   └── image.jpg
├── Documents/
│   └── notes.docx
├── Others/
```

### 👨‍💻 Author
Aditya Sharma  
Diploma in Computer Science & Engineering  
Interested in Automation & AI
