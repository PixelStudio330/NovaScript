# NovaScript - A Lightweight Programming Language Runtime

A Python-based interpreter for the NovaScript programming language, designed as a modern, lightweight alternative to Node.js. Write full-stack applications with a unified language runtime.

**Current Version**: 1.0.0  
**Status**: Beta (Core language features complete, web runtime in development)

## 🚀 Quick Start

### Installation

Install NovaScript globally via pip:

```bash
# Clone or navigate to the NovaScript directory
cd NovaScript

# Install in development mode (creates 'nova' command)
pip install -e .

# Or install from current directory
pip install .
```

After installation, the `nova` command will be available globally on your system.

### Run Your First Program

Create a file called `hello.nova`:

```nova
print("Hello, Nova!")

var name = "World"
print("Welcome to " + name)
```

Run it:

```bash
nova hello.nova
```

### Interactive REPL

Start the interactive interpreter:

```bash
nova
```

Type NovaScript code and see results instantly:

```
nova> var x = 10
nova> print(x + 5)
15
nova> exit
```

## 📖 Language Features

### Variables

```nova
var name = "Alice"
var age = 25
var pi = 3.14159
```

### Functions

```nova
function greet(person):
{
    print("Hello, " + person)
}

greet("Bob")

function add(a, b):
{
    return a + b
}

var sum = add(3, 5)
```

### Control Flow

```nova
# If / Else
if (age >= 18): {
    print("Adult")
} else: {
    print("Minor")
}

# While loop
var count = 0
while (count < 5): {
    print(count)
    count = count + 1
}

# For loop
for (var i = 1 : i <= 5 : i = i + 1): {
    print("Number: " + i)
}
```

### Operators

- **Arithmetic**: `+`, `-`, `*`, `/`, `%`
- **Comparison**: `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Logical**: `and`, `or`, `!`

### Advanced Features

- **Recursion**
- **String concatenation** with automatic type coercion
- **Comments** with `#`

## 🛠️ CLI Commands

The `nova` command supports various options:

### Run a Script

```bash
nova script.nova
```

### Interactive REPL

```bash
nova
```

### Watch Mode (Auto-run on Changes)

```bash
nova --watch script.nova
# or
nova -w script.nova
```

### Execute Code Inline

```bash
nova -c 'print("Hello Nova")'
```

### Debug Mode

```bash
nova --debug script.nova
```

### Show Version

```bash
nova --version
# or
nova -v
```

### Display Help

```bash
nova --help
# or
nova -h
```

## 📦 Standard Library (In Development)

NovaScript includes a standard library for common tasks. Import modules using `require()`:

### Available Modules

#### `fs` - File System

```nova
var fs = require("fs")

# Write to file
fs.writeFile("test.txt", "Hello")

# Read from file
var content = fs.readFile("test.txt")

# Check if file exists
if (fs.fileExists("test.txt")): {
    print("File exists")
}
```

#### `console` - Logging

```nova
var console = require("console")

console.log("Regular message")
console.warn("Warning!")
console.error("Error occurred")
console.info("Info")
console.debug("Debug message")
```

#### `math` - Mathematics

```nova
var math = require("math")

print(math.sqrt(16))        # 4.0
print(math.pow(2, 3))       # 8
print(math.abs(-5))         # 5
print(math.floor(4.7))      # 4
print(math.pi)              # 3.14159...
```

#### `random` - Random Numbers

```nova
var random = require("random")

var n = random.randInt(1, 100)      # Random int 1-100
var f = random.randFloat()           # Random 0.0-1.0
```

#### `date` - Date/Time

```nova
var date = require("date")

print(date.now())           # Current timestamp
print(date.format("%Y-%m-%d"))   # Formatted date
print(date.addDays(5))      # Date 5 days from now
```

#### `http` - HTTP Requests

```nova
var http = require("http")

# GET request
var response = http.get("https://api.example.com/data")

# POST request
var result = http.post("https://api.example.com", {key: "value"})
```

## 📂 Project Structure

```
nova/
├── __init__.py              # Package initialization
├── interpreter.py           # Core language interpreter
│   ├── Lexer              # Tokenizes source code
│   ├── Parser             # Builds AST
│   └── Executor           # Executes code
└── stdlib/                  # Standard library
    ├── fs.py              # File system
    ├── console.py         # Logging
    ├── math.py            # Math functions
    ├── random.py          # Random numbers
    ├── date.py            # Date/time
    └── http.py            # HTTP requests

nova_cli.py                 # Command-line interface
setup.py                    # Installation configuration
examples/                   # Example programs
```

## 🚀 Examples

See the `examples/` directory for complete working programs:

