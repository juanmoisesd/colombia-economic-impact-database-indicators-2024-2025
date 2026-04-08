import os
import pandas as pd
import pytest

def test_files_exist():
    assert os.path.exists("data_dictionary.csv")
    assert os.path.exists("CODEBOOK.md")

def test_data_dictionary_format():
    df = pd.read_csv("data_dictionary.csv")
    assert "variable" in df.columns
    assert "description" in df.columns
