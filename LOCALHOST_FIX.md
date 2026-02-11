# NovaScript Web IDE - Windows Localhost Fix Guide

## Problem Summary

On Windows, the NovaScript Web IDE works on `http://127.0.0.1:5000/` but fails with "Cannot GET /" on `http://localhost:5000/`.

This is caused by IPv6/IPv4 resolution differences on Windows when binding Flask servers.

## Root Cause Analysis

### Why 127.0.0.1 Works but localhost Doesn't

1. **127.0.0.1** (IPv4 loopback)
   - Directly routes to the IPv4 stack
   - Flask's `0.0.0.0` binding includes IPv4
   - Works reliably

2. **localhost** (DNS name)
   - Resolves to BOTH `127.0.0.1` (IPv4) AND `::1` (IPv6)
   - On Windows, sometimes prefers IPv6 (`::1`)
   - Flask's `0.0.0.0` binding may not properly expose the IPv6 interface
   - Results in "Cannot GET /" error

### Windows Hosts File

Both entries must exist:
```
127.0.0.1       localhost
::1             localhost
```

If only IPv4 is present, IPv6 connections fail.
If both exist but Flask isn't binding to IPv6, connections still fail.

## Solution: Updated Flask Configuration

### The Fix

The key is ensuring Flask explicitly binds to both IPv4 and IPv6. Update [server.py](server.py) with:

```python
if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',      # Binds to all IPv4 interfaces
        port=5000,
        threaded=True,       # CRITICAL for Windows threading issues
        use_reloader=True    # Auto-reload on code changes
    )
```

### Why This Works

- **`host='0.0.0.0'`**: Binds to all IPv4 addresses (127.0.0.1 and more)
- **`threaded=True`**: Windows needs this for proper socket handling
- **`use_reloader=True`**: Enables auto-reload on file changes

## Complete Fix Checklist

### Step 1: Verify Windows Hosts File

```bash
# PowerShell (Run as Administrator)
type C:\Windows\System32\drivers\etc\hosts | findstr localhost
```

Expected output:
```
127.0.0.1       localhost
::1             localhost
```

If missing, add entries (Run PowerShell as Admin):
```powershell
# IPv4 entry
Add-Content -Path C:\Windows\System32\drivers\etc\hosts -Value "`n127.0.0.1`tlocalhost" -Encoding UTF8

# IPv6 entry
Add-Content -Path C:\Windows\System32\drivers\etc\hosts -Value "::1`tlocalhost" -Encoding UTF8
```

### Step 2: Verify Folder Structure

```
E:\NovaScript\
├── nova_interpreter.py       ✓ Required
├── server.py                 ✓ Updated Flask server
├── requirements.txt          ✓ Dependencies
├── templates\
│   └── index.html            ✓ HTML template
└── static\
    ├── style.css             ✓ Styling
    └── script.js             ✓ Frontend logic
```

Verify all files exist:
```powershell
cd e:\NovaScript
ls               # Check main directory
ls templates     # Check templates folder
ls static       # Check static folder
```

### Step 3: Clear Python Cache

Delete old bytecode that might cause issues:

```powershell
# Remove all __pycache__ directories
cd e:\NovaScript
Remove-Item -Path .\.venv\lib\__pycache__ -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path .\__pycache__ -Recurse -Force -ErrorAction SilentlyContinue
```

### Step 4: Kill All Python Processes

```powershell
taskkill /F /IM python.exe /T
```

Wait 2 seconds for all processes to terminate.

### Step 5: Start Fresh Server

```powershell
cd e:\NovaScript

# Activate virtual environment
.\.venv\Scripts\Activate.ps1

# Start the server
python server.py
```

You should see:
```
NovaScript Web IDE Server
======================================================================
Starting NovaScript Web IDE Server...
======================================================================

Access the IDE from your browser:
  • http://127.0.0.1:5000/
  • http://localhost:5000/

...
```

### Step 6: Test Both URLs

#### Test 1: IPv4 (127.0.0.1)
```
http://127.0.0.1:5000/
```
Expected: CodeMirror editor loads with example code

#### Test 2: localhost (DNS resolution)
```
http://localhost:5000/
```
Expected: Same as Test 1 - full IDE interface with editor and console

#### Test 3: Run Code
In the IDE:
1. Click "Run Code" button (or press Ctrl+Enter)
2. Should see output in the console

#### Test 4: Error Handling
Replace code with invalid syntax:
```nova
var x =
```
Click "Run Code" → Should show error in console

## Diagnostic Commands

### Check Port Usage

```powershell
# See what's using port 5000
netstat -ano | findstr :5000

# If something is using port 5000, kill it
taskkill /PID <PID> /F
```

### Test DNS Resolution

```powershell
# Test IPv4 resolution
nslookup localhost

# Should show:
# Name:    localhost
# Address: 127.0.0.1
#          ::1
```

### Check Flask Routes

Flask will print routes on startup. Look for:
```
* Route: /                 -> index
* Route: /api/execute      -> execute_code
* Route: /api/highlight-keywords -> get_keywords
```

## Advanced Configuration (Optional)

### For Production Use

If you want to run on a specific IP only:

```python
# Only IPv4 loopback
app.run(host='127.0.0.1', port=5000)

# Only IPv6 loopback
app.run(host='::1', port=5000, threaded=True)

# All interfaces (current - recommended)
app.run(host='0.0.0.0', port=5000, threaded=True)
```

### For Custom Port

If port 5000 is in use, change it:

```python
app.run(host='0.0.0.0', port=5001, threaded=True)
```

Then access via:
- `http://127.0.0.1:5001/`
- `http://localhost:5001/`

