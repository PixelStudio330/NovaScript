# NovaScript Web IDE - Complete Setup Guide

A fully functional, browser-based integrated development environment (IDE) for the NovaScript programming language.

## Features

✨ **Modern Web Editor**
- Clean, professional dark-themed interface
- Syntax highlighting for NovaScript code
- Line numbers and automatic indentation
- CodeMirror integration for smooth editing experience

🚀 **Real-time Code Execution**
- Execute NovaScript code directly from the browser
- Instant output display in built-in console
- Error handling with helpful messages
- Support for all NovaScript features (variables, functions, loops, conditionals)

💻 **Responsive Design**
- Works on desktop, tablet, and mobile devices
- Flexible editor and console layout
- Touch-friendly buttons and controls

🔧 **Full Feature Support**
- Variables: `var x = 10`
- Functions with parameters and return values
- Conditionals: `if`/`else` statements
- Loops: `for` and `while` loops
- Arithmetic and string operations
- Comments with `#`

## Project Structure

```
NovaScript/
├── nova_interpreter.py      # NovaScript Python interpreter (core execution engine)
├── server.py                # Flask backend server
├── requirements.txt         # Python dependencies
├── templates/
│   └── index.html           # Main IDE HTML page with editor and console
└── static/
    ├── style.css            # Professional CSS styling
    └── script.js            # Frontend JavaScript for interactivity
```

## Installation & Setup

### Prerequisites

- **Python 3.7+** (Check with `python --version`)
- **pip** (Python package manager)
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Step 1: Install Dependencies

Navigate to the NovaScript directory and install Flask:

```powershell
cd e:\NovaScript
pip install -r requirements.txt
```

Or install Flask directly:

```powershell
pip install Flask==2.3.3
```

### Step 2: Start the Server

Run the Flask development server:

```powershell
python server.py
```

You should see output like:
```
NovaScript Web IDE Server
======================================================================
Starting NovaScript Web IDE Server...
======================================================================

Access the IDE from your browser:
  → http://127.0.0.1:5000/

Press Ctrl+C to stop the server
======================================================================
```

### Step 3: Open in Browser

Open your web browser and navigate to:

```
http://127.0.0.1:5000
```

The NovaScript IDE should load with a default example program ready to run!

## Usage Guide

### Writing Code

1. **Code Editor (Left Panel)**
   - Write your NovaScript code in the editor
   - Syntax highlighting provides instant visual feedback
   - Line numbers help identify errors

2. **Example Code**
   - The editor comes pre-loaded with a working example
   - Click "Reset" button to restore the default example

### Running Code

**Option 1: Run Button**
- Click the blue "▶ Run Code" button in the top right

**Option 2: Keyboard Shortcut**
- Press `Ctrl+Enter` (Windows/Linux) or `Cmd+Enter` (Mac) to execute

**Option 3: Editor Hotkey**
- The hotkey is active in the code editor

### Viewing Output

- **Output Console (Right Panel)**
  - All `print()` statements display here
  - Errors are displayed in red with helpful messages
  - Each output line appears on its own line

### Managing the Console

- **Clear Output**: Click the "✕ Clear Output" button to clear the console
- **Auto-scroll**: Console automatically scrolls to show new output
- **Persistent History**: Console content remains until you clear it

## NovaScript Syntax Reference

### Variables
```nova
var name = value
var x = 10
var message = "Hello"
```

### Functions
```nova
function functionName(param1, param2):
{
    print("Function body")
    return result
}
```

### Print Statement
```nova
print("Hello, World")
print("Value: " + x)  # String concatenation
```

### Conditionals
```nova
if (condition): {
    print("If body")
} else: {
    print("Else body")
}
```

### While Loop
```nova
var count = 0
while (count < 5): {
    print("Count: " + count)
    count = count + 1
}
```

### For Loop
```nova
for (var i = 0 : i < 5 : i = i + 1): {
    print("i = " + i)
}
```

### Operators
- **Arithmetic**: `+`, `-`, `*`, `/`, `%`
- **Comparison**: `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Logical**: `and`, `or`, `!`

### Comments
```nova
# This is a comment
```

## Examples

### Example 1: Hello World
```nova
function greet(name):
{
    print("Hello, " + name)
}

greet("World")
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

print("Fibonacci(7) = " + fibonacci(7))
```

### Example 3: Loop and Arithmetic
```nova
var sum = 0
for (var i = 1 : i <= 10 : i = i + 1): {
    sum = sum + i
}
print("Sum 1 to 10: " + sum)
```

### Example 4: Conditionals
```nova
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

## Backend Architecture

### Flask Server (server.py)

The backend consists of:

