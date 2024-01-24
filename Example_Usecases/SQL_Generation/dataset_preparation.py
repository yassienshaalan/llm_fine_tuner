# dataset_preparation.py

from datasets import load_dataset
import os

def prepare_nl2sql_dataset(dataset_name="spider", local_path=None):
    """
    Prepares the NL2SQL dataset.

    Parameters:
    dataset_name (str): Name of the dataset to load. Default is 'spider'.
    local_path (str): Local path to the dataset. If None, the dataset will be downloaded.

    Returns:
    Loaded or downloaded dataset.
    """

    if local_path and os.path.exists(local_path):
        print(f"Loading dataset from local path: {local_path}")
        dataset = load_dataset('json', data_files=local_path)
    else:
        print(f"Downloading and loading dataset: {dataset_name}")
        dataset = load_dataset(dataset_name)

    # Add any necessary preprocessing steps here
    return dataset

if __name__ == "__main__":
    # Example usage: Load 'spider' dataset from local path or download if not available
    dataset = prepare_nl2sql_dataset(local_path="./data/spider")
    # Additional code to process the dataset
