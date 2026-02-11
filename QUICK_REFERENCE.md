# NovaScript Quick Reference Guide

A quick reference for NovaScript syntax and CLI usage.

## 📋 Table of Contents

- [CLI Commands](#cli-commands)
- [Language Syntax](#language-syntax)
- [Operators](#operators)
- [Built-in Functions](#built-in-functions)
- [Standard Library](#standard-library)
- [Common Patterns](#common-patterns)

---

## 🖥️ CLI Commands

### Basic Usage

```bash
# Execute a file
nova script.nova

# Interactive REPL
nova

# Run code inline
nova -c 'print(5 + 3)'

# Watch mode (auto-run on changes)
nova --watch script.nova
nova -w script.nova

# Debug mode (shows parse tree)
nova --debug script.nova

# Show version
nova --version
nova -v

# Show help
nova --help
nova -h
```

### Options

```bash
nova [options] [file]

Options:
  -h, --help            Show help message
  -v, --version         Show version
  -c CODE, --code CODE  Execute code string
  -d, --debug           Enable debug mode
  -w, --watch FILE      Watch file for changes and rerun
```

---

## 💻 Language Syntax

### Variables

```nova
var x = 10;
var name = "Alice";
var result = x + 5;
```

### Functions

```nova
function add(a, b) {
    return a + b;
}

var sum = add(5, 3);        # 8

# Recursive functions
function factorial(n) {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}
```

### Control Flow

```nova
# If/Else
if (x > 0) {
    print("positive");
} else {
    print("non-positive");
}

# While loop
var i = 0;
while (i < 5) {
    print(i);
    i = i + 1;
}

# For loop
for (i = 0; i < 5; i = i + 1) {
    print(i * 2);
}
```

### Comments

```nova
# This is a comment
var x = 10;  # inline comment
```

### Strings

```nova
var msg = "Hello World";
var greeting = "Hi " + name;  # Concatenation
```

---

## 🧮 Operators

### Arithmetic

| Operator | Example | Result |
|----------|---------|--------|
| `+` | `5 + 3` | `8` |
| `-` | `5 - 3` | `2` |
| `*` | `5 * 3` | `15` |
| `/` | `6 / 3` | `2` |
| `%` | `5 % 3` | `2` |

### Comparison

| Operator | Example | Result |
|----------|---------|--------|
| `==` | `5 == 5` | `true` |
| `!=` | `5 != 3` | `true` |
| `<` | `3 < 5` | `true` |
| `>` | `5 > 3` | `true` |
| `<=` | `3 <= 5` | `true` |
| `>=` | `5 >= 3` | `true` |

### Logical

| Operator | Example | Result |
|----------|---------|--------|
| `and` | `true and false` | `false` |
| `or` | `true or false` | `true` |
| `!` | `!true` | `false` |

### Assignment

| Operator | Example |
|----------|---------|
| `=` | `x = 10` |
| `=` (reassign) | `x = x + 1` |

---

## 🔧 Built-in Functions

### I/O

```nova
print(value);              # Print to stdout
print("Hello", "World");   # Multiple arguments
```

### Type Checking

```nova
type(x);                   # Returns type as string
                           # "number", "string", "function", etc.
```

### Conversion

```nova
string(42);                # "42"
number("42");              # 42
```

### Module Loading

```nova
var module = require("module_name");
var fs = require("fs");
var math = require("math");
var console = require("console");
```

---

## 📚 Standard Library

### `fs` - File System

```nova
var fs = require("fs");

# Read file
var content = fs.readFile("path/to/file.txt");

# Write file (overwrites)
fs.writeFile("output.txt", "content");

# Append to file
fs.appendFile("output.txt", "\nmore content");

# Check if file exists
var exists = fs.fileExists("file.txt");

# Delete file
fs.deleteFile("file.txt");

# List files in directory
var files = fs.listFiles("./");
```

### `console` - Logging

```nova
var console = require("console");

console.log("Regular message");          # [LOG]
console.warn("Warning message");         # [WARN]
console.error("Error message");          # [ERROR]
console.info("Info message");            # [timestamp]
console.debug("Debug info");             # [DEBUG]
console.clear();                         # Clear terminal
```

### `math` - Math Functions

```nova
var math = require("math");

# Functions
math.sqrt(16);                 # 4
math.pow(2, 3);                # 8
math.abs(-5);                  # 5
math.floor(3.7);               # 3
math.ceil(3.2);                # 4
math.round(3.5);               # 4 (rounds to nearest)
math.sin(angle);               # sine
math.cos(angle);               # cosine
math.tan(angle);               # tangent
math.log(n);                   # natural logarithm
math.exp(n);                   # e^n

# Constants
math.pi;                       # 3.14159...
math.e;                        # 2.71828...
math.tau;                      # 6.28318... (2π)
math.inf;                      # Infinity
math.nan;                      # Not a Number
```

### `random` - Random Numbers

```nova
var random = require("random");

random.random();               # 0.0 to 1.0
random.randInt(1, 10);         # 1 to 10 (inclusive)
random.randFloat();            # 0.0 to 1.0
random.uniform(min, max);      # min to max
random.choice(list);           # Random element from list
random.shuffle(list);          # Shuffle list in place
random.seed(42);               # Set random seed
```

### `date` - Date & Time

```nova
var date = require("date");

date.now();                    # Seconds since epoch
date.nowMs();                  # Milliseconds since epoch
date.format("%Y-%m-%d");       # Format current date
date.getYear();                # Current year
date.getMonth();               # Current month (1-12)
date.getDay();                 # Current day (1-31)
date.getDayOfWeek();           # Day of week (0-6, 0=Sunday)
date.getHour();                # Current hour
date.getMinute();              # Current minute
date.getSecond();              # Current second
date.addDays(n);               # Add n days
date.addHours(n);              # Add n hours
date.fromTimestamp(ts);        # Convert timestamp to date
```

### `http` - HTTP Requests

```nova
var http = require("http");

# GET request
var response = http.get("https://api.example.com/data");

# POST request with JSON
var response = http.post("https://api.example.com/data", {
    name: "value"
});

# PUT request
var response = http.put("https://api.example.com/item/1", {
    name: "updated"
});

# DELETE request
http.delete("https://api.example.com/item/1");

# With custom headers
var response = http.get("https://api.example.com", {
    "Authorization": "Bearer token123"
});
```

---

## 📝 Common Patterns

### Loop Over Numbers

```nova
for (i = 0; i < 10; i = i + 1) {
    print(i);
}
```

### Conditional Logic

```nova
if (x > 100) {
    print("very big");
} else if (x > 50) {
    print("big");
} else if (x > 0) {
    print("small");
} else {
    print("non-positive");
}
```

### Function with Multiple Returns

```nova
function describe(x) {
    if (x < 0) {
        return "negative";
    }
    if (x == 0) {
        return "zero";
    }
    return "positive";
}
```

### Nested Loops

```nova
for (i = 1; i <= 3; i = i + 1) {
    for (j = 1; j <= 3; j = j + 1) {
        print(i * 10 + j);
    }
}
```

### Recursion - Countdown

```nova
function countdown(n) {
    if (n <= 0) {
        print("Blastoff!");
        return;
    }
    print(n);
    countdown(n - 1);
}

countdown(5);  # Prints 5, 4, 3, 2, 1, Blastoff!
```

### Reading and Writing Files

```nova
var fs = require("fs");

# Read
var content = fs.readFile("input.txt");
print(content);

# Write
fs.writeFile("output.txt", "Hello, World!");

# Append
fs.appendFile("output.txt", "\nSecond line");
```

### Processing Data

```nova
var math = require("math");

var numbers = 10;  # Placeholder until arrays are supported
var total = 0;
var count = 0;

function add_to_total(n) {
    total = total + n;
    count = count + 1;
}

add_to_total(5);
add_to_total(15);
add_to_total(20);

var average = total / count;  # 13.33...
print(average);
```

---

## ⚠️ Current Limitations (v1.0)

These features are **NOT** yet supported:
- ❌ Arrays: `[1, 2, 3]`
- ❌ Objects: `{key: value}`
- ❌ Member access: `math.sqrt()` (workaround: use `var sqrt = require("math").sqrt`)
- ❌ Try/catch error handling
- ❌ Classes and OOP
- ❌ Async/await
- ❌ Imports (use `require()` instead)
- ❌ String templates
- ❌ Multiple files

These are planned for v1.1+. See [ROADMAP.md](ROADMAP.md) for details.

---

## 📖 Examples

Comprehensive examples are in the `examples/` directory:

- `examples/hello_world/` - Basic variables and print
- `examples/functions_loops/` - Functions, loops, recursion
- `examples/stdlib_demo/` - Using require() and modules

Run them with:
```bash
nova examples/hello_world/main.nova
nova examples/functions_loops/main.nova
nova examples/stdlib_demo/main.nova
```

---

## 🔍 Debugging

### Debug Mode

```bash
nova --debug script.nova
```

Shows:
- Tokens from lexer
- AST from parser
- Execution steps

### Manual Debugging

```nova
# Print variables
print("x = ", x);
print("type of x: ", type(x));

# Print in functions
function myFunc(param) {
    print("myFunc called with:", param);
    return param * 2;
}
```

### Testing Code Snippets

```bash
# Test one-liners
nova -c 'var x = 5; print(x * 2);'

# Test files incrementally
nova script.nova
```

---

## 📚 More Resources

- [README.md](README.md) - Full documentation
- [DEVELOPMENT.md](DEVELOPMENT.md) - Architecture and development
- [ROADMAP.md](ROADMAP.md) - Future features and timeline
- [CONTRIBUTING.md](CONTRIBUTING.md) - How to contribute

---

**Version 1.0.0** - Quick Reference Generated February 2026
