import json
import sys
import os
import glob

def clean_notebook(notebook_path, output_path=None):
    """
    Clean a Jupyter notebook to reduce file size by removing:
    - All output cells
    - Widget state data
    - Execution counts
    """
    if output_path is None:
        output_path = notebook_path

    try:
        # Load notebook
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)

        # Clear outputs and execution counts from all cells
        cells_modified = 0
        for cell in notebook.get('cells', []):
            if cell.get('cell_type') == 'code':
                # Clear outputs
                if cell.get('outputs'):
                    cell['outputs'] = []
                    cells_modified += 1

                # Clear execution count
                if cell.get('execution_count') is not None:
                    cell['execution_count'] = None
                    cells_modified += 1

        # Remove widget state from metadata
        if 'metadata' in notebook:
            if 'widgets' in notebook['metadata']:
                del notebook['metadata']['widgets']

        # Save cleaned notebook
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, indent=1, ensure_ascii=False)

        # Calculate size reduction
        original_size = os.path.getsize(notebook_path)
        cleaned_size = os.path.getsize(output_path)
        reduction = (1 - cleaned_size/original_size) * 100 if original_size > 0 else 0

        return original_size, cleaned_size, reduction

    except Exception as e:
        print(f"Error processing {notebook_path}: {e}")
        return None, None, None

def clean_all_notebooks():
    """Clean all Jupyter notebooks in the current directory"""
    # Get current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Find all .ipynb files in the current directory
    notebook_pattern = os.path.join(current_dir, "*.ipynb")
    notebook_files = glob.glob(notebook_pattern)

    if not notebook_files:
        print("No Jupyter notebook files found in the current directory.")
        return

    print(f"Found {len(notebook_files)} notebook(s) to clean:")
    print("-" * 60)

    total_original_size = 0
    total_cleaned_size = 0
    successful_cleanings = 0

    for notebook_path in notebook_files:
        notebook_name = os.path.basename(notebook_path)
        print(f"Processing: {notebook_name}")

        original_size, cleaned_size, reduction = clean_notebook(notebook_path)

        if original_size is not None:
            print(f"  Original: {original_size/1024/1024:.2f} MB")
            print(f"  Cleaned:  {cleaned_size/1024/1024:.2f} MB")
            print(f"  Reduction: {reduction:.1f}%")

            total_original_size += original_size
            total_cleaned_size += cleaned_size
            successful_cleanings += 1

        print("-" * 60)

    # Summary
    if successful_cleanings > 0:
        total_reduction = (1 - total_cleaned_size/total_original_size) * 100 if total_original_size > 0 else 0
        print("SUMMARY:")
        print(f"Successfully cleaned: {successful_cleanings}/{len(notebook_files)} notebooks")
        print(f"Total original size: {total_original_size/1024/1024:.2f} MB")
        print(f"Total cleaned size: {total_cleaned_size/1024/1024:.2f} MB")
        print(f"Total size reduction: {total_reduction:.1f}%")
    else:
        print("No notebooks were successfully cleaned.")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        # No arguments - clean all notebooks in current directory
        clean_all_notebooks()
    elif len(sys.argv) == 2:
        # Single argument - clean specific notebook
        notebook_path = sys.argv[1]
        original_size, cleaned_size, reduction = clean_notebook(notebook_path)
        if original_size is not None:
            print(f"Original size: {original_size/1024/1024:.2f} MB")
            print(f"Cleaned size: {cleaned_size/1024/1024:.2f} MB")
            print(f"Size reduction: {reduction:.1f}%")
            print(f"Cleaned notebook saved as: {notebook_path}")
    else:
        print("Usage:")
        print("  python clean_notebook.py                    # Clean all notebooks in current directory")
        print("  python clean_notebook.py <notebook_path>    # Clean specific notebook")
        sys.exit(1)
