#!/usr/bin/env python3
"""
NovaScript-X CLI - Command-line interface for the NovaScript runtime

Usage:
    novax [options] [file.nova]
    novax -v
    novax --repl
    novax --serve server.nova
    novax --watch program.nova

This module provides the entry point for the 'novax' command when installed via pip.
"""

import argparse
import sys
import os
import time
from pathlib import Path
from typing import Optional

from novascriptx.interpreter import run_code, run_file, run_repl, __version__


def watch_file(filename: str, debug: bool = False) -> None:
    """
    Watch a file for changes and re-run on modification (watch mode).
    
    Args:
        filename: Path to .nova file to watch
        debug: Enable debug output
    """
    filepath = Path(filename)
    
    if not filepath.exists():
        print(f"Error: File '{filename}' not found", file=sys.stderr)
        sys.exit(1)
    
    initial_mtime = filepath.stat().st_mtime
    print(f"Watching {filename} for changes... (Ctrl+C to stop)")
    print("-" * 60)
    
    try:
        while True:
            try:
                current_mtime = filepath.stat().st_mtime
                
                if current_mtime != initial_mtime:
                    print(f"\n[{time.strftime('%H:%M:%S')}] File changed, re-running...\n")
                    execute_file(filename, debug)
                    initial_mtime = current_mtime
                
                time.sleep(0.5)
            except KeyboardInterrupt:
                raise
            except FileNotFoundError:
                print(f"Error: File '{filename}' was deleted", file=sys.stderr)
                break
            except Exception as e:
                print(f"Error: {e}", file=sys.stderr)
                initial_mtime = filepath.stat().st_mtime
    except KeyboardInterrupt:
        print("\n\nWatch mode stopped")
        sys.exit(0)


def execute_file(filename: str, debug: bool = False) -> None:
    """
    Execute a NovaScript file.
    
    Args:
        filename: Path to .nova file
        debug: Enable debug output
    """
    try:
        output = run_file(filename, debug=debug)
        if output:
            print(output, end='')
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except RuntimeError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def execute_code(code: str, debug: bool = False) -> None:
    """
    Execute NovaScript code from string.
    
    Args:
        code: NovaScript source code
        debug: Enable debug output
    """
    try:
        output = run_code(code, debug=debug)
        if output:
            print(output, end='')
    except RuntimeError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def main(argv: Optional[list] = None) -> int:
    """
    Main CLI entry point.
    
    Args:
        argv: Command-line arguments (defaults to sys.argv[1:])
        
    Returns:
        Exit code (0 for success, 1 for error)
    """
    parser = argparse.ArgumentParser(
        prog='novax',
        description='NovaScript-X Runtime - A lightweight programming language',
        epilog='Examples:\n'
               '  novax script.nova              # Run a script\n'
               '  novax                          # Interactive REPL\n'
               '  novax -w script.nova           # Watch mode\n'
               '  novax --debug script.nova      # Debug mode',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    # Version
    parser.add_argument(
        '-v', '--version',
        action='version',
        version=f'NovaScript-X {__version__}'
    )
    
    # File execution
    parser.add_argument(
        'file',
        nargs='?',
        help='NovaScript file to execute'
    )
    
    # REPL mode
    parser.add_argument(
        '-r', '--repl',
        action='store_true',
        help='Start interactive REPL mode'
    )
    
    # Watch mode
    parser.add_argument(
        '-w', '--watch',
        action='store_true',
        help='Watch file for changes and auto-run on modification'
    )
    
    # Debug mode
    parser.add_argument(
        '--debug',
        action='store_true',
        help='Enable debug output'
    )
    
    # Execute code directly
    parser.add_argument(
        '-c',
        dest='code',
        metavar='CODE',
        help='Execute code from command line'
    )
    
    # Web server mode (placeholder for later)
    parser.add_argument(
        '--serve',
        dest='serve_file',
        metavar='FILE',
        help='Run NovaScript HTTP server'
    )
    
    # Parse arguments
    args = parser.parse_args(argv)
    
    # Determine what to do based on arguments
    if args.code:
        # Execute code from -c option
        execute_code(args.code, debug=args.debug)
        return 0
    
    elif args.serve_file:
        # Web server mode (TODO: implement)
        print(f"Error: Web server mode not yet implemented", file=sys.stderr)
        print(f"Use: novax {args.serve_file} to run as regular script", file=sys.stderr)
        return 1
    
    elif args.watch and args.file:
        # Watch mode
        watch_file(args.file, debug=args.debug)
        return 0
    
    elif args.repl or (not args.file and not args.code):
        # Interactive REPL mode
        run_repl()
        return 0
    
    elif args.file:
        # Execute file
        execute_file(args.file, debug=args.debug)
        return 0
    
    else:
        # Default to REPL
        run_repl()
        return 0


if __name__ == '__main__':
    sys.exit(main())