1. **Main Routes**
   - `GET /` - Serves the IDE frontend
   - `POST /api/execute` - Executes NovaScript code
   - `GET /api/highlight-keywords` - Returns language keywords

2. **Code Execution Pipeline**
   - Receives code via JSON POST request
   - Passes code through NovaScript interpreter (Lexer → Parser → Executor)
   - Captures stdout using Python's `io.StringIO`
   - Returns output or error as JSON response

3. **Error Handling**
   - Catches syntax errors from lexer/parser
   - Catches runtime errors from executor
   - Returns helpful error messages to frontend

### Frontend Architecture

The frontend uses:

1. **HTML (index.html)**
   - CodeMirror editor integration
   - Console output display area
   - Control buttons (Run, Clear, Reset)
   - Responsive layout

2. **CSS (style.css)**
   - Modern dark theme
   - Responsive grid layout
   - Professional styling for code editor
   - Terminal-style console appearance
   - Mobile-friendly design

3. **JavaScript (script.js)**
   - Handles code execution via AJAX
   - Manages editor state and output
   - Event listeners for buttons and keyboard
   - Console output management
   - Real-time UI updates

## API Documentation

### POST /api/execute

**Request:**
```json
{
    "code": "var x = 10\nprint(x)"
}
```

**Success Response (200):**
```json
{
    "success": true,
    "output": "10\n"
}
```

**Error Response (200):**
```json
{
    "success": false,
    "error": "Error: Undefined variable: x"
}
```

### GET /api/highlight-keywords

**Response:**
```json
{
    "keywords": [
        "var", "function", "print", "if", "else",
        "for", "while", "return", "in", "True", "False"
    ]
}
```

## Customization & Extension

### Adding More Features

The architecture is modular and easy to extend:

1. **Modify `nova_interpreter.py`**
   - Add new keywords to `Lexer.KEYWORDS`
   - Add parsing methods in `Parser`
   - Add execution logic in `Executor`

2. **Update `server.py`**
   - The Flask routes automatically work with new features

3. **Enhance `script.js`**
   - Add new buttons and event listeners
   - Implement custom syntax highlighting
   - Add keyboard shortcuts

### Styling Customization

- Modify `static/style.css` for custom colors, fonts, and layout
- CSS variables (defined at top) make theme changes easy
- Responsive breakpoints at `@media` rules

### Adding Built-in Functions

Add new built-in functions by extending the executor:

```python
# In Executor class
def evaluate_call(self, expr):
    # Add built-ins
    if name == 'len':
        # Custom len() implementation
    elif name == 'input':
        # Custom input() implementation
```

## Troubleshooting

### Server Won't Start

**Problem**: `Address already in use` error
- **Solution**: Change port in `server.py` from 5000 to another (e.g., 5001)

**Problem**: `ModuleNotFoundError: No module named 'flask'`
- **Solution**: Install Flask: `pip install Flask`

### Code Won't Execute

**Problem**: "No code provided" error
- **Solution**: Make sure you have code in the editor and click Run

**Problem**: Code runs but no output appears
- **Solution**: Make sure you're using `print()` to output results

**Problem**: Syntax error even though code looks correct
- **Solution**: NovaScript requires braces `{}` for multi-statement blocks

### IDE Not Loading

**Problem**: Blank page when opening http://localhost:5000
- **Solution**: Check Flask server is running (you should see "Starting server at...")
- **Solution**: Try refreshing browser (F5 or Ctrl+R)
- **Solution**: Check console for JavaScript errors (F12 → Console tab)

## Performance Notes

- The interpreter runs on the server, making execution fast and secure
- Output is captured efficiently without slowing down code
- CodeMirror provides smooth editing even with large files
- Responsive UI updates without page reloads

## Security Considerations

- Code execution is sandboxed within the Python interpreter
- User code runs in an isolated executor context
- Frontend validation prevents malformed requests
- Flask CORS is configured for local use

## Browser Compatibility

✅ Chrome 90+
✅ Firefox 88+
✅ Safari 14+
✅ Edge 90+

## License

Part of the NovaScript project

## Support & Documentation

- GitHub Repository: https://github.com/PixelStudio330/NovaScript
- NovaScript Documentation: See main README.md

## Next Steps

After getting the IDE running:

1. Try the default example program
2. Experiment with different NovaScript programs
3. Explore the source code to understand how it works
4. Extend the language with new features
5. Customize the styling and interface

## Development Tips

- Use browser DevTools (F12) to debug JavaScript
- Check Flask console output for server-side errors
- Use `console.log()` in JavaScript for debugging
- Add print statements in Python for debugging interpreter

Enjoy coding with NovaScript! 🚀
