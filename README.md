# NovaScript Interpreter

A Python-based interpreter for the NovaScript programming language with support for variables, functions, loops, conditionals, and arithmetic operations.

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
