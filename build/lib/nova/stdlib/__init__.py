"""
NovaScript Standard Library

Available modules:
- fs: File system operations (read/write files)
- console: Logging and output (log, warn, error)
- math: Mathematical functions (sqrt, pow, sin, cos, etc)
- random: Random number generation (randInt, choice, shuffle)
- date: Date and time operations (now, format, addDays)
- http: HTTP requests (get, post, put, delete)

Usage:
    var fs = require("fs")
    var math = require("math")
    var result = math.sqrt(16)
"""

from nova.stdlib import fs, console, math, random, date, http

__all__ = ['fs', 'console', 'math', 'random', 'date', 'http']
