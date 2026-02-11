# NovaScript Development Guide

This document outlines the architecture, development progress, and future roadmap for NovaScript.

## 📊 Project Status

**Version**: 1.0.0 (Beta)  
**Status**: Core runtime and CLI complete, web runtime in development  
**Last Updated**: February 2026

### Completed Features (v1.0)

- ✅ **Core Interpreter**
  - Lexer: Full tokenization with keywords, operators, strings, numbers
  - Parser: Recursive descent parser with operator precedence
  - Executor: Full execution engine with scopes and function calls
  - 923 lines of well-documented Python code

- ✅ **CLI Runtime**
  - File execution: `nova script.nova`
  - Interactive REPL: `nova`
  - Watch mode: `nova --watch script.nova`
  - Debug mode: `nova --debug`
  - Inline code: `nova -c 'print()'`
  - Version display: `nova --version`
  - Help system: `nova --help`

- ✅ **Package Distribution**
  - `setup.py` configured for pip installation
  - Installable via `pip install .`
  - Creates global `nova` command
  - Cross-platform support (Windows, macOS, Linux)

- ✅ **Standard Library (6 modules)**
  - `fs`: File system operations (readFile, writeFile, deleteFile, etc.)
  - `console`: Logging and output (log, warn, error, info, debug)
  - `math`: Mathematical functions (sqrt, pow, floor, ceil, sin, cos, pi, e, etc.)
  - `random`: Random number generation (randInt, randFloat, choice, shuffle, seed)
  - `date`: Date/time operations (now, format, getYear, getMonth, addDays, etc.)
  - `http`: HTTP requests (get, post, put, delete)

- ✅ **Module System**
  - `require()` built-in function
  - Dynamic module loading
  - Module caching

- ✅ **Language Features**
  - Variables: `var x = 10`
  - Functions: `function name(params): { body }`
  - Control flow: `if/else`, `while`, `for`
  - Operators: Arithmetic, comparison, logical
  - Recursion support
  - String concatenation with type coercion
  - Comments with `#`

- ✅ **Examples**
  - Hello World tutorial
  - Functions, loops, and recursion demo
  - Standard library showcase

- ✅ **Documentation**
  - Comprehensive README.md
  - Examples with working code
  - CLI help system
  - Code comments and docstrings

### In Progress / Planned (v1.1+)

#### 🚧 High Priority (v1.1)

1. **Member Access (Dot Notation)**
   - Enable `math.sqrt(16)` syntax
   - Enable `obj.property` access
   - Requires parser changes for DOT token handling
   - Needed for stdlib module functions

2. **Arrays/Lists**
   - Array literals: `var arr = [1, 2, 3]`
   - Array indexing: `arr[0]`
   - Array methods: `length`, `push`, `pop`, etc.
   - Iteration: Integrate with for loops

3. **Objects/Dictionaries**
   - Object literals: `var obj = {key: value}`
   - Property access: `obj.key`, `obj["key"]`
   - Methods on objects
   - JSON-like syntax

4. **Web Server Support**
   - `nova --serve` command
   - HTTP route handling
   - `res.send()` and `res.json()` in NovaScript
   - Request/response objects
   - Route definitions in NovaScript

#### 📋 Medium Priority (v1.2)

5. **Web Framework (nova-web)**
   - `nova create myapp` scaffold command
   - Folder structure: pages/, routes/, public/, styles/
   - Server-side rendering
   - Hot reload in development
   - Template support for HTML generation

6. **More Standard Library**
   - `url`: URL parsing / manipulation
   - `json`: JSON encode/decode (JSON support in language)
   - `string`: String utilities (split, trim, upper, lower, etc.)
   - `stream`: Stream processing
   - `os`: OS operations (env vars, paths, etc.)

7. **Language Enhancements**
   - String templates / interpolation
   - Try/catch error handling
   - Type annotations (optional)
   - Better error messages with line numbers
   - stack traces for debugging

#### 🔮 Lower Priority (v1.3+)

8. **Advanced Features**
   - Classes and OOP
   - Async/await support
   - Modules/packages (multi-file projects)
   - Package manager (novapkg)
   - Testing framework
   - Build tools / bundler

## 🏗️ Architecture

### Package Structure

```
nova/
├── __init__.py              # Main package exports
├── interpreter.py           # Core interpreter (Lexer, Parser, Executor)
└── stdlib/                  # Standard library modules
    ├── __init__.py
    ├── fs.py                # File system (read, write, delete)
    ├── console.py           # Logging (log, warn, error)
    ├── math.py              # Math functions (sqrt, pow, floor, ceil)
    ├── random.py            # Random (randInt, choice, shuffle)
    ├── date.py              # Date/time (now, format, addDays)
    └── http.py              # HTTP requests (get, post, put, delete)

nova_cli.py                 # CLI entry point (argparse)
setup.py                    # Installation configuration
examples/                   # Example programs
├── hello_world/
├── functions_loops/
└── stdlib_demo/
```

