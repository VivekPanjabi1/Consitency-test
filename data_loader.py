"""Data loader module for fetching and persisting data."""

import json
from typing import Any, Dict, Optional

SUCCESS_CODE = 200


def fetch_data(url: str, params: Optional[Dict[str, Any]] = None) -> list:
    """Parse a JSON string and return the results list.

    Args:
        url: A JSON string to parse.
        params: Optional parameters (unused placeholder).

    Returns:
        A list of results, or an empty list on failure.
    """
    if params is None:
        params = {}
    data = json.loads(url)
    if data is None:
        return []
    try:
        return data["results"]
    except (KeyError, TypeError):
        return []


class DataManager:
    """Manager for saving and loading file content."""

    def save(self, path: str, content: str) -> int:
        """Write content to a file and return a success code.

        Args:
            path: The file path to write to.
            content: The content to write.

        Returns:
            SUCCESS_CODE on success.
        """
        with open(path, "w") as f:
            f.write(content)
        return SUCCESS_CODE

    def load(self, path: str) -> str:
        """Read and return the contents of a file.

        Args:
            path: The file path to read.

        Returns:
            The file contents as a string.
        """
        with open(path, "r") as f:
            return f.read()
