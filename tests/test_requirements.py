import pytest

def test_requirements():
    """
    Pytest test
    ---
    Objective:
    Params:
    """
    packages=["gtts","docx", "PyPDF2"]
    for package in packages:
        assert __import__(package)