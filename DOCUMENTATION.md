# 📚 NovaScript Documentation Index

Complete navigation guide to all NovaScript documentation.

## 🎯 Quick Navigation

**New to NovaScript?** Start here in order:
1. [Installation & Quick Start](#installation--quick-start)
2. [CLI Usage Guide](#cli-usage-guide)
3. [Language Syntax](#language-syntax)
4. [Working Examples](#working-examples)

**Want to Contribute?**
1. Read [CONTRIBUTING.md](CONTRIBUTING.md)
2. Check [ROADMAP.md](ROADMAP.md) for feature areas
3. Review [DEVELOPMENT.md](DEVELOPMENT.md) for architecture

**Building with NovaScript?**
1. [QUICK_REFERENCE.md](QUICK_REFERENCE.md) - Syntax quick reference
2. [Standard Library](#standard-library)
3. [Examples](#working-examples)

---

## 📖 Main Documentation Files

### For Users

| File | Purpose | Best For |
|------|---------|----------|
| [README.md](README.md) | Complete user guide and reference | Learning NovaScript, getting started |
| [QUICK_REFERENCE.md](QUICK_REFERENCE.md) | Syntax and CLI quick reference | Looking up syntax, CLI commands |
| [examples/](examples/) | Working code samples | Learning by example |
| [examples/README.md](examples/README.md) | Example guide | Understanding example programs |

### For Developers & Contributors

| File | Purpose | Best For |
|------|---------|----------|
| [DEVELOPMENT.md](DEVELOPMENT.md) | Architecture and development setup | Understanding codebase, adding features |
| [ROADMAP.md](ROADMAP.md) | Feature timeline and future plans | Planning contributions, understanding direction |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Contribution guidelines | Making contributions, reporting issues |

---

## 🚀 Installation & Quick Start

### Installation

```bash
# Clone repository
git clone https://github.com/PixelStudio330/NovaScript.git
cd NovaScript

# Install (development mode recommended)
pip install -e .

# Verify installation
nova --version   # Should show: NovaScript 1.0.0
```

### First Program

```bash
# Run example
nova examples/hello_world/main.nova

# Or create your own
echo 'print("Hello, Nova!");' > hello.nova
nova hello.nova
```

See [README.md](README.md#installation) for complete installation guide.

---

## 💻 CLI Usage Guide

### Available Commands

```bash
# Execute a script
nova script.nova

# Interactive REPL
nova

# Run code directly
nova -c 'print(5 + 3)'

# Watch mode (auto-reload on file changes)
nova --watch script.nova

# Debug mode (show parse tree)
nova --debug script.nova

# Show help
nova --help
nova -h

# Show version
nova --version
nova -v
```

See [QUICK_REFERENCE.md](QUICK_REFERENCE.md#cli-commands) for detailed CLI reference.

---

## 📝 Language Syntax

### Variables & Functions

```nova
var x = 10;
var name = "Alice";

function greet(name) {
    return "Hello, " + name;
}

print(greet(name));  # Hello, Alice
```

### Control Flow

```nova
if (x > 0) {
    print("positive");
} else {
    print("non-positive");
}

while (x > 0) {
    print(x);
    x = x - 1;
}

for (i = 0; i < 5; i = i + 1) {
    print(i);
}
```

See [QUICK_REFERENCE.md](QUICK_REFERENCE.md#language-syntax) for complete syntax guide.

---

## 📚 Standard Library

### Available Modules

Load modules with `require()`:

```nova
var fs = require("fs");
var console = require("console");
var math = require("math");
var random = require("random");
var date = require("date");
var http = require("http");
```

### Module Reference

| Module | Purpose | Examples |
|--------|---------|----------|
| **fs** | File operations | read, write, delete files |
| **console** | Logging output | log, warn, error, info, debug |
| **math** | Math functions | sqrt, pow, floor, ceil, sin, cos, pi, e |
| **random** | Random numbers | randInt, choice, shuffle, seed |
| **date** | Date/time | now, format, getYear, addDays |
| **http** | HTTP requests | get, post, put, delete |

See [README.md](README.md#standard-library) for complete stdlib reference.

See [QUICK_REFERENCE.md](QUICK_REFERENCE.md#standard-library) for quick stdlib reference.

---

## 💡 Working Examples

All examples are in [examples/](examples/) directory:

### [hello_world/](examples/hello_world/)
**Basics of variables, output, and arithmetic**
- Variables with different types
- String concatenation
- Basic arithmetic
- Using print()

```bash
nova examples/hello_world/main.nova
```

### [functions_loops/](examples/functions_loops/)
**Functions, recursion, and loops**
- Function definition and calling
- Return statements
- Recursion (factorial, Fibonacci)
- For and while loops
- Nested loops
- Conditionals

```bash
nova examples/functions_loops/main.nova
```

### [stdlib_demo/](examples/stdlib_demo/)
**Using standard library modules**
- Loading modules with require()
- Accessing module functions
- Comments about v1.1+ features

```bash
nova examples/stdlib_demo/main.nova
```

See [examples/README.md](examples/README.md) for detailed example guide.

---

## 🔧 Architecture Overview

### Interpreter Components

**Lexer** → **Parser** → **AST** → **Executor**

```
Source Code
    ↓
[Lexer]  → Tokens (keywords, operators, values)
    ↓
[Parser] → AST (syntax tree)
    ↓
[Executor] → Output
```

### Package Structure

```
nova/
├── __init__.py          # Main package
├── interpreter.py       # Lexer, Parser, Executor (923 lines)
└── stdlib/              # Standard library modules
    ├── fs.py
    ├── console.py
    ├── math.py
    ├── random.py
    ├── date.py
    └── http.py

nova_cli.py             # CLI entry point
setup.py                # Installation config
```

See [DEVELOPMENT.md](DEVELOPMENT.md#architecture) for detailed architecture.

---

## 🗺️ Roadmap & Features

### Version 1.0.0 (Released ✅)
- ✅ Core interpreter
- ✅ CLI runtime
- ✅ 6 stdlib modules
- ✅ require() function
- ✅ Full documentation

### Version 1.1.0 (In Planning)
- 🚧 Member access (dot notation)
- 🚧 Arrays/lists
- 🚧 Objects/dictionaries

### Version 1.2.0 (Planned)
- 📋 Web server (`--serve`)
- 📋 Web framework
- 📋 Routing system

### Version 2.0.0 (Future)
- 🔮 Module system (import/export)
- 🔮 Classes and OOP
- 🔮 Async/await
- 🔮 Package manager

See [ROADMAP.md](ROADMAP.md) for complete roadmap with detailed features and timeline.

---

## 🤝 Contributing

### Want to Help?

1. **Read** [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines
2. **Check** [ROADMAP.md](ROADMAP.md) for feature areas
3. **Understand** [DEVELOPMENT.md](DEVELOPMENT.md) for architecture
4. **Make** a Pull Request!

### Contribution Areas

- 🐛 **Bug Fixes**: Report and fix issues
- ✨ **Features**: Implement planned features
- 📚 **Documentation**: Improve guides and examples
- 🧪 **Tests**: Add test coverage
- 🌍 **Platform Support**: Test on different OS

See [CONTRIBUTING.md](CONTRIBUTING.md#what-can-you-contribute) for more areas.

---

## ❓ FAQ

### How do I install NovaScript?

See [Installation & Quick Start](#installation--quick-start) above, or [README.md](README.md#installation) for detailed steps.

### How do I use the CLI?

See [CLI Usage Guide](#cli-usage-guide) above, or [QUICK_REFERENCE.md](QUICK_REFERENCE.md#cli-commands) for detailed commands.

### What syntax does NovaScript support?

See [Language Syntax](#language-syntax) above, or [QUICK_REFERENCE.md](QUICK_REFERENCE.md#language-syntax) for complete reference.

### How do I load modules?

Use `require()`:
```nova
var math = require("math");
var result = math.sqrt(16);  # Planned for v1.1: dot notation
```

Current workaround for v1.0: See [examples/stdlib_demo/](examples/stdlib_demo/) for examples.

### What features are planned?

See [ROADMAP.md](ROADMAP.md) for complete feature roadmap through v2.0+.

### How do I contribute?

See [CONTRIBUTING.md](CONTRIBUTING.md) for step-by-step contribution guide.

### Where are the examples?

All examples are in [examples/](examples/) directory. See [examples/README.md](examples/README.md) for guide.

### What's the architecture?

See [DEVELOPMENT.md](DEVELOPMENT.md#architecture) for detailed architecture explanation.

---

## 📞 Support

### Documentation Issues?
- Check the relevant markdown file above
- Use Ctrl+F to search for topics
- See [FAQ](#faq) section above

### Reporting Bugs?
- Create an issue on GitHub with reproduction steps
- See [CONTRIBUTING.md](CONTRIBUTING.md#1-create-an-issue-first) for bug report format

### Want to Contribute?
- Start with [CONTRIBUTING.md](CONTRIBUTING.md)
- Check [ROADMAP.md](ROADMAP.md) for feature areas
- Ask questions in issues or pull requests

### Looking for Examples?
- See [examples/](examples/) directory
- See [QUICK_REFERENCE.md](QUICK_REFERENCE.md#common-patterns) for common patterns
- See [README.md](README.md) for detailed examples

---

## 📋 Documentation Stats

| Document | Lines | Purpose |
|----------|-------|---------|
| README.md | 734 | Complete user guide |
| QUICK_REFERENCE.md | 400+ | Syntax and CLI reference |
| ROADMAP.md | 450+ | Feature roadmap v1.0-v2.0+ |
| DEVELOPMENT.md | 400+ | Architecture and development |
| CONTRIBUTING.md | 500+ | Contribution guidelines |
| examples/README.md | 90+ | Example programs guide |

**Total Documentation**: 2500+ lines covering every aspect of NovaScript.

---

## 🎓 Learning Path

### Beginner
1. Read [README.md](README.md#quick-start)
2. Run [examples/hello_world/](examples/hello_world/)
3. Review [QUICK_REFERENCE.md](QUICK_REFERENCE.md#language-syntax)
4. Modify examples to learn

### Intermediate
1. Study [examples/functions_loops/](examples/functions_loops/)
2. Review [Standard Library](#standard-library) section
3. Build small programs using stdlib modules
4. Check [QUICK_REFERENCE.md](QUICK_REFERENCE.md#standard-library)

### Advanced
1. Read [DEVELOPMENT.md](DEVELOPMENT.md)
2. Study [nova/interpreter.py](nova/interpreter.py)
3. Check [ROADMAP.md](ROADMAP.md) for features to implement
4. Make contributions following [CONTRIBUTING.md](CONTRIBUTING.md)

---

## Version Info

- **Current Version**: 1.0.0 (Beta)
- **Last Updated**: February 2026
- **Status**: Core runtime complete, web framework in development
- **Python Version**: 3.7+
- **Platforms**: Windows, macOS, Linux

---

## 🚀 Next Steps

- **Using NovaScript**: Install and run [examples/hello_world/](examples/hello_world/)
- **Learning Language**: Study [examples/functions_loops/](examples/functions_loops/)
- **Building Apps**: Use [Standard Library](#standard-library) modules
- **Contributing**: Follow [CONTRIBUTING.md](CONTRIBUTING.md)
- **Planning Ahead**: Check [ROADMAP.md](ROADMAP.md)

---

**Happy scripting with NovaScript!** 🎉

For questions or issues, refer to the relevant documentation file above or create an issue on GitHub.
