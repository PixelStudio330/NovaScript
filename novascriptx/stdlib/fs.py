"""
NovaScript Standard Library: File System Module

Provides file I/O operations for NovaScript programs.

Usage:
    var fs = require("fs")
    fs.writeFile("test.txt", "Hello World")
    var content = fs.readFile("test.txt")
    print(content)
"""

import os
from typing import Any, Dict


class FileSystemModule:
    """Provides file system operations."""
    
    @staticmethod
    def read_file(filename: str) -> str:
        """
        Read entire file contents as string.
        
        Args:
            filename: Path to file
            
        Returns:
            File contents as string
            
        Raises:
            FileNotFoundError: If file doesn't exist
        """
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {filename}")
    
    @staticmethod
    def write_file(filename: str, content: str) -> None:
        """
        Write content to file (overwrites if exists).
        
        Args:
            filename: Path to file
            content: Content to write
        """
        # Create directory if needed
        dirname = os.path.dirname(filename)
        if dirname and not os.path.exists(dirname):
            os.makedirs(dirname, exist_ok=True)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(str(content))
    
    @staticmethod
    def append_file(filename: str, content: str) -> None:
        """
        Append content to file.
        
        Args:
            filename: Path to file
            content: Content to append
        """
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(str(content))
    
    @staticmethod
    def file_exists(filename: str) -> bool:
        """
        Check if file exists.
        
        Args:
            filename: Path to file
            
        Returns:
            True if file exists, False otherwise
        """
        return os.path.isfile(filename)
    
    @staticmethod
    def delete_file(filename: str) -> None:
        """
        Delete a file.
        
        Args:
            filename: Path to file to delete
        """
        if os.path.isfile(filename):
            os.remove(filename)
    
    @staticmethod
    def list_files(directory: str = ".") -> list:
        """
        List files in directory.
        
        Args:
            directory: Directory path
            
        Returns:
            List of file names in directory
        """
        try:
            return os.listdir(directory)
        except FileNotFoundError:
            raise FileNotFoundError(f"Directory not found: {directory}")


def create_module() -> Dict[str, Any]:
    """Create fs module with callable functions."""
    return {
        'readFile': FileSystemModule.read_file,
        'writeFile': FileSystemModule.write_file,
        'appendFile': FileSystemModule.append_file,
        'fileExists': FileSystemModule.file_exists,
        'deleteFile': FileSystemModule.delete_file,
        'listFiles': FileSystemModule.list_files,
    }
