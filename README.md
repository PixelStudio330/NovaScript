# NovaScript-X - A Lightweight Programming Language Runtime

A Python-based interpreter for the NovaScript programming language, designed as a modern, lightweight alternative to Node.js. Write full-stack applications with a unified language runtime.

**Package Name**: `novascript-x`  
**CLI Command**: `novax`  
**Current Version**: 1.0.0  
**Status**: Beta (Core language features complete, web runtime in development)  
**License**: MIT

---

## Table of Contents

1. [Quick Start](#-quick-start)
2. [Getting Started](#-getting-started)
3. [Language Features](#-language-features)
4. [CLI Commands](#️-cli-commands)
5. [Standard Library](#-standard-library)
6. [Examples](#-examples)
7. [Troubleshooting](#-troubleshooting)
8. [Project Structure](#-project-structure)
9. [Contributing](#-contributing)

---

## 🚀 Quick Start

### Installation

```bash
# From PyPI (recommended)
pip install novascript-x

# Or from source (development mode)
git clone https://github.com/YourRepo/NovaScript-X.git
cd NovaScript
pip install -e .
```

### Your First Program

Create `hello.nova`:

```nova
var name = "World"
print("Hello, " + name)
```

Run it:

```bash
novax hello.nova
# Output: Hello, World
```

### Interactive REPL

Start an interactive session:

```bash
novax
# nova> var x = 10
# nova> print(x * 2)
# 20
# nova> exit
```

---

## 📚 Getting Started

### 1. Variables and Basic Operations

```nova
# Declare variables with var
var name = "Alice"
var age = 30
var score = 95.5
var active = True

# Arithmetic operations
var sum = 10 + 5
var product = 4 * 3
var result = 20 / 4

# String concatenation
var message = "Hello, " + name
print(message)

# Output: Hello, Alice
```

### 2. Control Flow - If/Else

```nova
var temperature = 25

if (temperature > 30): {
    print("It's hot!")
} else: {
    if (temperature > 15): {
        print("It's pleasant")
    } else: {
        print("It's cold")
    }
}

# Output: It's pleasant
```

### 3. Loops - While

```nova
var countdown = 3

while (countdown > 0): {
    print(countdown)
    countdown = countdown - 1
}

print("Blastoff!")

# Output:
# 3
# 2
# 1
# Blastoff!
```

### 4. Loops - For

```nova
for (var i = 1 : i <= 5 : i = i + 1): {
    print("Iteration: " + i)
}

# Output:
# Iteration: 1
# Iteration: 2
# Iteration: 3
# Iteration: 4
# Iteration: 5
```

### 5. Functions

```nova
function greet(name, title):
{
    print("Hello, " + title + " " + name)
}

greet("Smith", "Dr")
# Output: Hello, Dr Smith

function add(a, b):
{
    return a + b
}

var total = add(5, 3)
print("Total: " + total)
# Output: Total: 8
```

### 6. Recursion

```nova
function factorial(n):
{
    if (n <= 1): {
        return 1
    }
    return n * factorial(n - 1)
}

print("5! = " + factorial(5))
# Output: 5! = 120
```

### 7. Using the Standard Library

```nova
# Math operations
var math = require("math")
print(math.sqrt(16))          # 4.0
print(math.sqrt(25))          # 5.0
print(math.pow(2, 3))         # 8
print(math.abs(-5))           # 5
print(math.pi)                # 3.14159...

# File operations
var fs = require("fs")
fs.writeFile("greeting.txt", "Hello, NovaScript!")
var content = fs.readFile("greeting.txt")
print(content)

# Random numbers
var random = require("random")
var dice = random.randInt(1, 6)
print("Dice roll: " + dice)

# Date/time
var date = require("date")
var now = date.now()
print("Current timestamp: " + now)
```

---

## 📖 Language Features

### Data Types

- **Numbers**: `10`, `3.14`, `-5`
- **Strings**: `"hello"`, `'world'`
- **Booleans**: `True`, `False`
- **Null**: `None` (nil value)

### Operators

#### Arithmetic
- `+` Addition / String concatenation
- `-` Subtraction
- `*` Multiplication
- `/` Division
- `%` Modulo (remainder)

#### Comparison
- `==` Equal to
- `!=` Not equal to
- `<` Less than
- `>` Greater than
- `<=` Less than or equal to
- `>=` Greater than or equal to

#### Logical
- `and` Logical AND
- `or` Logical OR
- `!` Logical NOT

### Comments

```nova
# This is a comment
# Everything after # is ignored
```

### Advanced Features

- **Member Access**: `math.sqrt(16)` (for module functions)
- **Recursion**: Functions can call themselves
- **Type Coercion**: Automatic type conversion in string concatenation

---

## 🛠️ CLI Commands

### Run a Script

```bash
novax script.nova
```

### Interactive REPL

```bash
novax
# or
novax --repl
```

### Watch Mode (Auto-reload)

```bash
novax --watch script.nova
# or
novax -w script.nova

# Now the script re-runs whenever you save it
```

### Run Code Inline

```bash
novax -c 'print("Hello from NovaScript-X")'
```

### Debug Mode

```bash
novax --debug script.nova
```

### Show Version

```bash
novax --version
# or
novax -v

# Output: NovaScript-X 1.0.0
```

### Display Help

```bash
novax --help
# or
novax -h
```

---

## 📦 Standard Library

NovaScript includes a comprehensive standard library for common tasks.

### Math Module

```nova
var math = require("math")

# Constants
print(math.pi)          # 3.14159...
print(math.e)           # 2.71828...

# Functions
print(math.sqrt(16))    # 4.0
print(math.pow(2, 3))   # 8
print(math.abs(-5))     # 5
print(math.floor(3.7))  # 3
print(math.ceil(3.2))   # 4
print(math.round(3.5))  # 4.0

# Trigonometry
print(math.sin(0))      # 0.0
print(math.cos(0))      # 1.0
print(math.tan(0))      # 0.0
```

### File System Module

```nova
var fs = require("fs")

# Write to file
fs.writeFile("output.txt", "Hello, World!")

# Read from file
var content = fs.readFile("output.txt")
print(content)

# Delete file
fs.deleteFile("output.txt")

# Check if file exists
if (fs.fileExists("script.nova")): {
    print("File exists")
}
```

### Console Module

```nova
var console = require("console")

# Logging
console.log("Info message")
console.warn("Warning message")
console.error("Error message")
```

### Random Module

```nova
var random = require("random")

# Random integers
var dice = random.randInt(1, 6)

# Random floating-point
var float = random.randFloat()

# Choose from list
var choice = random.choice([1, 2, 3, 4, 5])

# Set seed for reproducibility
random.seed(42)
```

### Date/Time Module

```nova
var date = require("date")

# Get current timestamp
var now = date.now()

# Format date
var formatted = date.format("YYYY-MM-DD")

# Get year, month, day
var year = date.getYear()
var month = date.getMonth()
var day = date.getDay()

# Add days to a date
var tomorrow = date.addDays(1)
```

### HTTP Module

```nova
var http = require("http")

# GET request
var response = http.get("https://api.example.com/data")

# POST request
var data = http.post("https://api.example.com/data", "{\"key\": \"value\"}")
```

---

## 💡 Examples

### Example 1: Sum Calculator

```nova
function sum(n):
{
    var total = 0
    for (var i = 1 : i <= n : i = i + 1): {
        total = total + i
    }
    return total
}

print("Sum of 1 to 10: " + sum(10))
# Output: Sum of 1 to 10: 55
```

### Example 2: Fibonacci Sequence

```nova
function fibonacci(n):
{
    if (n <= 1): {
        return n
    }
    return fibonacci(n - 1) + fibonacci(n - 2)
}

for (var i = 0 : i < 10 : i = i + 1): {
    print(fibonacci(i))
}

# Output:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
```

### Example 3: File Processing

```nova
var fs = require("fs")

# Create a file with content
fs.writeFile("numbers.txt", "1\n2\n3\n4\n5")

# Read and display
var content = fs.readFile("numbers.txt")
print("File content:")
print(content)
```

### Example 4: Using Multiple Modules

```nova
var math = require("math")
var random = require("random")
var console = require("console")

# Generate random numbers and calculate stats
var num1 = random.randInt(1, 100)
var num2 = random.randInt(1, 100)

var min = math.min(num1, num2)
var max = math.max(num1, num2)

console.log("Number 1: " + num1)
console.log("Number 2: " + num2)
console.log("Minimum: " + min)
console.log("Maximum: " + max)
```

---

## 🐛 Troubleshooting

### Error: "novax: command not found"

**Solution**: Make sure NovaScript-X is installed:

```bash
pip install novascript-x
# or
pip install -e .
```

Verify installation:

```bash
novax --version
```

### Error: "File not found"

**Solution**: Use absolute paths or ensure relative paths are correct:

```bash
# Absolute path
novax /full/path/to/script.nova

# Relative path from current directory
novax ./scripts/script.nova

# Current directory
novax script.nova
```

### Error: "Module not found"

**Solution**: The module name must match. Available modules are:
- `fs` - File system
- `math` - Mathematics
- `console` - Logging
- `random` - Random numbers
- `date` - Date/time
- `http` - HTTP requests

```nova
var fs = require("fs")      # Correct
# var file = require("File")  # Wrong - use "fs"
```

### Error: "Expected X, got Y" (Syntax Error)

**Solution**: Check your syntax carefully:

```nova
# Correct: colons and braces
if (x > 5): {
    print("yes")
}

# Wrong: missing colon
if (x > 5) {
    print("yes")
}

# Wrong: missing braces
if (x > 5):
    print("yes")
```

### Code doesn't run (no output)

**Solution**: Make sure you're printing results:

```nova
var result = 5 + 3
print(result)      # This displays the result

# Without print, nothing is shown:
var result = 5 + 3  # This runs but shows nothing
```

---

## 📂 Project Structure

```
novascriptx/
├── __init__.py              # Package initialization
├── interpreter.py           # Core interpreter (Lexer, Parser, Executor)
├── novascriptx_cli.py       # Command-line interface
└── stdlib/                  # Standard library modules
    ├── __init__.py
    ├── console.py           # Logging/output
    ├── date.py              # Date/time operations
    ├── fs.py                # File system operations
    ├── http.py              # HTTP requests
    ├── math.py              # Math functions
    └── random.py            # Random number generation

examples/
├── hello_world/
│   └── main.nova
├── functions_loops/
│   └── main.nova
└── stdlib_demo/
    └── main.nova

templates/                   # Web IDE (future)
static/                      # Web IDE assets (future)

setup.py                    # Package configuration
requirements.txt            # Python dependencies
README.md                   # This file
```

---

## 🔌 Web IDE (Coming Soon)

In future versions, NovaScript-X will include a browser-based IDE accessible at `localhost:5000` when running:

```bash
novax --serve
```

---

## 🎓 Next Steps

1. **Explore Examples**: Check the `examples/` directory for more programs
2. **Read the USAGE Guide**: See `USAGE.md` for detailed tutorials
3. **Experiment**: Create your own programs and test them
4. **Share**: Contribute improvements back to the project!

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Quick Contribution Steps

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-feature`
3. Make your changes
4. Test thoroughly
5. Commit with clear messages: `git commit -m "feat: Add new feature"`
6. Push and create a Pull Request

---

## 📝 Development

For developers who want to extend or improve NovaScript-X:

- See [DEVELOPMENT.md](DEVELOPMENT.md) for architecture details
- See [ROADMAP.md](ROADMAP.md) for planned features
- Run tests: `pytest tests/` (when available)

---

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/YourRepo/NovaScript-X/issues)
- **Discussions**: [GitHub Discussions](https://github.com/YourRepo/NovaScript-X/discussions)
- **Documentation**: See [USAGE.md](USAGE.md) and examples/

---

## 📄 License

MIT License - See LICENSE file for full details

Open source software, free to use and modify.

---

## 🎉 Acknowledgments

NovaScript-X is inspired by Node.js, Python, and JavaScript, bringing together the best features of modern runtimes.

**Happy coding! 🚀**