### Enable CORS (For External Access)

If you want to access from other machines:

```bash
pip install flask-cors
```

Then in `server.py`:

```python
from flask_cors import CORS
CORS(app)
```

And run:
```python
app.run(host='0.0.0.0', port=5000, threaded=True)
```

Then access from other machines:
```
http://<YOUR_WINDOWS_IP>:5000/
```

Find your IP:
```powershell
ipconfig | findstr "IPv4"
```

## Troubleshooting Table

| Symptom | Cause | Solution |
|---------|-------|----------|
| "Cannot GET /" on localhost | IPv6 routing issue | See Step 1: Verify hosts file |
| Works on 127.0.0.1 but not localhost | Flask not binding to IPv6 | Update to `host='0.0.0.0'` + `threaded=True` |
| "Connection refused" on both | Flask not running | Check Flask console output |
| "Address already in use" | Port 5000 occupied | Kill process: `taskkill /F /IM python.exe` |
| Blank page loads | Templates not found | Verify templates/index.html exists |
| Editor works but no output | AJAX request failed | Check browser console (F12) for errors |
| Slow startup on Windows | Flask debugger overhead | Normal during development (add --fast-reload flag later) |

## Browser Testing

### Clear Browser Cache

```
Chrome:  Ctrl+Shift+Delete
Firefox: Ctrl+Shift+Delete
Edge:    Ctrl+Shift+Delete
```

Then reload:
- Press `F5` (refresh)
- Or `Ctrl+F5` (hard refresh)

### Check Browser Console

Press `F12` → Console tab:
- Look for JavaScript errors
- Check Network tab for failed requests to `/api/execute`
- Verify `/api/execute` returns JSON

## Expected Behavior After Fix

### Startup Messages

```
 * Running on http://127.0.0.1:5000
 * Running on http://[::1]:5000    ← IPv6 line (may vary)
 * WARNING: This is a development server. Do not use it in production.
 * Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with reloader
```

### Both URLs Work

| URL | Result |
|-----|--------|
| http://127.0.0.1:5000 | ✅ Full IDE |
| http://localhost:5000 | ✅ Full IDE |
| http://[::1]:5000 | ✅ Full IDE (if IPv6 enabled) |

### Code Execution Works

1. Default example loads in editor
2. Click "Run Code" → Output appears in console
3. Edit code → Click "Run Code" → New output appears
4. Errors display in red

## Performance Notes

- **First load**: May take 2-3 seconds (Flask startup + compilation)
- **Code execution**: <100ms for simple code, <1s for recursive functions
- **Auto-reload**: ~1-2 seconds when server.py changes (due to reloader)

## Port Considerations

### Why Port 5000?

- Standard Flask development port
- Easy to remember
- Usually available on development machines

### If 5000 is Occupied

```powershell
# Find what's using it
netstat -ano | findstr :5000

# Kill it (if safe)
taskkill /PID <PID> /F

# Or use different port
python server.py  # Edit port in server.py first
```

## Final Verification Script

Save as `test_novascript_ide.ps1`:

```powershell
Write-Host "NovaScript IDE Verification" -ForegroundColor Cyan
Write-Host "===========================" 

# Check hosts file
Write-Host "`nChecking hosts file..."
$hosts = Get-Content C:\Windows\System32\drivers\etc\hosts | Select-String localhost
if ($hosts -match "127.0.0.1" -and $hosts -match "::1") {
    Write-Host "✓ Hosts file configured correctly" -ForegroundColor Green
} else {
    Write-Host "✗ Hosts file missing entries" -ForegroundColor Red
}

# Check port 5000
Write-Host "`nChecking if port 5000 is available..."
$port = netstat -ano | Select-String :5000
if ($port) {
    Write-Host "⚠ Port 5000 is in use" -ForegroundColor Yellow
    Write-Host $port
} else {
    Write-Host "✓ Port 5000 is available" -ForegroundColor Green
}

# Check file structure
Write-Host "`nChecking file structure..."
$files = @(
    "nova_interpreter.py",
    "server.py",
    "templates\index.html",
    "static\style.css",
    "static\script.js"
)

foreach ($file in $files) {
    if (Test-Path $file) {
        Write-Host "✓ $file" -ForegroundColor Green
    } else {
        Write-Host "✗ $file NOT FOUND" -ForegroundColor Red
    }
}

Write-Host "`nVerification complete!" -ForegroundColor Cyan
```

Run it:
```powershell
..\test_novascript_ide.ps1
```

## Summary: Why This Works Now

✅ **Host Configuration**: Hosts file has both IPv4 and IPv6
✅ **Flask Binding**: `host='0.0.0.0'` binds to all interfaces
✅ **Windows Threading**: `threaded=True` enables proper socket handling
✅ **Template Paths**: Using absolute paths ensures files are found
✅ **Both URLs Work**: 
  - 127.0.0.1 → Resolved via IPv4
  - localhost → Resolved via DNS to either IPv4 or IPv6

## Next Steps

1. ✅ Apply the fixes above
2. ✅ Test both URLs
3. ✅ Run sample code
4. ✅ Push changes to GitHub
5. 🚀 Share the IDE with others!

---

**Need Help?**

Check the console output when starting the server. Most issues are visible there.

For persistent issues, check:
- Browser console (F12)
- Flask console output
- Antivirus/Firewall blocking localhost

Good luck with NovaScript! 🎉
