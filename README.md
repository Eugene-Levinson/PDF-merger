## Setup

### Install dependencies
```bash
pip install PyPDF2
```

### Prep files
Place all the pdfs to be combined in one folder. Add a number to the front of each of the file names, seperated by a space to dictate the order in which they will be combined. For example: `foo.pdf` => `1 foo.pdf` and `bar.pdf` => `2 bar.pdf`.


## Usage
```
python combine.py <input_dir> <output file name>
```

For example:
```bash
python combine.pdf mypdfs-folder combined.pdf
```

