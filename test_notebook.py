import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

def test_clustering_notebook_execution():
    """
    Test that the Clustering .ipynb notebook can be executed from start to finish
    without throwing any exceptions.
    """
    notebook_filename = 'Clustering .ipynb'
    assert os.path.exists(notebook_filename), f"Notebook file {notebook_filename} not found."

    with open(notebook_filename) as f:
        nb = nbformat.read(f, as_version=4)

    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')

    try:
        # Preprocess (execute) the notebook in the current directory
        ep.preprocess(nb, {'metadata': {'path': './'}})
    except Exception as e:
        assert False, f"Notebook execution failed with exception: {e}"
