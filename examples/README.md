# NovaScript Examples

This directory contains example NovaScript programs demonstrating language features and capabilities.

## Running Examples

After installing NovaScript via `pip install .`, you can run examples:

```bash
# Hello World example
nova examples/hello_world/main.nova

# Functions, loops, and recursion
nova examples/functions_loops/main.nova

# Standard library demo (once implemented)
nova examples/stdlib_demo/main.nova

# Watch mode - auto-run when file changes
nova --watch examples/hello_world/main.nova

# Interactive REPL
nova
```

## Example List

### 1. hello_world/
**File**: `main.nova`

A simple introduction to NovaScript covering:
- Print statements
- Variables
- String concatenation
- Basic arithmetic

**Run**: `nova examples/hello_world/main.nova`

### 2. functions_loops/
**File**: `main.nova`

Comprehensive example showing:
- Function definitions with parameters
- Return statements
- For loops with conditions
- While loops
- Recursion (factorial, fibonacci)
- Conditional logic (if/else chains)
- Nested loops (multiplication table)

**Run**: `nova examples/functions_loops/main.nova`

### 3. stdlib_demo/ (Coming Soon)
**File**: `main.nova`

Will demonstrate standard library modules:
- `fs` - File system operations
- `math` - Mathematical functions
- `random` - Random number generation
- `console` - Logging
- `date` - Date/time operations
- `http` - HTTP requests

**Features to add**:
- `require()` function integration
- Module loading from stdlib
- Example for each stdlib module

## Creating Your Own Examples

To create a new example:

1. Create a directory: `examples/your_example/`
2. Create `main.nova` with your code
3. Run: `nova examples/your_example/main.nova`

## Tips

- Use `--debug` flag for verbose output: `nova --debug examples/hello_world/main.nova`
- Use `--watch` flag to auto-run on file changes: `nova -w examples/hello_world/main.nova`
- Use `-c` to run code directly: `nova -c 'print("Hello from CLI")' `
- Start interactive REPL with: `nova`

## Next Features

Upcoming features to be demonstrated:
- Web server with routing (`--serve`)
- Standard library requi re() integration
- Web framework with `nova create`
- Template rendering
- API development
