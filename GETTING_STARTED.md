# NovaScript Web IDE - Quick Start (127.0.0.1)

## ✅ What You Need

- Windows 10/11
- Python 3.7+
- Flask installed (`pip install Flask`)

## 🚀 Run the IDE (3 Steps)

### Step 1: Navigate to Project
```powershell
cd e:\NovaScript
```

### Step 2: Start Server
```powershell
python server.py
```

You'll see:
```
NovaScript Web IDE Server
======================================================================
Starting NovaScript Web IDE Server...

Access the IDE from your browser:
  → http://127.0.0.1:5000/

Press Ctrl+C to stop the server
======================================================================
```

### Step 3: Open in Browser
```
http://127.0.0.1:5000/
```

## ✨ That's It!

You should see:
- 📝 **Code Editor** on the left with example code
- 📺 **Output Console** on the right (empty initially)
- 🎛️ **Buttons**: Run Code, Clear Output, Reset

## 💻 Use the IDE

1. **Write Code** - Type NovaScript code in the editor
2. **Run Code** - Click "▶ Run Code" or press `Ctrl+Enter`
3. **See Output** - Results appear in the console on the right

## 📝 Example Code

Try this:
```nova
var x = 10
print("x = " + x)

function greet(name):
{
    print("Hello, " + name)
}

greet("NovaScript")
```

Click "Run Code" → You'll see output in the console!

## ❌ Not Working?

Try these fixes:

**Issue: "Address already in use"**
```powershell
taskkill /F /IM python.exe /T
python server.py
```

**Issue: "Cannot find nova_interpreter"**
- Make sure you're in `e:\NovaScript` directory
- Check that `nova_interpreter.py` exists in that folder

**Issue: Blank page in browser**
- Refresh the page (F5)
- Check browser console (F12 → Console tab) for errors

## 🎓 NovaScript Features

✅ Variables: `var x = 10`
✅ Functions: `function name(params): { }`
✅ Conditionals: `if (x > 5): { }`
✅ Loops: `for (var i = 0 : i < 10 : i = i + 1): { }`
✅ Print: `print("Hello")`
✅ Comments: `# Comment here`

## 📚 Full Documentation

- `COMPLETE_SETUP_GUIDE.md` → Comprehensive setup guide
- `WEB_IDE_README.md` → Complete IDE documentation
- `README.md` → NovaScript language guide

## 🎉 Done!

Your NovaScript Web IDE is ready to use at **http://127.0.0.1:5000/**

Happy coding! 🚀
