"""
NovaScript Standard Library: Console Module

Provides enhanced logging and output operations.

Usage:
    var console = require("console")
    console.log("Hello")
    console.warn("Warning message")
    console.error("Error message")
    console.info("Info message")
"""

import sys
from typing import Any, Dict
from datetime import datetime


class ConsoleModule:
    """Provides console operations."""
    
    @staticmethod
    def log(*args) -> None:
        """
        Print log message to stdout.
        
        Args:
            *args: Arguments to print
        """
        message = ' '.join(str(arg) for arg in args)
        print(f"[LOG] {message}")
    
    @staticmethod
    def warn(*args) -> None:
        """
        Print warning message to stderr.
        
        Args:
            *args: Arguments to print
        """
        message = ' '.join(str(arg) for arg in args)
        print(f"[WARN] {message}", file=sys.stderr)
    
    @staticmethod
    def error(*args) -> None:
        """
        Print error message to stderr.
        
        Args:
            *args: Arguments to print
        """
        message = ' '.join(str(arg) for arg in args)
        print(f"[ERROR] {message}", file=sys.stderr)
    
    @staticmethod
    def info(*args) -> None:
        """
        Print info message to stdout.
        
        Args:
            *args: Arguments to print
        """
        message = ' '.join(str(arg) for arg in args)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {message}")
    
    @staticmethod
    def debug(*args) -> None:
        """
        Print debug message to stdout.
        
        Args:
            *args: Arguments to print
        """
        message = ' '.join(str(arg) for arg in args)
        print(f"[DEBUG] {message}")
    
    @staticmethod
    def clear() -> None:
        """Clear the console screen."""
        import os
        os.system('cls' if os.name == 'nt' else 'clear')


def create_module() -> Dict[str, Any]:
    """Create console module with callable functions."""
    return {
        'log': ConsoleModule.log,
        'warn': ConsoleModule.warn,
        'error': ConsoleModule.error,
        'info': ConsoleModule.info,
        'debug': ConsoleModule.debug,
        'clear': ConsoleModule.clear,
    }
