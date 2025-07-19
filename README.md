# 🧹 nbclean - Clean up Notebooks to Reduce File Size

A simple Python script that cleans Jupyter notebooks by removing outputs, execution counts, and widget metadata to significantly reduce file size.

## 🎯 What it does

- 🗑️ Removes all cell outputs
- 🔢 Clears execution counts
- 🎛️ Removes widget state metadata
- 📉 Reduces notebook file sizes by 40-90%

## 💡 Why use this?

- **Version control**: Cleaner git diffs without output noise
- **File sharing**: Smaller files for easier sharing
- **Storage**: Reduced disk space usage
- **Collaboration**: Removes execution-specific data for cleaner handoffs

## ✨ Features

- **Batch processing**: Automatically finds and cleans all `.ipynb` files
- **Size reporting**: Shows before/after sizes and reduction percentage
- **Error handling**: Continues processing even if some notebooks fail
- **Summary stats**: Displays total space saved across all notebooks

## ⚡ Requirements

- Python 3.x
- No external dependencies (uses only standard library)

## 🛠️ Installation

1. **Download** the `clean_notebook.py` file, or
2. **Clone** the repository:
   ```bash
   git clone https://github.com/lisekarimi/nbclean.git
   ```
3. **Run** it in your notebook directory

✅ No `uv init` or dependencies needed!

## 🚀 Usage

### Clean all notebooks in current directory
```bash
python clean_notebook.py
```

### Clean a specific notebook
```bash
python clean_notebook.py notebook_name.ipynb
```

## 📏 Check file sizes (Git Bash)

**Before cleaning:**
```bash
ls -lah *.ipynb
```

**After cleaning:**
```bash
ls -lah *.ipynb
```

## 📋 Example Output

```
Found 18 notebook(s) to clean:
------------------------------------------------------------
Processing: nb_data_science.ipynb
  Original: 0.29 MB
  Cleaned:  0.03 MB
  Reduction: 89.5%
------------------------------------------------------------
SUMMARY:
Successfully cleaned: 18/18 notebooks
Total original size: 4.12 MB
Total cleaned size: 2.63 MB
Total size reduction: 36.2%
```
## Licence
MIT
