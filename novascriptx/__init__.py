"""
NovaScript-X - A lightweight, modern programming language runtime

Version: 1.0.0
Homepage: https://github.com/YourRepo/NovaScript-X

Main API:
- run_code(source): Execute NovaScript code from string
- run_file(filename): Execute NovaScript file
- run_repl(): Start interactive REPL

Example:
    from novascriptx import run_code
    output = run_code('print("Hello, NovaScript-X!")')
"""

from novascriptx.interpreter import (
    __version__,
    Lexer,
    Parser,
    Executor,
    Token,
    run_code,
    run_file,
    run_repl,
)

__all__ = [
    '__version__',
    'Lexer',
    'Parser',
    'Executor',
    'Token',
    'run_code',
    'run_file',
    'run_repl',
]
