"""
NovaScript - A lightweight, modern programming language runtime

Version: 1.0.0
Homepage: https://github.com/YourRepo/NovaScript

Main API:
- run_code(source): Execute NovaScript code from string
- run_file(filename): Execute NovaScript file
- run_repl(): Start interactive REPL

Example:
    from nova import run_code
    output = run_code('print("Hello, Nova!")')
"""

from nova.interpreter import (
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
