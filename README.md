# File Organizer CLI

A Python script to organize files in a folder by file type. It moves files into respective subfolders such as `Images`, `Videos`, `Documents`, `Music`, and `Others`. The script can also be run in "dry run" mode to preview the changes without actually moving the files.

## ⚙️ Features

- **Organize Files**: Moves files into appropriate subfolders based on their extension.
- **Dry Run Mode**: Preview what files would be moved without actually moving them.
- **Customizable File Types**: Add or modify file types by editing the `extentions.json` file.

## 📝 Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [License](#license)

## 🛠️ Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Ketan692/File-Organizer.git
    cd File-Organizer
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/Mac
    venv\Scripts\activate     # On Windows
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## ⚡ Usage

### 1. Basic Command to Organize Files:

```bash
python main.py /path/to/your/folder
```

### 2. Dry Run (Preview Without Moving Files):
```bash
python main.py /path/to/your/folder --dry-run
```
This will show you which files would be moved and to which folder, without actually performing the operation.

Example:

```bash
python main.py /path/to/your/folder --dry-run
```
Output Example:
```bash
File 'image1.jpg' would be moved to 'Images' folder.
File 'document1.pdf' would be moved to 'Documents' folder.
```

## ⚙️ Configuration
The script uses a JSON file called extentions.json to define file types and their respective extensions. You can modify this file to add or remove file types.

Example of extentions.json:

```json
{
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Music": [".mp3", ".wav"]
}
```
Feel free to edit this file to suit your needs.

## 📝 License
This project is licensed under the MIT License - see the LICENSE file for details.
