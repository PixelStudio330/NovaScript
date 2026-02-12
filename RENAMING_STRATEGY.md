# NovaScript → NovaScript-X Renaming Strategy

## Renaming Overview

**Old Name** → **New Name**
- PyPI Package: `nova-script` → `novascript-x`
- Module Name: `nova` → `novascriptx`
- CLI Command: `nova` → `novax`
- Entry Point: `nova.nova_cli:main` → `novascriptx.novascriptx_cli:main`

## Why "novascript-x"?

✅ Unique on PyPI  
✅ Maintains branding  
✅ Professional and memorable  
✅ Not conflicting with existing packages  
✅ Clear intent as a programming language  

---

## Files to Update (Systematic Renaming)

### Phase 1: Directory Structure
- [ ] Rename `nova/` → `novascriptx/`
- [ ] Keep `novascriptx/stdlib/` (unchanged)
- [ ] Keep `novascriptx/web/` (unchanged)

### Phase 2: Python Files
- [ ] Rename `nova/nova_cli.py` → `novascriptx/novascriptx_cli.py`
- [ ] Update `novascriptx/__init__.py` imports
- [ ] Update `novascriptx/interpreter.py` version string

### Phase 3: Configuration Files
- [ ] Update `setup.py` - package name, entry point, module references
- [ ] Update `.gitignore` if needed
- [ ] Update any tox.ini or CI configs

### Phase 4: Documentation
- [ ] Update `README.md` - installation and usage
- [ ] Update `GETTING_STARTED.md`
- [ ] Update `DOCUMENTATION.md`
- [ ] Update all references to CLI command
- [ ] Update import examples

### Phase 5: Testing & Validation
- [ ] Reinstall package: `pip install -e .`
- [ ] Test: `novax --version`
- [ ] Test: `novax example.nova`
- [ ] Test: `novax -c "print(42)"`
- [ ] Test stdlib: `var m = require("math"); m.sqrt(100)`
- [ ] Run comprehensive tests
- [ ] Check PyPI availability: `pip index versions novascript-x`

### Phase 6: Build & Release
- [ ] Clean build artifacts: `rm -rf build/ dist/`
- [ ] Build wheels: `python -m build`
- [ ] Dry run upload: `twine check dist/*`
- [ ] Publish to PyPI: `twine upload dist/*`

---

## Renaming Details

### setup.py Changes
```python
# BEFORE
name='nova-script',
packages=find_packages(),
entry_points={
    'console_scripts': [
        'nova=nova.nova_cli:main',
    ],
}

# AFTER
name='novascript-x',
packages=find_packages(),
entry_points={
    'console_scripts': [
        'novax=novascriptx.novascriptx_cli:main',
    ],
}
```

### Import Changes (Everywhere)
```python
# BEFORE
from nova.interpreter import run_code
import nova

# AFTER
from novascriptx.interpreter import run_code
import novascriptx
```

### CLI Documentation Changes
```bash
# BEFORE
nova --version
nova script.nova
nova -c "print('Hello')"

# AFTER
novax --version
novax script.nova
novax -c "print('Hello')"
```

---

## Impact Analysis

### User Facing Changes
- ✅ Installation: `pip install novascript-x` (new)
- ✅ CLI command: `novax` (was `nova`)
- ❌ Can no longer use `nova` command directly
- ⚠️ Users need to update scripts/docs

### Internal Changes (Transparent to Users)
- Module name change: `nova` → `novascriptx`
- CLI file: `nova_cli.py` → `novascriptx_cli.py`
- Imports updated but API same

### Backward Compatibility
- ❌ Not backward compatible (name change)
- ✅ All functionality preserved
- ✅ Same language, same stdlib

---

## Safety Checks

Before publishing:
- [ ] All imports working
- [ ] CLI accessible
- [ ] Examples execute correctly
- [ ] Stdlib modules load
- [ ] Error handling intact
- [ ] No orphaned references to old name
- [ ] Documentation updated
- [ ] Version remains 1.0.0 (or increment appropriately)

---

## PyPI Publication Steps

After successful local testing:

```bash
# 1. Check package
python -m build
twine check dist/*

# 2. Dry run (if twine has it)
twine upload --repository testpypi dist/*

# 3. Publish
twine upload dist/*

# 4. Verify
pip install novascript-x
novax --version
```

---

## Quick Reference: Old vs New

| Item | Old | New |
|------|-----|-----|
| PyPI Package | `nova-script` | `novascript-x` |
| Python Module | `nova` | `novascriptx` |
| CLI Command | `nova` | `novax` |
| CLI File | `nova_cli.py` | `novascriptx_cli.py` |
| Import | `from nova import` | `from novascriptx import` |
| Entry Point | `nova=nova.nova_cli:main` | `novax=novascriptx.novascriptx_cli:main` |
| Install | `pip install nova-script` | `pip install novascript-x` |

---

## Status

Current Phase: **Planning**
Next: **Execute Phase 1 - Directory Reorganization**
