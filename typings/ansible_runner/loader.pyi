"""
This type stub file was generated by pyright.
"""

class ArtifactLoader:
    """
    Handles loading and caching file contents from disk

    This class will load the file contents and attempt to deserialize the
    contents as either JSON or YAML.  If the file contents cannot be
    deserialized, the contents will be returned to the caller as a string.

    The deserialized file contents are stored as a cached object in the
    instance to avoid any additional reads from disk for subsequent calls
    to load the same file.
    """

    def __init__(self, base_path) -> None: ...
    def get_contents(self, path):  # -> str:
        """
        Loads the contents of the file specified by path

        Args:
            path (string): The relative or absolute path to the file to
                be loaded.  If the path is relative, then it is combined
                with the base_path to generate a full path string

        Returns:
            string: The contents of the file as a string

        Raises:
            ConfigurationError: If the file cannot be loaded
        """
        ...

    def abspath(self, path):  # -> str:
        """
        Transform the path to an absolute path

        Args:
            path (string): The path to transform to an absolute path

        Returns:
            string: The absolute path to the file
        """
        ...

    def isfile(self, path):  # -> bool:
        """
        Check if the path is a file

        :params path: The path to the file to check.  If the path is relative
            it will be exanded to an absolute path

        :returns: boolean
        """
        ...

    def load_file(
        self, path, objtype=..., encoding=...
    ):  # -> Any | bytes | str | None:
        """
        Load the file specified by path

        This method will first try to load the file contents from cache and
        if there is a cache miss, it will load the contents from disk

        Args:
            path (string): The full or relative path to the file to be loaded

            encoding (string): The file contents text encoding

            objtype (object): The object type of the file contents.  This
                is used to type check the deserialized content against the
                contents loaded from disk.
                Ignore serializing if objtype is string_types

        Returns:
            object: The deserialized file contents which could be either a
                string object or a dict object

        Raises:
            ConfigurationError:
        """
        ...
