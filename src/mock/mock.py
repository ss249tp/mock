__all__ = (
    "load_text",
    "tokenize",
)


import os
import string


def load_text(path: str) -> str:
    """Load contents of a text file into a string.

    Args:
        path: Path to a text file.

    Returns:
        Text in the file as a string.

    Raises:
        ValueError: If `path` cannot be read as a text file.
    """

    if not os.path.isfile(path):
        raise ValueError(f"{path} either does not exist or is not a file.")

    try:
        with open(path, "r") as file:
            return file.read()
    except UnicodeDecodeError as err:
        raise ValueError(f"Failed to read {path} as a text file.") from err


def tokenize(text: str) -> list[str]:
    """Split a string into a list of words.

    Args:
        text: Text string to tokenize.

    Returns:
        A list of words in `text`, but with punctuations removed and letters lowercased.
    """

    for p in string.punctuation:
        text = text.replace(p, " ")

    return text.lower().split()
