# Migration Guide: nova-script → novascript-x

## Overview

The NovaScript package has been renamed to **`novascript-x`** to resolve PyPI naming conflicts. All functionality remains identical—this is purely a name change for package distribution purposes.

## What Changed

| Item | Before | After |
|------|--------|-------|
| **PyPI Package** | `nova-script` | `novascript-x` |
| **Python Module** | `nova` | `novascriptx` |
| **CLI Command** | `nova` | `novax` |
| **Installation** | `pip install nova-script` | `pip install novascript-x` |
| **Language** | NovaScript | NovaScript-X |

## For End Users

### Upgrading from nova-script

```bash
# 1. Uninstall old package
pip uninstall nova-script

# 2. Install new package
pip install novascript-x

# 3. Verify installation
novax --version
```

### Quick Reference

**Old code:**
```bash
nova script.nova
nova -c "print('Hello')"
nova --watch program.nova
```

**New code (same language, new command):**
```bash
novax script.nova
novax -c "print('Hello')"
novax --watch program.nova
```

### Your NovaScript Programs Don't Change!

All `.nova` files remain 100% compatible. No modifications needed:

```nova
# This works exactly the same!
var math = require("math")
var result = math.sqrt(100)
print("Result: " + result)
```

Just run with the new command:
```bash
novax my_program.nova
```

---

## For Developers/Contributors

### If You're Working with Source Code

#### Update Imports
```python
# BEFORE
from nova.interpreter import run_code
from nova import run_file

# AFTER
from novascriptx.interpreter import run_code
from novascriptx import run_file
```

#### Update Internal References
```python
# BEFORE
var interpreter = require('nova')

# AFTER
var interpreter = require('novascriptx')
```

#### Installation from Source
```bash
cd novascript-x
pip install -e .  # Development mode
```

---

## FAQ

### Q: Will my old NovaScript programs stop working?
**A:** No! All `.nova` files are 100% compatible. You just need to use the `novax` command instead of `nova`.

### Q: Do I need to update my code?
**A:** Not your NovaScript code. Only if you have scripts that call `nova` command - change them to `novax`.

### Q: What about the old `nova-script` package on PyPI?
**A:** It will be deprecated. New users should install `novascript-x`. Existing users can continue using the old package, but we recommend upgrading.

### Q: Is this a major version bump?
**A:** No, this is still stable v1.0.0. The language didn't change, only the package name. No breaking changes to the language itself.

### Q: Can I use both `nova` and `novax` commands?
**A:** Only if you have both packages installed, but we don't recommend this. Choose one for your project.

### Q: What about Docker/CI/CD scripts?
**A:** Update them to use `novax` instead of `nova`:
```dockerfile
# Before
RUN pip install nova-script

# After
RUN pip install novascript-x
```

### Q: Is the language called "Nova" or "NovaScript" or "NovaScript-X"?
**A:** The language is still called **"NovaScript"**. The package name changed to `novascript-x` for distribution purposes. The `-x` suffix indicates this is the modern runtime version.

---

## Troubleshooting

### Error: `nova: command not found`
You're using the new package but running the old command. Use:
```bash
novax  # instead of nova
```

### Error: `Module not found: novascriptx`
If you're importing in Python, update your imports:
```python
from novascriptx import run_code  # was: from nova import run_code
```

### Error: `novax` command not found after installation
Make sure the package is installed in your active Python environment:
```bash
pip list | grep novascript  # should show novascript-x
which novax                 # should show path to novax
```

---

## Summary

✅ Same language, same functionality  
✅ New package name for PyPI compatibility  
✅ New CLI command: `nova` → `novax`  
✅ All `.nova` programs work unchanged  
✅ Seamless upgrade path  

**Welcome to NovaScript-X!** 🚀