### Interpreter Components

**Lexer** (235 lines)
- Input: NovaScript source code string
- Output: List of Token objects
- Handles: Keywords, identifiers, strings, numbers, operators, punctuation

**Parser** (360 lines)
- Input: Token list
- Output: AST (list of statement dicts)
- Implements: Recursive descent parsing with operator precedence
- Supports: All NovaScript language constructs

**Executor** (220 lines)
- Input: AST statements
- Output: Execution results + stdout
- Manages: Global and local scopes, function calls, returns
- Implements: All operators, control flow, function execution

### Execution Flow

```
Source Code → Lexer → Tokens → Parser → AST → Executor → Output
```

## 💻 Development Setup

### Install for Development

```bash
cd NovaScript
pip install -e .
```

### Run Tests

```bash
# Test file execution
python nova_cli.py examples/hello_world/main.nova

# Test REPL
python nova_cli.py

# Test inline code
python nova_cli.py -c 'print(5 + 3)'

# Test watch mode
python nova_cli.py -w examples/hello_world/main.nova
```

### Running Examples

```bash
# Hello world
python nova_cli.py examples/hello_world/main.nova

# Complex example
python nova_cli.py examples/functions_loops/main.nova

# Stdlib demo
python nova_cli.py examples/stdlib_demo/main.nova
```

## 🔄 Development Guidelines

### Code Style

- **Python version**: 3.7+
- **Type hints**: Use type annotations for clarity
- **Docstrings**: Document all classes and methods
- **Comments**: Explain complex logic
- **Line length**: Keep under 100 characters

### Adding Features

1. **New Keywords**: Add to `Lexer.KEYWORDS`
2. **New Operators**: Add to parser (parse_* methods)
3. **New Statements**: Add to `Parser.parse_statement()`
4. **New Builtin Functions**: Add to `Executor` class
5. **New Stdlib Module**: Create in `nova/stdlib/module_name.py`

### Testing

Create test scripts in `examples/` directory showing:
- What the feature does
- Example usage
- Expected output

## 📚 Implementation Notes

### Dot Notation Implementation (for v1.1)

To implement member access (`math.sqrt()`):

1. **Lexer**: Already handles DOT token ✓
2. **Parser**: Add member access in `parse_primary()` 
   - Check for DOT after identifier
   - Create member access AST node
3. **Executor**: Add member access evaluation
   - Support for dict/object properties
   - Support for method calls

Example AST:
```python
{
    'type': 'member_access',
    'object': {'type': 'identifier', 'name': 'math'},
    'member': 'sqrt',
    'call_args': [16]  # if it's a method call
}
```

### Array Implementation (for v1.1)

1. **Lexer**: Handle `[` and `]` (already done) ✓
2. **Parser**: Add array literal parsing
   - `parse_primary()` checks for `[`
   - Parse comma-separated expressions
3. **Parser**: Add array indexing
   - Check for `[` after expression
   - Create index access AST node
4. **Executor**: Store arrays as Python lists
   - Implement index access
   - Add array methods

## 🐛 Known Limitations (v1.0)

- ❌ No member access (dot notation)
- ❌ No arrays/lists
- ❌ No objects/dicts
- ❌ No web server (`--serve` placeholder)
- ❌ No error stack traces
- ❌ No line number in runtime errors
- ❌ No module system for multi-file projects
- ❌ No type system
- ❌ No async/await

## 📈 Performance Notes

- **Startup time**: ~200-500ms (includes Python startup)
- **Simple script**: <100ms execution time
- **Fibonacci(20)**: ~1-2 seconds
- **Recursion**: Works well, no tail-call optimization yet

## 🔗 Integration Points

### Planned Web Server Integration

```python
# server.py (v1.1)
app = NovaWebServer()

@app.route('/')
def handle_home(req, res):
    res.send("Hello Nova!")

@app.route('/api/data')  
def handle_api(req, res):
    res.json({'status': 'ok', 'data': [1, 2, 3]})

app.listen(3000)
```

### Future Package Manager

```bash
nova install package-name
nova search keyword
nova publish
```

## 📝 Contributing

To contribute to NovaScript:

1. Create a new branch: `git checkout -b feature/new-feature`
2. Make changes following code style guidelines
3. Add examples demonstrating new features
4. Test thoroughly: `python nova_cli.py examples/test.nova`
5. Commit with descriptive messages
6. Push and create a pull request

## 🎯 Success Metrics

At each version, we measure:

- ✅ **Code Quality**: Type hints, docstrings, comments
- ✅ **Test Coverage**: Examples for each feature
- ✅ **Performance**: Startup time, execution speed
- ✅ **Documentation**: README, examples, comments
- ✅ **Usability**: Clear error messages, helpful CLI

## 📞 Questions?

Refer to:
- [README.md](README.md) - User guide
- [examples/](examples/) - Working code samples
- Source code comments - Implementation details

---

**Version 1.0.0** - Core runtime complete, web framework coming in v1.1
