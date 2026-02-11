# NovaScript Web IDE - Quick Start Guide

## 🚀 Getting Started

Your fully functional web-based NovaScript IDE is now running!

### Access the IDE

Open your browser and visit:
```
http://127.0.0.1:5000
```

## 💡 Features You'll See

### 1. **Code Editor (Left Panel)**
   - Pre-loaded with example NovaScript code
   - Syntax highlighting with line numbers
   - Supports all NovaScript keywords: var, function, print, if, else, for, while, return

### 2. **Control Buttons (Top Right)**
   - **▶ Run Code** - Execute the code immediately
   - **✕ Clear Output** - Clear the console
   - **↻ Reset** - Restore the default example

### 3. **Output Console (Right Panel)**
   - Terminal-style output display
   - Shows results from `print()` statements
   - Displays error messages in red
   - Auto-scrolls to new output

## 🧪 Quick Tests

### Test 1: Hello World
Replace the editor code with:
```nova
print("Hello from NovaScript Web IDE!")
```
Click **Run Code** → You should see: `Hello from NovaScript Web IDE!`

### Test 2: Variables and Arithmetic
```nova
var x = 10
var y = 20
print("Sum: " + (x + y))
print("Product: " + (x * y))
```
Click **Run Code** → Output:
```
Sum: 30
Product: 200
```

### Test 3: Functions
```nova
function add(a, b):
{
    return a + b
}

var result = add(5, 7)
print("5 + 7 = " + result)
```
Click **Run Code** → Output: `5 + 7 = 12`

### Test 4: Loops
```nova
for (var i = 1 : i <= 5 : i = i + 1): {
    print("Square of " + i + " = " + (i * i))
}
```
Click **Run Code** → Output shows squares from 1 to 25

### Test 5: Conditionals
```nova
var score = 85
if (score >= 90): {
    print("Grade: A")
} else: {
    if (score >= 80): {
        print("Grade: B")
    }
}
```
Click **Run Code** → Output: `Grade: B`

## ⌨️ Keyboard Shortcuts

- **Ctrl+Enter** (Windows/Linux) or **Cmd+Enter** (Mac) - Run code
- Use Tab key for auto-indentation
- Use Ctrl+/ to comment/uncomment lines (CodeMirror feature)

## 🔍 How It Works

### Frontend → Backend Communication

1. You write code in the editor
2. Click "Run Code" or press Ctrl+Enter
3. Browser sends code to backend via AJAX POST request
4. Flask server receives the code
5. NovaScript interpreter (Lexer → Parser → Executor) processes it
6. Output is captured and returned as JSON
7. Browser displays results in the console

### Behind the Scenes

- **server.py** - Flask web server handling HTTP requests
- **nova_interpreter.py** - NovaScript execution engine
- **templates/index.html** - Frontend structure
- **static/style.css** - Professional dark-theme styling
- **static/script.js** - JavaScript for editor and interactivity

## 🎨 Customization

### Change Theme
Edit `static/style.css` at the top to modify colors (e.g., `--accent-color`)

### Add More Buttons
Edit `templates/index.html` to add buttons, then add event listeners in `static/script.js`

### Modify Default Code
Edit `DEFAULT_CODE` variable in `static/script.js`

## 🐛 Troubleshooting

### IDE Doesn't Load
- Check if Flask server is running
- Refresh browser (F5)
- Check console for errors (F12 → Console tab)

### Code Runs But No Output
- Make sure to use `print()` for output
- Remember NovaScript requires braces `{}` for blocks: `if (x > 5): {}`

### Syntax Error in IDE
- Check you're using correct NovaScript syntax
- Function parameters must be in parentheses: `function greet(name):`
- Loop syntax requires colons: `for (var i = 1 : i < 10 : i = i + 1):`

## 📝 Debug Mode

Open browser console (F12) to see:
- JavaScript debugger
- Network requests (F12 → Network tab)
- Server errors (check Flask console)

## 🎯 Example Programs

### Fibonacci Sequence
```nova
function fib(n):
{
    if (n <= 1): {
        return n
    }
    return fib(n - 1) + fib(n - 2)
}

print("Fib(10) = " + fib(10))
```

### Counter Program
```nova
var counter = 0
while (counter < 3): {
    print("Counter: " + counter)
    counter = counter + 1
}
print("Done!")
```

### String Manipulation
```nova
var name = "NovaScript"
print("Language: " + name)
print("Greeting: " + "Hello, " + name + "!")
```

## 🚀 Next Steps

1. **Explore the Code**
   - Read comments in `server.py`, `nova_interpreter.py`
   - Understand the architecture in frontend files

2. **Extend Features**
   - Add new keywords to `nova_interpreter.py`
   - Add UI buttons for new features
   - Implement array/list support

3. **Deploy Online**
   - Use Heroku, Replit, or similar platforms
   - Modify CORS settings for production
   - Set `debug=False` in `server.py`

4. **Share Projects**
   - Push to GitHub
   - Create code sharing feature
   - Add save/load functionality

## 📊 Project Files

```
NovaScript/
├── nova_interpreter.py      # Core interpreter (Lexer, Parser, Executor)
├── server.py                # Flask backend server
├── requirements.txt         # Python dependencies (Flask, Werkzeug)
├── templates/
│   └── index.html           # Main IDE page (HTML + CodeMirror)
├── static/
│   ├── style.css           # Professional dark-theme CSS
│   └── script.js           # Frontend JavaScript (AJAX, editor control)
├── WEB_IDE_README.md       # Complete setup & API documentation
└── QUICK_START.md          # This file
```

## 💬 Support

For issues or questions:
- Check Flask console output
- Check browser console (F12)
- Review code comments
- Visit GitHub: https://github.com/PixelStudio330/NovaScript

---

**Enjoy coding with NovaScript!** 🎉

Created with ❤️ by PixelStudio330
