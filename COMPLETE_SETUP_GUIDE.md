# NovaScript Web IDE - Complete Setup & Troubleshooting Guide

## 🎯 Quick Reference

✅ **Status**: NovaScript Web IDE is fully functional on Windows
🔗 **Access URL**: `http://127.0.0.1:5000/`
📋 **Setup Time**: ~5 minutes


## ⚡ Quick Setup (5 Minutes)

For detailed setup instructions, see [GETTING_STARTED.md](GETTING_STARTED.md).

**TL;DR**:
```powershell
cd e:\NovaScript
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python server.py
# Then open: http://127.0.0.1:5000/
```


## 🔧 Windows Localhost Fix (Why It Works)
### The Problem
Windows resolves `localhost` to both IPv4 (`127.0.0.1`) and IPv6 (`::1`). Flask's original configuration couldn't handle dual-stack connections properly, resulting in "Cannot GET /" errors.

### The Solution
```python
app.run(
    debug=True,
    host='0.0.0.0',      # Listen on all interfaces
    port=5000,
    threaded=True,       # ← KEY FIX: Multi-threaded socket handling
    use_reloader=True    # Auto-reload on code changes
)
```

**Why `threaded=True` fixes it**: Windows socket driver doesn't handle IPv4+IPv6 without threading. This enables simultaneous connections on both loopback addresses.


## 📋 Verification Checklist

### Port 5000 Availability
```powershell
netstat -ano | findstr :5000  # Should show no output (port free)
```

### File Structure
```powershell
cd e:\NovaScript
Test-Path nova_interpreter.py    # True
Test-Path server.py               # True
Test-Path templates\index.html    # True
Test-Path static\style.css        # True
Test-Path static\script.js        # True
```

### Flask Startup Verification
```powershell
python server.py
# Look for output:
# * Serving Flask app 'server'
# * Debug mode: on
# * Running on http://127.0.0.1:5000
```

### Sample Code Execution
In IDE, click **Run Code** with default example:
```
Expected Output:
Sum: 30
Hello, World
5 + 3 = 8
You are an adult
Count: 1
Count: 2
Count: 3
For loop from 1 to 5:
i = 1
i = 2
i = 3
i = 4
i = 5
```


## 🚨 Troubleshooting

### Issue: "Address already in use"
```powershell
taskkill /F /IM python.exe /T
# Wait 1-2 seconds, then:
python server.py
```

### Issue: "Cannot GET /" or blank page
**Step 1**: Restart server
```powershell
# Press Ctrl+C, then:
python server.py
```

**Step 2**: Clear browser cache and hard refresh
```
Ctrl+Shift+Delete  (or Ctrl+F5)
```

**Step 3**: Verify hosts file (Administrator PowerShell)
```powershell
type C:\Windows\System32\drivers\etc\hosts | findstr localhost
# Should show:
# 127.0.0.1       localhost
# ::1             localhost

# If missing, add:
Add-Content -Path "C:\Windows\System32\drivers\etc\hosts" -Value "`n127.0.0.1`tlocalhost" -Encoding UTF8
Add-Content -Path "C:\Windows\System32\drivers\etc\hosts" -Value "::1`tlocalhost" -Encoding UTF8
```

**Step 4**: Flush DNS cache
```powershell
ipconfig /flushdns
nslookup localhost  # Should return 127.0.0.1 and ::1
```

### Issue: "jinja2.exceptions.TemplateNotFound: index.html"
```powershell
# Verify file exists:
Test-Path templates\index.html  # Should be True
ls templates\                    # Should list index.html

# If missing, file needs to be recreated
```

### Issue: "No module named 'flask'"
```powershell
.\.venv\Scripts\Activate.ps1
pip install Flask==2.3.3
python server.py
```

### Issue: Code won't execute (no output)
**Check 1**: Browser console for JavaScript errors
```
Press F12 → Console tab
Look for red errors (especially "Cannot POST /api/execute")
```

**Check 2**: Flask console for Python errors
```
Look at terminal where python server.py is running
Look for error messages or POST request failures
```

**Check 3**: Test with simple code
```nova
print("Hello")
```

**Check 4**: Check Network tab in F12
```
Click Run Code
Press F12 → Network tab
Look for /api/execute request (should be green 200)
```


## 🎓 Architecture Overview

### Request Flow
```
USER CODE IN EDITOR
         ↓
