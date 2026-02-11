# Contributing to NovaScript

Thank you for your interest in contributing to NovaScript! This document provides guidelines and instructions for contributing.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [What Can You Contribute?](#what-can-you-contribute)
- [Contribution Process](#contribution-process)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Documentation](#documentation)
- [Commit Messages](#commit-messages)
- [Pull Request Process](#pull-request-process)

## 🎯 Code of Conduct

Be respectful, inclusive, and professional. We're building a welcoming community for developers of all levels.

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- Git
- GitHub account
- Basic knowledge of Python

### Fork & Clone

1. Fork the repository: Click "Fork" on GitHub
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/NovaScript.git
   cd NovaScript
   ```
3. Add upstream remote:
   ```bash
   git remote add upstream https://github.com/PixelStudio330/NovaScript.git
   ```

## 💻 Development Setup

### Install Development Version

```bash
# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .

# Install any development dependencies
pip install pytest black flake8
```

### Verify Installation

```bash
# Should display version
nova --version

# Should work
nova -c "print(5 + 3)"

# Should run
nova examples/hello_world/main.nova
```

## 🎁 What Can You Contribute?

### Documentation 📚
- Improve README.md or other guides
- Add tutorials or examples
- Fix typos or unclear explanations
- Add docstrings to code
- Create architecture diagrams

### Code 💻
- Implement planned features (see [ROADMAP.md](ROADMAP.md))
- Fix bugs (see Issues)
- Improve performance
- Add type hints
- Refactor modules

### Examples 📝
- Create demo programs
- Add real-world examples
- Create tutorial series
- Build sample projects

### Testing 🧪
- Write unit tests
- Create integration tests
- Test on different platforms
- Report bugs

### Platform Support 🌍
- Test on Windows, macOS, Linux
- Report compatibility issues
- Optimize for different platforms

### Standard Library 📦
- Add new stdlib modules
- Enhance existing modules
- Add documentation for modules
- Create utility functions

## 🔄 Contribution Process

### 1. Create an Issue First

For significant changes, create an issue first:
- **Bug Report**: Describe the bug, reproduction steps, expected behavior
- **Feature Request**: Explain the feature, why it's needed, how it would work
- **Enhancement**: Suggest improvements to existing features

Use issue templates if available.

### 2. Work on Your Feature

Create a feature branch:
```bash
# Update main branch
git fetch upstream
git rebase upstream/main

# Create feature branch
git checkout -b feature/my-feature
```

### 3. Make Changes

Implement your feature or fix:
- Follow coding standards (see below)
- Write clear, readable code
- Add comments for complex logic
- Update docstrings
- Add type hints when applicable

### 4. Test Your Changes

```bash
# Run examples
nova examples/hello_world/main.nova
nova examples/functions_loops/main.nova

# Test your new code
nova tests/my_test.nova  # or python nova_cli.py tests/my_test.nova

# If you wrote unit tests
pytest tests/

# Lint your code
black nova/
flake8 nova/
```

### 5. Update Documentation

- Add docstrings to new functions/classes
- Update README if needed
- Add examples if it's a user-facing feature
- Update ROADMAP.md status if relevant

### 6. Commit & Push

```bash
# Commit with descriptive message (see guidelines below)
git add .
git commit -m "feat: Add new feature description"

# Push to your fork
git push origin feature/my-feature
```

### 7. Create Pull Request

1. Go to YOUR repository on GitHub
2. Click "New Pull Request"
3. Set base to `upstream/main` and compare to your feature branch
4. Fill in PR title and description:
   - **Title**: Concise description (same as commit message)
   - **Description**: 
     - What problem does this solve?
     - How does it work?
     - Related issue(s)
     - Testing notes
5. Click "Create Pull Request"

### 8. Code Review

- Respond to reviewer comments
- Make requested changes
- Push updates (they appear in the PR automatically)
- Once approved, maintainer will merge

## 📝 Coding Standards

### Python Style

Follow [PEP 8](https://pep8.org/) style guide:

```python
# Good: Clear, readable code
def calculate_factorial(n: int) -> int:
    """Calculate the factorial of n.
    
    Args:
        n: Non-negative integer
    
    Returns:
        Factorial of n
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 1
    return n * calculate_factorial(n - 1)


# Also good: Using built-in when available
def factorial(n: int) -> int:
    """Calculate factorial using math.factorial."""
    import math
    return math.factorial(n)
```

### Naming Conventions

```python
# Classes: PascalCase
class MyClass:
    pass

# Functions/variables: snake_case
def my_function():
    my_variable = 10
    return my_variable

# Constants: UPPER_CASE
MAX_ITERATIONS = 100
DEFAULT_TIMEOUT = 30

# Private/internal: _leading_underscore
def _internal_helper():
    pass
```

### Type Hints

Use type hints for clarity:

```python
def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b

def get_user_data(user_id: int) -> dict:
    """Fetch user data by ID."""
    pass

from typing import List, Optional
def process_items(items: List[str]) -> Optional[dict]:
    """Process a list of items."""
    pass
```

### Comments

```python
# Good: Explain why, not what
# Use set for O(1) lookup performance
visited = set()

# Bad: Obvious from code
# Create a set
visited = set()

# Complex logic: Use multi-line comments
# This algorithm uses dynamic programming to avoid
# recalculating subproblems. We cache results in
# the dp dictionary keyed by input parameters.
```

### Line Length

- Aim for 88 characters (Black's default)
- Maximum 100 characters
- Break long lines logically:

```python
# Good: Break at logical point
result = some_function(
    argument1,
    argument2,
    argument3
)

# Also good: Brief enough
message = "This is a long message that needs to be displayed"
```

## 🧪 Testing

### Running Tests

```bash
# Test core features
python nova_cli.py examples/hello_world/main.nova
python nova_cli.py examples/functions_loops/main.nova
python nova_cli.py examples/stdlib_demo/main.nova

# Test your changes
python nova_cli.py your_test_file.nova

# Test REPL
python nova_cli.py

# Test watch mode
python nova_cli.py -w examples/hello_world/main.nova
```

### Creating Test Files

Create a test Nova script:

```nova
# tests/test_arrays.nova (when arrays are implemented)
var arr = [1, 2, 3];
print(arr[0]);           # Should print: 1
print(arr.length);       # Should print: 3

arr.push(4);
print(arr.length);       # Should print: 4

print("All tests passed!");
```

### Python Unit Tests

For core interpreter changes:

```python
# tests/test_interpreter.py
import pytest
from nova.interpreter import Lexer, Parser, Executor

def test_lexer_tokenizes_numbers():
    lexer = Lexer("var x = 42;")
    tokens = lexer.tokenize()
    assert any(t.type == "NUMBER" and t.value == 42 for t in tokens)

def test_parser_creates_ast():
    code = "var x = 10;"
    lexer = Lexer(code)
    parser = Parser(lexer.tokenize())
    ast = parser.parse()
    assert len(ast) == 1
    assert ast[0]['type'] == 'var_declaration'

def test_executor_runs_code():
    code = "print(5 + 3);"
    executor = Executor()
    executor.execute(Lexer(code).tokenize())
    # Should not raise an error
```

## 📖 Documentation

### Docstring Format

Use Google-style docstrings:

```python
def my_function(param1: str, param2: int) -> bool:
    """Short description of what the function does.
    
    Longer description if needed. Explain the algorithm,
    special cases, or important notes.
    
    Args:
        param1: Description of param1
        param2: Description of param2, must be positive
    
    Returns:
        Description of return value
        
    Raises:
        ValueError: When param2 is negative
        TypeError: When param1 is not a string
        
    Examples:
        >>> my_function("test", 5)
        True
    """
    pass
```

### README Updates

When adding features:
1. Update feature list
2. Add example usage
3. Describe behavior clearly
4. Include limitations if applicable

### Example Programs

Create examples that demonstrate:
- **What** the feature does
- **How** to use it
- **Why** it's useful
- **Expected output**

## 💬 Commit Messages

Use conventional commits format:

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Code style (formatting, missing semicolons, etc.)
- **refactor**: Code refactoring without changing behavior
- **perf**: Performance improvement
- **test**: Adding or updating tests
- **chore**: Dependency updates, build changes

### Examples

```bash
# Feature
git commit -m "feat(interpreter): Add member access for objects"

# Bug fix
git commit -m "fix(cli): Handle file paths with spaces"

# Documentation
git commit -m "docs: Update README with array examples"

# Multiple changes
git commit -m "feat(stdlib): Add json module with encode/decode

- Implement JSON.stringify() for serialization
- Implement JSON.parse() for deserialization
- Add error handling for invalid JSON"

# Reference issue
git commit -m "fix(require): Handle circular dependencies

Fixes #123"
```

## 🔀 Pull Request Process

### Before Submitting

- [ ] Code follows style guide
- [ ] Tests pass
- [ ] Documentation updated
- [ ] Commit messages follow guidelines
- [ ] No breaking changes (or documented)
- [ ] PR description is clear

### PR Title Format

Same as commit messages:
- `feat: Add array support`
- `fix: Handle null values properly`
- `docs: Update installation guide`

### PR Description Template

```markdown
## Description
Brief explanation of what this PR does.

## Problem it solves
What issue or feature request does this address?

## Solution
How does this PR solve the problem?

## Related Issues
Closes #123

## Testing
How can reviewers test this change?
- [ ] Run examples/test.nova
- [ ] Check nova --help output
- [ ] Test on Windows/macOS

## Checklist
- [ ] Code follows style guide
- [ ] Self-review completed
- [ ] Comments added for complex logic
- [ ] Documentation updated
- [ ] Tests added/updated
- [ ] No breaking changes (or documented)
```

### After Submission

- Respond to feedback promptly
- Make requested changes in new commits
- Updates appear automatically in the PR
- Once approved, maintainer handles merge

## 🎓 Learning Resources

To contribute effectively:

1. **Language Syntax**: See [examples/](examples/) directory
2. **Interpreter Design**: Read comments in [nova/interpreter.py](nova/interpreter.py)
3. **Architecture**: Check [DEVELOPMENT.md](DEVELOPMENT.md)
4. **Planned Features**: Review [ROADMAP.md](ROADMAP.md)
5. **Python Best Practices**: https://pep8.org/

## ❓ Questions?

- **Issue Tracker**: Create an issue with your question
- **Code Review**: Ask in PR comments
- **General Discussion**: GitHub Discussions (when enabled)

## 🙌 Recognition

Contributors will be:
- Listed in README.md contributors section
- Mentioned in release notes
- Credited in commit messages

Thank you for contributing to NovaScript! 🚀

---

**Happy Contributing!**

This guide is a living document. Suggest improvements by opening an issue or PR.