1. **hello_world/** - Basic variables and printing
2. **functions_loops/** - Functions, loops, recursion, and conditions

Run examples:

```bash
nova examples/hello_world/main.nova
nova examples/functions_loops/main.nova
```

## 🔧 Features & Roadmap

### ✅ Completed (v1.0)

- [x] Core language interpreter (Lexer, Parser, Executor)
- [x] CLI with argparse support
- [x] Watch mode for development
- [x] Standard library modules (fs, console, math, random, date, http)
- [x] REPL mode
- [x] Cross-platform (Windows, macOS, Linux)
- [x] pip installation support

### 🚧 In Development

- [ ] `require()` function for module imports
- [ ] Web server/HTTP routing support
- [ ] Web framework with `nova create` scaffold
- [ ] Server-side rendering
- [ ] Hot reloading

### 📋 Planned (v1.1+)

- [ ] Array/List support
- [ ] Object/Dictionary support
- [ ] Classes and OOP
- [ ] Async/await
- [ ] Package manager
- [ ] Type system
- [ ] Testing framework
- [ ] Build tools

## 🎓 Tutorial & Documentation

### Your First Program

Create `script.nova`:

```nova
# Variables and printing
var greeting = "Welcome to NovaScript"
print(greeting)

# Functions
function multiply(a, b):
{
    return a * b
}

# Using the function
var result = multiply(6, 7)
print("6 * 7 = " + result)

# Loops
for (var i = 1 : i <= 3 : i = i + 1): {
    print("Iteration " + i)
}
```

Run it:

```bash
nova script.nova
```

### Conditionals

```nova
var score = 85

if (score >= 90): {
    print("Grade A")
} else: {
    if (score >= 80): {
        print("Grade B")
    } else: {
        print("Grade C")  
    }
}
```

### Recursion

```nova
# Calculate factorial
function factorial(n):
{
    if (n <= 1): {
        return 1
    }
    return n * factorial(n - 1)
}

print(factorial(5))  # 120
```

## 🔌 Web Runtime (Coming Soon)

In future versions, run NovaScript as an HTTP server:

```bash
# Start web server
nova --serve app.nova

# app.nova
function handleRequest(req, res):
{
    res.send("Hello from NovaScript!")
}
```

## 🐛 Troubleshooting

### Command not found: nova

Make sure you installed NovaScript:

```bash
pip install -e .
```

Verify installation:

```bash
which nova
nova --version
```

### Import errors

Make sure you're in the correct directory and the nova package is properly installed:

```bash
pip install -e .
python -c "import nova; print(nova.__version__)"
```

### File not found

Use absolute paths or relative paths from your current directory:

```bash
# Absolute path
nova /full/path/to/script.nova

# Relative path
nova ./scripts/script.nova
```

## 📄 License

MIT License - See LICENSE file for details

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## 📞 Support

For issues and questions:
- Open an issue on GitHub
- Check documentation in `examples/` directory
- Review test files in `tests/` directory

## 🎉 Acknowledgments

NovaScript is inspired by Node.js, Python, and JavaScript, bringing together the best features of modern runtimes into a lightweight, easy-to-learn language.

## Features

- **Variables**: Declare variables with `var`
- **Functions**: Create functions with `function` keyword and `return` statements
- **Print**: Output values with `print()`
- **Conditionals**: `if`/`else` statements with boolean logic
- **Loops**: `while` and `for` loops
- **Arithmetic**: Full arithmetic operations (+, -, *, /, %)
- **String Concatenation**: Use `+` operator to concatenate strings
- **Operators**: Comparison (==, !=, <, >, <=, >=), logical (and, or), unary (!, -)

## Usage

### Running a NovaScript File

```bash
python nova_interpreter.py program.nova
```

### Interactive REPL Mode

```bash
python nova_interpreter.py
```

Then type NovaScript commands at the `nova>` prompt. Type `exit` to quit.

## Syntax

### Variables

```nova
var name = value
var x = 10
var greeting = "Hello"
```

### Functions

```nova
function functionName(param1, param2):
{
    # Function body
    return result
}
```

Example:
```nova
function add(a, b):
{
    return a + b
}

var result = add(5, 3)
print("Result: " + result)  # Output: Result: 8
```

### Print Statement

```nova
print("Hello, World")
print("Value: " + x)
print("Sum: " + (5 + 3))
```

### Conditionals

```nova
if (condition): {
    # Then body
} else: {
    # Else body
}
```

Example:
```nova
var age = 25
if (age >= 18): {
    print("Adult")
} else: {
    print("Minor")
}
```

### While Loop

```nova
while (condition): {
    # Loop body
}
```

Example:
```nova
var count = 1
while (count <= 3): {
    print("Count: " + count)
    count = count + 1
}
```

### For Loop

```nova
for (init : condition : update): {
    # Loop body
}
```

Example:
```nova
for (var i = 1 : i <= 5 : i = i + 1): {
    print("i = " + i)
}
```

### Arithmetic Operators

- `+`: Addition and string concatenation
- `-`: Subtraction
- `*`: Multiplication
- `/`: Division (integer division for integers)
- `%`: Modulo

### Comparison Operators

- `==`: Equal to
- `!=`: Not equal to
- `<`: Less than
- `>`: Greater than
- `<=`: Less than or equal to
- `>=`: Greater than or equal to

### Logical Operators

- `and`: Logical AND
- `or`: Logical OR
- `!`: Logical NOT

### Comments

```nova
# This is a comment
```

## Interpreter Architecture

The interpreter is modular with three main components:

1. **Lexer**: Tokenizes NovaScript source code
   - Recognizes keywords, operators, literals, and identifiers
   - Handles string literals with escape sequences
   - Produces a stream of Token objects

2. **Parser**: Parses tokens into an abstract syntax tree (AST)
   - Implements recursive descent parsing with operator precedence
   - Produces a list of statement dictionaries
   - Handles all NovaScript language constructs

3. **Executor**: Executes the parsed AST
   - Manages global and local scope
   - Evaluates expressions and executes statements
   - Handles function calls and returns

## Example Program

```nova
# Variables
var name = "NovaScript"
print("Language: " + name)

# Functions
function greet(person):
{
    print("Hello, " + person)
}

greet("World")

# Fibonacci with recursion
function fibonacci(n):
{
    if (n <= 1): {
        return n
    }
    return fibonacci(n - 1) + fibonacci(n - 2)
}

print("Fibonacci(7) = " + fibonacci(7))

# Loops
for (var i = 1 : i <= 5 : i = i + 1): {
    var square = i * i
    print("Square of " + i + " = " + square)
}

# Conditionals
var score = 85
if (score >= 90): {
    print("Grade: A")
} else: {
    if (score >= 80): {
        print("Grade: B")
    } else: {
        print("Grade: C")
    }
}
```

## Project File Structure

### Core Interpreter
- **[nova_interpreter.py](nova_interpreter.py)** (893 lines)
  - `Lexer` class: Tokenizes source code, handles keywords, operators, strings, numbers
  - `Parser` class: Recursive descent parser, builds abstract syntax tree (AST)
  - `Executor` class: Executes AST, manages scopes, evaluates expressions
  - REPL mode for interactive execution

### Web IDE Backend
- **[server.py](server.py)** (152 lines)
  - Flask web server configuration
  - `GET /` route: Serves the IDE interface (index.html)
  - `POST /api/execute` route: Receives code, executes it, captures output, returns JSON
  - `GET /api/highlight-keywords` route: Returns language keywords for syntax highlighting
  - Error handling and output capture with `io.StringIO`

### Web IDE Frontend
- **[templates/index.html](templates/index.html)**
  - CodeMirror 5 editor integration for syntax highlighting
  - Dark theme styling
  - Output console for displaying results
  - Buttons: Run Code (Ctrl+Enter), Clear, Reset
  - AJAX communication with Flask backend

- **[static/style.css](static/style.css)** (700+ lines)
  - Professional dark theme (GitHub dark mode inspired)
  - CSS variables for theming and layout control
  - Responsive grid layout (editor + console)
  - Terminal-style console output styling

- **[static/script.js](static/script.js)** (300+ lines)
  - CodeMirror editor initialization and configuration
  - AJAX request/response handling for code execution
  - Console message formatting and display
  - Event listeners for Run, Clear, Reset buttons
  - Keyboard shortcuts (Ctrl+Enter to run)

### Configuration Files
- **requirements.txt**: Python dependencies (Flask==2.3.3, Werkzeug==2.3.7)
- **test.nova**: Sample NovaScript program for testing

## Extending the Interpreter

The modular design makes it easy to add new features:

1. **Add Keywords**: Add to `Lexer.KEYWORDS` and create a parse method
2. **Add Operators**: Extend the binary/unary operator parsing and evaluation
3. **Add Data Types**: Add new value types to the executor
4. **Add Built-in Functions**: Add to the executor for built-in functions

## Limitations

- Requires braces for multi-statement blocks (indentation-based syntax can be added)
- No array/list support yet (can be added)
- No object/dictionary support yet (can be added)
- No file I/O support yet (can be added)
- No module/import system yet (can be added)

## Error Handling

The interpreter provides helpful error messages:
- Syntax errors from the lexer and parser
- Runtime errors from the executor
- Type errors for invalid operations
- Name errors for undefined variables/functions
