# NovaScript-X Usage Guide & Tutorial

Comprehensive guide for using NovaScript-X with beginner and advanced tutorials.

---

## Table of Contents

1. [Installation & Setup](#installation--setup)
2. [Beginner Tutorial](#beginner-tutorial)
3. [Intermediate Tutorial](#intermediate-tutorial)
4. [Advanced Tutorial](#advanced-tutorial)
5. [Standard Library Deep Dive](#standard-library-deep-dive)
6. [Advanced Techniques](#advanced-techniques)
7. [Best Practices](#best-practices)
8. [Debugging & Troubleshooting](#debugging--troubleshooting)

---

## Installation & Setup

### 1. Install from PyPI (Recommended)

```bash
pip install novascript-x
```

### 2. Install from Source (Development)

```bash
git clone https://github.com/YourRepo/NovaScript-X
cd NovaScript
pip install -e .
```

### 3. Verify Installation

```bash
novax --version
# Output: NovaScript-X 1.0.0

novax --help
# Shows all available commands
```

---

## Beginner Tutorial

### 1. Your First Program

Create a file named `hello.nova`:

```nova
print("Hello, NovaScript-X!")
```

Run it:

```bash
novax hello.nova
# Output: Hello, NovaScript-X!
```

**What's happening?**
- `print()` displays text to the console
- Strings are enclosed in double quotes

### 2. Variables

Create `variables.nova`:

```nova
# Create variables
var name = "Alice"
var age = 25
var height = 5.8
var active = True

# Display variables
print("Name: " + name)
print("Age: " + age)
print("Height: " + height)
print("Active: " + active)
```

Run it:

```bash
novax variables.nova
```

**Key Points:**
- Use `var` keyword to declare variables
- Variable names are case-sensitive
- Strings use `+` for concatenation
- Numbers and booleans convert automatically

### 3. Arithmetic Operations

Create `math.nova`:

```nova
var a = 10
var b = 3

var sum = a + b
var difference = a - b
var product = a * b
var quotient = a / b
var remainder = a % b

print("Sum: " + sum)
print("Difference: " + difference)
print("Product: " + product)
print("Quotient: " + quotient)
print("Remainder: " + remainder)
```

**Output:**
```
Sum: 13
Difference: 7
Product: 30
Quotient: 3
Remainder: 1
```

### 4. Conditionals (If/Else)

Create `conditionals.nova`:

```nova
var age = 16

if (age >= 18): {
    print("You are an adult")
} else: {
    print("You are a minor")
}

# Output: You are a minor

# Nested conditions
var score = 85

if (score >= 90): {
    print("Grade: A")
} else: {
    if (score >= 80): {
        print("Grade: B")
    } else: {
        if (score >= 70): {
            print("Grade: C")
        } else: {
            print("Grade: F")
        }
    }
}

# Output: Grade: B
```

**Syntax Notes:**
- Use `:` after the condition
- Enclose the block in `{ }`
- Conditions can use: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Use `and`, `or` for compound conditions

### 5. Loops - While

Create `while_loop.nova`:

```nova
var count = 1

while (count <= 5): {
    print("Count: " + count)
    count = count + 1
}

# Output:
# Count: 1
# Count: 2
# Count: 3
# Count: 4
# Count: 5
```

### 6. Loops - For

Create `for_loop.nova`:

```nova
# for (init : condition : update): { body }

for (var i = 1 : i <= 5 : i = i + 1): {
    print("Count: " + i)
}

# Output: Same as while loop above

# Countdown
for (var n = 5 : n > 0 : n = n - 1): {
    print(n)
}
print("Blastoff!")

# Output:
# 5
# 4
# 3
# 2
# 1
# Blastoff!
```

### 7. Functions

Create `functions.nova`:

```nova
# Define a function
function greet(name):
{
    print("Hello, " + name)
}

# Call the function
greet("Alice")
greet("Bob")

# Function with return
function add(a, b):
{
    return a + b
}

var result = add(5, 3)
print("5 + 3 = " + result)

# Output:
# Hello, Alice
# Hello, Bob
# 5 + 3 = 8
```

---

## Intermediate Tutorial

### 1. Recursion

Create `recursion.nova`:

```nova
# Factorial: 5! = 5 * 4 * 3 * 2 * 1 = 120
function factorial(n):
{
    if (n <= 1): {
        return 1
    }
    return n * factorial(n - 1)
}

print("5! = " + factorial(5))
# Output: 5! = 120

# Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13...
function fib(n):
{
    if (n <= 1): {
        return n
    }
    return fib(n - 1) + fib(n - 2)
}

var i = 0
while (i < 10): {
    print(fib(i))
    i = i + 1
}
```

**Key Points:**
- Recursive functions call themselves
- Must have a base case to avoid infinite recursion
- Each recursive call uses the call stack

### 2. Using the Math Module

Create `math_module.nova`:

```nova
var math = require("math")

# Constants
print("Pi: " + math.pi)
print("E: " + math.e)

# Basic math
print("sqrt(16): " + math.sqrt(16))
print("sqrt(2): " + math.sqrt(2))

# Power
print("2^3: " + math.pow(2, 3))
print("2^10: " + math.pow(2, 10))

# Rounding
print("floor(3.7): " + math.floor(3.7))
print("ceil(3.2): " + math.ceil(3.2))
print("round(3.5): " + math.round(3.5))

# Min/Max
print("min(3, 5, 1): " + math.min(3, 5, 1))
print("max(3, 5, 1): " + math.max(3, 5, 1))

# Absolute value
print("abs(-5): " + math.abs(-5))
```

### 3. Using the Random Module

Create `random_module.nova`:

```nova
var random = require("random")

# Random integer between 1 and 6 (like dice)
for (var i = 1 : i <= 10 : i = i + 1): {
    var dice = random.randInt(1, 6)
    print("Roll " + i + ": " + dice)
}

# Random choice from list
# Note: Array support coming in v1.1
```

### 4. Using the File System Module

Create `file_operations.nova`:

```nova
var fs = require("fs")

# Write to a file
fs.writeFile("greeting.txt", "Hello, NovaScript-X!")

# Check if file exists
if (fs.fileExists("greeting.txt")): {
    print("File exists!")
    
    # Read the file
    var content = fs.readFile("greeting.txt")
    print("Content: " + content)
    
    # Delete the file
    fs.deleteFile("greeting.txt")
    print("File deleted")
}
```

Run with:

```bash
novax file_operations.nova
```

### 5. String Operations

Create `strings.nova`:

```nova
var str = "NovaScript"

# String concatenation
var greeting = "Hello, " + str
print(greeting)

# String length (via string methods when available)
var msg = "Length can be calculated"

# Substring extraction (coming in v1.1)

# Case operations
print("Uppercase: " + str)

# String comparison
if (str == "NovaScript"): {
    print("It's NovaScript!")
}

# Numeric string conversion
var num_str = "42"
# Note: Use explicit conversion when needed
```

### 6. Complex Problem: Palindrome Checker

Create `palindrome.nova`:

```nova
# Check if a word is a palindrome
function isPalindrome(text):
{
    var len = text.length()
    var left = 0
    var right = len - 1
    
    while (left < right): {
        if (text.charAt(left) != text.charAt(right)): {
            return False
        }
        left = left + 1
        right = right - 1
    }
    
    return True
}

# Note: String methods will be available in v1.1
# For now, use conceptual approach:

function checkPalindrome(word):
{
    # Simplified version
    if (word == "racecar"): {
        return True
    } else: {
        if (word == "level"): {
            return True
        } else: {
            return False
        }
    }
}

print(checkPalindrome("racecar"))
```

---

## Advanced Tutorial

### 1. Function Composition

Create `function_composition.nova`:

```nova
# Create reusable functions
function double(n):
{
    return n * 2
}

function square(n):
{
    return n * n
}

function addOne(n):
{
    return n + 1
}

# Compose functions
function compose(x):
{
    var result = x
    result = double(result)
    result = addOne(result)
    result = square(result)
    return result
}

# Test
for (var i = 1 : i <= 5 : i = i + 1): {
    var input = i
    var output = compose(input)
    print("compose(" + input + ") = " + output)
}
```

### 2. Algorithm Implementation: Bubble Sort

Create `bubble_sort.nova`:

```nova
function bubbleSort():
{
    # For v1.1 with array support
    # Current version can work with individual variables
    
    var a = 5
    var b = 2
    var c = 8
    var d = 1
    
    # Manual bubble sort
    var temp
    
    # Pass 1
    if (a > b): {
        temp = a
        a = b
        b = temp
    }
    if (b > c): {
        temp = b
        b = c
        c = temp
    }
    if (c > d): {
        temp = c
        c = d
        d = temp
    }
    
    print("Sorted: " + a + ", " + b + ", " + c + ", " + d)
}

bubbleSort()
```

### 3. Performance Testing

Create `performance.nova`:

```nova
function primeCount(n):
{
    var count = 0
    var i = 2
    
    while (i < n): {
        var isPrime = True
        var j = 2
        
        while (j * j <= i): {
            if (i % j == 0): {
                isPrime = False
            }
            j = j + 1
        }
        
        if (isPrime): {
            count = count + 1
        }
        
        i = i + 1
    }
    
    return count
}

# Count primes up to 100
var primes = primeCount(100)
print("Primes up to 100: " + primes)
```

### 4. Multi-Module Integration

Create `integration.nova`:

```nova
var math = require("math")
var fs = require("fs")
var random = require("random")
var date = require("date")

# Create a data log
var log = "NovaScript Integration Test\n"
var timestamp = date.now()
log = log + "Time: " + timestamp + "\n"

# Generate random data
var random_num = random.randInt(1, 100)
log = log + "Random Number: " + random_num + "\n"

# Calculate something
var sqrt_result = math.sqrt(random_num)
log = log + "Square Root: " + sqrt_result + "\n"

# Save to file
fs.writeFile("log.txt", log)

# Read and display
var content = fs.readFile("log.txt")
print(content)
```

---

## Standard Library Deep Dive

### Math Module Complete Reference

```nova
var math = require("math")

# Constants
print(math.pi)          # 3.141592653589793
print(math.e)           # 2.718281828459045
print(math.tau)         # 6.283185307179586 (2π)
print(math.inf)         # Infinity
print(math.nan)         # Not a number

# Arithmetic
print(math.abs(-5))     # 5
print(math.sqrt(16))    # 4.0
print(math.pow(2, 8))   # 256
print(math.min(3, 1, 4, 1, 5))  # 1
print(math.max(3, 1, 4, 1, 5))  # 5

# Rounding
print(math.floor(3.7))  # 3
print(math.ceil(3.2))   # 4
print(math.round(3.5))  # 4

# Trigonometry (radians)
print(math.sin(0))      # 0.0
print(math.cos(0))      # 1.0
print(math.tan(0))      # 0.0
```

### File System Module Complete Reference

```nova
var fs = require("fs")

# Write file
fs.writeFile("file.txt", "Content")

# Read file
var content = fs.readFile("file.txt")

# Append to file
fs.appendFile("file.txt", "\nMore content")

# Check existence
if (fs.fileExists("file.txt")): {
    print("Exists")
}

# Delete file
fs.deleteFile("file.txt")

# List directory
var files = fs.listDirectory(".")

# Create directory
fs.mkdir("my_directory")
```

### Console Module Complete Reference

```nova
var console = require("console")

console.log("Normal log message")
console.info("Info message")
console.warn("Warning message")
console.error("Error message")
console.debug("Debug message")
```

### Random Module Complete Reference

```nova
var random = require("random")

# Seed for reproducible results
random.seed(42)

# Random integers (inclusive)
var n = random.randInt(1, 100)

# Random float [0, 1)
var f = random.randFloat()

# Random choice from values
var choice = random.choice([1, 2, 3, 4, 5])

# Shuffle (for arrays in v1.1)
```

### Date Module Complete Reference

```nova
var date = require("date")

# Current timestamp (seconds since epoch)
var now = date.now()

# Get date parts
var year = date.getYear()
var month = date.getMonth()
var day = date.getDay()
var hour = date.getHour()
var minute = date.getMinute()
var second = date.getSecond()

# Format date
var formatted = date.format("YYYY-MM-DD HH:MM:SS")

# Add days
var tomorrow = date.addDays(1)
var next_week = date.addDays(7)

# Add hours
var later = date.addHours(2)

# Add minutes
var soon = date.addMinutes(30)
```

### HTTP Module Complete Reference

```nova
var http = require("http")

# GET request
var response_get = http.get("https://api.example.com/endpoint")

# POST request
var body = "{\"key\": \"value\"}"
var response_post = http.post("https://api.example.com/endpoint", body)

# PUT request
var response_put = http.put("https://api.example.com/endpoint/1", body)

# DELETE request
var response_delete = http.delete("https://api.example.com/endpoint/1")

# Headers (coming in v1.1)
```

---

## Advanced Techniques

### 1. Error Handling Patterns

Create `error_handling.nova`:

```nova
function safeRead(filename):
{
    # For now, use defensive programming
    # Try/catch coming in v1.1
    
    var fs = require("fs")
    
    if (fs.fileExists(filename)): {
        return fs.readFile(filename)
    } else: {
        print("Error: File not found")
        return None
    }
}

var content = safeRead("data.txt")
```

### 2. Module Encapsulation

Create `calculator.nova`:

```nova
# Create a simple calculator module

function createCalculator():
{
    # Closure-like pattern
    var memory = 0
    
    function add(x):
    {
        memory = memory + x
        return memory
    }
    
    function subtract(x):
    {
        memory = memory - x
        return memory
    }
    
    function getMemory():
    {
        return memory
    }
    
    # Simulate module export
    return memory
}

var result = createCalculator()
print("Result: " + result)
```

### 3. Complex Algorithms: Binary Search

Create `binary_search.nova`:

```nova
function binarySearch(target):
{
    # Simulated sorted array via manual indexing
    # Real array support coming in v1.1
    
    var low = 0
    var high = 9
    var mid
    var found = False
    var iterations = 0
    
    while (low <= high): {
        mid = (low + high) / 2
        iterations = iterations + 1
        
        # Would compare array[mid] vs target
        # Simulation: searching for 5 in [0-9]
        
        if (mid == target): {
            found = True
        } else: {
            if (mid < target): {
                low = mid + 1
            } else: {
                high = mid - 1
            }
        }
    }
    
    print("Found: " + found)
    print("Iterations: " + iterations)
}

binarySearch(5)
```

---

## Best Practices

### 1. Naming Conventions

```nova
# Good: Clear, descriptive names
var userName = "Alice"
var userAge = 30
var isActive = True

function calculateTotalPrice(basePrice, taxRate):
{
    return basePrice * (1 + taxRate)
}

# Avoid: Unclear names
var un = "Alice"        # Too short
var a = 30              # Ambiguous
var x = True            # Non-descriptive

function calc(p, t):    # What does this do?
{
    return p * (1 + t)
}
```

### 2. Code Organization

```nova
# Good: Organize code in logical sections

# ============================================
# CONSTANTS
# ============================================
var TAX_RATE = 0.08
var MAX_RETRIES = 3

# ============================================
# HELPER FUNCTIONS
# ============================================
function calculateTax(amount):
{
    return amount * TAX_RATE
}

# ============================================
# MAIN LOGIC
# ============================================
var price = 100
var tax = calculateTax(price)
var total = price + tax

print("Total: " + total)
```

### 3. Error Prevention

```nova
# Good: Check conditions before using values
var fs = require("fs")

if (fs.fileExists("data.txt")): {
    var data = fs.readFile("data.txt")
    # Process data
} else: {
    print("Warning: File not found, using defaults")
}

# Good: Validate function inputs
function divide(a, b):
{
    if (b == 0): {
        print("Error: Division by zero")
        return None
    }
    return a / b
}
```

### 4. Performance Tips

```nova
# Good: Avoid redundant calculations
var math = require("math")
var sqrt_2 = math.sqrt(2)

for (var i = 1 : i <= 1000 : i = i + 1): {
    var result = i * sqrt_2  # Reuse calculated value
}

# Avoid: Recalculating in loop
# for (var i = 1 : i <= 1000 : i = i + 1): {
#     var result = i * math.sqrt(2)  # Wasteful!
# }
```

---

## Debugging & Troubleshooting

### 1. Debug Output

Create `debug.nova`:

```nova
var value = 42

# Print to trace execution
print("Starting calculation")
print("Value: " + value)

var result = value * 2
print("After doubling: " + result)

print("Finished")
```

Run with:

```bash
novax debug.nova
```

### 2. Using Conditional Debugging

```nova
var DEBUG = True

function debugLog(message):
{
    if (DEBUG): {
        print("[DEBUG] " + message)
    }
}

debugLog("Starting process")
var x = 10
debugLog("x = " + x)
```

### 3. Common Errors and Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `Unexpected token: DOT` | Member access not recognized | Update to latest version |
| `NameError: Undefined variable: x` | Variable used before declaration | Use `var x = value` first |
| `TypeError: ... is not a function` | Calling non-existent function | Check function name spelling |
| `SyntaxError: Expected :` | Missing colon after if/while | Add `:` after condition |
| `File not found` | Invalid file path | Check file exists, use correct path |

### 4. Testing Your Code

Create `test.nova`:

```nova
# Test arithmetic
var sum = 5 + 3
if (sum == 8): {
    print("✓ Addition works")
} else: {
    print("✗ Addition failed")
}

# Test functions
function multiply(a, b):
{
    return a * b
}

if (multiply(3, 4) == 12): {
    print("✓ Multiply works")
} else: {
    print("✗ Multiply failed")
}

# Test modules
var math = require("math")
if (math.sqrt(4) == 2): {
    print("✓ Math module works")
} else: {
    print("✗ Math module failed")
}
```

---

## Conclusion

You now have the knowledge to:
- Write basic NovaScript programs
- Use functions and control flow
- Leverage the standard library modules
- Apply advanced programming techniques
- Debug and optimize your code

For more information:
- Check [README.md](README.md) for quick reference
- Explore [examples/](examples/) directory
- Review [DEVELOPMENT.md](DEVELOPMENT.md) for architecture

**Happy coding! 🚀**
