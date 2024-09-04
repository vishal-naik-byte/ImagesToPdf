# ImagesToPdf

**ImagesToPdf** is a Python script combined with a shell script to convert images to a PDF and recover corrupted PDFs.

## Features

- **Convert Images to PDF:** Converts `.webp`, `.jpeg`, and `.jpg` images in a specified directory into a single PDF file.
- **Recover Corrupted PDF:** Merges a potentially corrupted PDF with a valid PDF to recover the contents using Ghostscript.

## Requirements

- Python 3.6 or higher
- `Pillow` library
- `ghostscript` (for PDF recovery)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/ImagesToPdf.git
   ```
2. Navigate to the project directory:

    ```cd ImagesToPdf```

Install the required Python dependencies:

```pip install pillow```

Install Ghostscript for PDF recovery:

- On Ubuntu/Debian:

    ```sudo apt-get install ghostscript```

- On macOS:

    ```brew install ghostscript```

## Usage:

**Convert Images to PDF**

1. Edit the directory_path in imageToPdf.py to specify the directory containing your images.

2. Run the Python script to convert images to a PDF:

    ```python imageToPdf.py```

This will generate images1.pdf in the specified directory.

## Recover Corrupted PDF

1. Ensure you have images.pdf (the potentially corrupted PDF) in the same directory.

2. Run the shell script to recover the corrupted PDF:

    ```bash join.sh```

This will create output.pdf, which attempts to recover the contents from images.pdf and creates new file as recovered.pdf.

## Example

To convert images in the Documents directory:

    python imageToPdf.py

To recover a corrupted PDF:

    bash join.sh

## Contributing

Feel free to open issues or submit pull