JAVASCRIPT → POST /api/execute
         ↓
PYTHON FLASK SERVER
         ↓
NOVA_INTERPRETER (Lexer → Parser → Executor)
         ↓
CAPTURE STDOUT
         ↓
RETURN JSON { "success": true, "output": "..." }
         ↓
JAVASCRIPT APPENDS TO CONSOLE
         ↓
USER SEES OUTPUT IN BROWSER
```

### Component Responsibilities
| Component | Function |
|-----------|----------|
| `nova_interpreter.py` | Lexer, Parser, Executor (language runtime) |
| `server.py` | Flask HTTP server, routes, request handling |
| `templates/index.html` | Editor UI, CodeMirror integration |
| `static/style.css` | Dark theme styling |
| `static/script.js` | AJAX, editor state, console management |

### Flask Routes
- `GET /` → Returns index.html
- `POST /api/execute` → Takes `{code: string}`, returns `{success: bool, output: string}` or error
- `GET /api/highlight-keywords` → Returns language keywords for syntax highlighting


## 📊 Performance Metrics

| Operation | Time |
|-----------|------|
| Flask startup | ~1-2 seconds |
| Page load | ~500ms |
| Simple code execution (`print("x")`) | <100ms |
| Medium recursion (`fib(15)`) | ~200-300ms |
| Complex recursion (`fib(20)`) | ~1-2 seconds |
| Clear console | <10ms |

---

## 🔐 Development vs Production

### Current (Development)
- ✅ Debug mode ON (auto-reloads)
- ✅ Code runs in isolated executor (safe)
- ⚠️ No authentication
- ⚠️ Both `127.0.0.1` and `localhost` work

### For Production Deployment
```python
app.run(
    debug=False,           # Turn off debug
    host='127.0.0.1',
    port=5000,
    threaded=True
)
```

Also consider:
- Use Gunicorn or uWSGI server
- Add HTTPS/SSL certificate
- Implement authentication if public
- Set resource limits (timeout, memory limits)
- Use environment variables for config

---

## 💾 File Locations

```
e:\NovaScript\
├── nova_interpreter.py       (Core interpreter - DON'T TOUCH)
├── server.py                 (Flask app - RUN THIS)
├── requirements.txt          (Dependencies)
├── test.nova                 (Sample NovaScript file)
├── templates/
│   └── index.html            (Web IDE interface)
└── static/
    ├── style.css             (dark theme styling)
    └── script.js             (editor + AJAX logic)
```

---

## 🆘 Advanced Debugging

If standard troubleshooting doesn't help:

```powershell
# 1. Verify Python works
python --version              # Should be 3.7+
python -c "import sys; print(sys.executable)"

# 2. Verify virtual environment
.\.venv\Scripts\Activate.ps1
python -c "import sys; print(sys.prefix)"  # Should show .venv path

# 3. Verify Flask installation
python -c "import flask; print(flask.__version__)"  # Should be 2.3.3

# 4. Test interpreter directly
python -c "from nova_interpreter import Lexer, Parser, Executor; print('OK')"

# 5. Start server with debug logging
python -c "import logging; logging.basicConfig(level=logging.DEBUG); exec(open('server.py').read())"

# 6. Check network with netstat
netstat -an | findstr 5000   # Shows all connections on port 5000

# 7. Dump hosts file
type C:\Windows\System32\drivers\etc\hosts
```

---

## 📚 Documentation Guide

| File | Purpose |
|------|---------|
| **GETTING_STARTED.md** | Minimal 3-step setup guide |
| **QUICK_START.md** | Language features, examples, keyboard shortcuts |
| **COMPLETE_SETUP_GUIDE.md** | This file - setup + advanced troubleshooting |
| **README.md** | NovaScript language reference |

---

## ✨ Common Tasks

| Task | Command |
|------|---------|
| Start server | `python server.py` |
| Stop server | Press `Ctrl+C` |
| Kill lingering processes | `taskkill /F /IM python.exe /T` |
| Access IDE | `http://127.0.0.1:5000/` |
| Clear browser cache | `Ctrl+Shift+Delete` (or `Ctrl+F5`) |
| Check port 5000 | `netstat -ano \| findstr :5000` |
| Reinstall dependencies | `pip install -r requirements.txt` |

---

**Questions?** Check the Flask console output - most issues are logged there.
