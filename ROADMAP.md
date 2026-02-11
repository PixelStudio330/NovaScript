# NovaScript Roadmap

A comprehensive roadmap for NovaScript's development from v1.0 through v2.0 and beyond.

## Version Timeline

```
v1.0.0 (RELEASED) ────► v1.1.0 ────► v1.2.0 ────► v1.3.0 ────► v2.0.0
Core Runtime     Member Access  Web Server  Advanced   Production
Only            + Objects       Framework   Features   Ready
```

---

## 🎯 v1.0.0 - Core Runtime (RELEASED)

**Status**: ✅ Complete and Tested  
**Release Date**: February 2026

### Features
- ✅ Lexer, Parser, Executor interpreter
- ✅ CLI with file execution, REPL, watch mode
- ✅ 6 standard library modules (fs, console, math, random, date, http)
- ✅ require() function for module loading
- ✅ Functions, variables, control flow, operators
- ✅ Recursion support
- ✅ 3 working examples
- ✅ Comprehensive documentation

### Technical Achievements
- 923-line interpreter with clean API
- 212-line CLI with argparse
- Modular stdlib design
- Cross-platform support

---

## 🚀 v1.1.0 - Member Access & Data Structures

**Target Timeline**: Q2 2026  
**Estimated Work**: 2-3 weeks

### Core Features

#### 1. **Member Access (Dot Notation)** [HIGH PRIORITY]
- **Goal**: `math.sqrt(16)` syntax
- **Work Required**:
  - Parser: Enhance `parse_primary()` to handle DOT token
  - AST: Create member_access node type
  - Executor: Evaluate member access
  - Builtin functions: Return objects with properties
- **Breaking Changes**: None (backward compatible)
- **Testing**: 
  - `var math = require("math"); print(math.sqrt(16))`
  - `var obj = {x: 10}; print(obj.x)` (after object support)

#### 2. **Arrays/Lists** [HIGH PRIORITY]
- **Goal**: `var arr = [1, 2, 3]; print(arr[0])`
- **Work Required**:
  - Parser: Handle `[` `]` in parse_primary()
  - AST: array_literal node type
  - Executor: Python list storage
  - Index access: `arr[index]` syntax
  - Slice support: `arr[0:2]`
- **Breaking Changes**: None
- **Methods to Add**:
  - `length` property
  - `push(item)`
  - `pop()`
  - `shift()`
  - `unshift()`
  - `join(separator)`
  - `slice(start, end)`
  - `map(fn)` - for loops over arrays
  - `filter(fn)`
  - `reduce(fn)`
- **Testing**:
  ```nova
  var arr = [1, 2, 3, 4, 5];
  print(arr[0]);        # 1
  print(arr.length);    # 5
  arr.push(6);
  print(arr);
  ```

#### 3. **Objects/Dictionaries** [HIGH PRIORITY]
- **Goal**: `var config = {name: "Nova", version: 1}`
- **Work Required**:
  - Parser: Handle `{key: value}` syntax
  - AST: object_literal node type
  - Executor: Python dict storage
  - Property access: `obj.key` or `obj["key"]`
  - Property assignment: `obj.key = value`
- **Breaking Changes**: None
- **Methods to Add**:
  - `keys()` - return array of keys
  - `values()` - return array of values
  - `has(key)` - check key existence
  - `delete(key)` - remove property
  - `type()` - return "object"
- **Testing**:
  ```nova
  var person = {name: "Alice", age: 30};
  print(person.name);      # Alice
  person.age = 31;
  print(person["name"]);   # Alice
  ```

### Supporting Work
- Update stdlib modules to return proper objects
- Enhance require() to return callable objects
- Update examples to show object usage
- Update README with syntax documentation
- Backwards compatibility testing

### Files to Modify
- `nova/interpreter.py`: Parser member access, array support, object support
- `examples/`: New examples using arrays and objects
- `README.md`: Document new syntax
- Test suite: Add comprehensive tests

### Success Criteria
- ✅ Member access works: `math.sqrt(16)`
- ✅ Arrays fully functional with all methods
- ✅ Objects fully functional with property access
- ✅ All existing features still work
- ✅ Examples updated to show new features

---

## 🌐 v1.2.0 - Web Server & Web Framework

**Target Timeline**: Q3 2026  
**Estimated Work**: 4-5 weeks

### Core Features

#### 1. **Web Server Runtime** [HIGH PRIORITY]
- **Goal**: `nova --serve app.nova`
- **Work Required**:
  - Create `nova/web/` module
  - Implement HTTP server framework
  - Route definition syntax
  - Request/response handling
  - Port configuration
- **Breaking Changes**: None (new feature)
- **Features**:
  - Route matching: `@route('/path')`
  - HTTP methods: GET, POST, PUT, DELETE
  - Query parameters
  - Request body parsing (JSON)
  - Response types: HTML, JSON, plain text
  - Status codes: 200, 404, 500, etc.
- **Testing**:
  ```nova
  server.get('/', function(req, res): {
      res.send("Hello World!");
  });

  server.post('/api/data', function(req, res): {
      res.json({status: "ok", received: req.body});
  });

  server.listen(3000);
  ```

#### 2. **Web Framework (nova-web)** [MEDIUM PRIORITY]
- **Goal**: `nova create myapp`
- **Folder Structure**:
  ```
  myapp/
  ├── app.nova       # Main app entry point
  ├── routes/
  │   ├── home.nova
  │   └── api.nova
  ├── pages/
  │   ├── home.html
  │   └── about.html
  ├── public/
  │   └── style.css
  └── package.nova   # Package config
  ```
- **Features**:
  - Project scaffolding
  - Server-side rendering
  - Static file serving
  - Template support
  - Hot reload in development
  - Build for production

#### 3. **HTTP Utilities** [MEDIUM PRIORITY]
- Session management: `req.session`
- Cookie handling: `res.cookies`
- Middleware system
- Request validation
- Response compression
- CORS support

### Supporting Work
- HTTP server implementation using Python's `http.server`
- Route matching algorithm
- Request parsing library
- Template rendering engine
- Asset bundling for CSS/JavaScript

### Files to Create
- `nova/web/__init__.py` - Web framework exports
- `nova/web/server.py` - HTTP server implementation
- `nova/web/router.py` - Route matching
- `nova/web/request.py` - Request object
- `nova/web/response.py` - Response object
- `nova_cli.py` - Add --serve command
- Example web apps

### Success Criteria
- ✅ Web server starts correctly
- ✅ Routes match and execute
- ✅ Request/response work properly
- ✅ JSON parsing and response works
- ✅ Static files served
- ✅ Hot reload works in development

---

## 🛠️ v1.3.0 - Advanced Features & Polish

**Target Timeline**: Q4 2026  
**Estimated Work**: 3-4 weeks

### Language Features

#### 1. **Error Handling**
- Try/catch syntax
- Finally blocks
- Custom error types
- Stack traces with line numbers
- Better error messages

Example:
```nova
try {
    var result = mayFail();
} catch (error) {
    console.error("Error: " + error.message);
} finally {
    console.log("Cleanup");
}
```

#### 2. **String Enhancements**
- Template literals: `` `Hello ${name}` ``
- Multi-line strings
- String methods: split, trim, toUpper, toLower, etc.
- Regular expressions (basic)

#### 3. **More Standard Library Modules**
- **json**: JSON encode/decode
- **string**: String manipulation utilities
- **url**: URL parsing and building
- **path**: File path utilities
- **os**: Environment variables, platform detection
- **crypto**: Basic hashing (MD5, SHA1)
- **stream**: Stream processing

#### 4. **Language Improvements**
- Better error messages with code context
- Line numbers in error traces
- Type checking/inference
- Performance optimizations
- Memory management improvements

### Framework Enhancements
- Middleware chains
- Request validation library
- Database abstraction layer
- Authentication helpers
- Testing framework

### Files to Modify
- `nova/interpreter.py` - Error handling, string features
- `nova/stdlib/` - New modules
- `nova/web/` - Middleware, validation
- Examples: Error handling demo

### Success Criteria
- ✅ Try/catch fully functional
- ✅ Detailed error messages with context
- ✅ 6+ new stdlib modules
- ✅ String features working
- ✅ Performance >= v1.2

---

## 📦 v2.0.0 - Production Ready

**Target Timeline**: Q1 2027  
**Estimated Work**: 6-8 weeks

### Major Features

#### 1. **Module System**
- Multi-file projects
- Package structure
- Import/export syntax
- Circular dependency handling
- Module caching

Example:
```nova
// utils.nova
export function helper(): {
    return "help";
}

// main.nova
import helper from "utils";
print(helper());
```

#### 2. **Classes & OOP**
- Class definitions
- Constructors
- Methods
- Properties
- Inheritance
- Static methods

Example:
```nova
class Animal {
    function init(name): {
        this.name = name;
    }
    
    function speak(): {
        return this.name + " speaks";
    }
}

var dog = new Animal("Dog");
print(dog.speak());
```

#### 3. **Async/Await**
- Promise support
- Async functions
- Await expressions
- Error handling in async

Example:
```nova
async function fetchData(): {
    var response = await fetch("http://api.example.com");
    return response.json();
}
```

#### 4. **Package Manager (nova-pkg)**
- Dependency installation: `nova install package-name`
- Package registry
- Version management
- Dependency resolution
- Lock files

Commands:
```bash
nova install package-name      # Install package
nova install                   # Install all dependencies
nova search keyword            # Search packages
nova publish                   # Publish to registry
nova update package-name       # Update package
```

#### 5. **Build Tools**
- Bundler: Combine modules into single file
- Minifier: Reduce file size
- Source maps: Debug bundled code
- Tree shaking: Remove unused code

Commands:
```bash
nova build                     # Build for production
nova watch                     # Watch and rebuild
nova bundle app.nova           # Create bundle
```

### Framework Enhancements
- Full-featured web framework
- Database ORM
- Authentication/authorization
- Rate limiting
- Caching layer
- Logging framework

### Performance
- Performance profiler
- Memory leak detection
- Code optimization
- Caching improvements

### Files to Create/Modify
- Language grammar changes
- Parser enhancements for classes
- New executor scope for classes
- Module loader implementation
- Package manager CLI
- Build tools

### Success Criteria
- ✅ Classes fully functional with inheritance
- ✅ Multi-file projects work
- ✅ Async/await operational
- ✅ Package manager functional
- ✅ Build tools working
- ✅ Performance benchmarks met
- ✅ Production-ready stability

---

## 🗺️ Long-term Vision (v2.0+)

### Ecosystem Development
- **EditorConfig**: VS Code extension with syntax highlighting, debugging
- **Documentation**: Comprehensive language guide
- **Community**: Forum, GitHub discussions
- **Tutorials**: Step-by-step learning guides
- **Packages**: Standard library of community packages

### Platform Expansion
- **Mobile**: Run NovaScript on iOS/Android
- **Embedded**: IoT device support
- **CLI Tools**: Build command-line tools with Nova
- **Games**: Game development framework

### Language Evolution
- **Type System**: Static typing support (optional)
- **Macros**: Meta-programming capabilities
- **Custom Operators**: User-defined operators
- **Domain-specific Features**: Optimized for web, data science, etc.

---

## 📊 Progress Tracking

### Version 1.0.0
- [x] Core interpreter
- [x] CLI runtime
- [x] Standard library (6 modules)
- [x] Module system (require)
- [x] Documentation
- [x] Examples

**Status**: ✅ COMPLETE

### Version 1.1.0
- [ ] Member access (dot notation)
- [ ] Arrays/lists
- [ ] Objects/dictionaries
- [ ] Updated examples
- [ ] Updated documentation

**Status**: 🚧 IN PLANNING

### Version 1.2.0
- [ ] Web server
- [ ] Web framework
- [ ] Web examples
- [ ] Routing system

**Status**: 📋 PLANNED

### Version 1.3.0+
- [ ] Error handling (try/catch)
- [ ] More stdlib modules
- [ ] Language improvements
- [ ] Performance optimization

**Status**: 🔮 FUTURE

### Version 2.0.0
- [ ] Module system (import/export)
- [ ] Classes and OOP
- [ ] Async/await
- [ ] Package manager
- [ ] Build tools

**Status**: 🔮 FUTURE

---

## 🚦 Development Process

### For Each Version
1. **Planning**: Define features and scope
2. **Design**: Architecture and API design
3. **Implementation**: Write code with tests
4. **Testing**: Unit and integration tests
5. **Documentation**: Update guides and examples
6. **Release**: Version bump, changelog, GitHub release
7. **Feedback**: Collect user feedback for next version

### Release Checklist
- [ ] All features implemented
- [ ] Tests passing
- [ ] Documentation complete
- [ ] Examples working
- [ ] Performance tested
- [ ] Security reviewed
- [ ] Changelog written
- [ ] Version bumped
- [ ] GitHub release created
- [ ] Announcement to community

---

## 💡 Design Principles

1. **Simplicity**: Easy to learn and use
2. **Consistency**: Predictable syntax and behavior
3. **Compatibility**: Backward compatible when possible
4. **Performance**: Fast startup and execution
5. **Elegance**: Clean, readable code
6. **Extensibility**: Easy to add new features

---

## 📅 Estimated Timeline

```
Feb 2026: v1.0.0 Released ✅
Mar-Apr 2026: v1.1.0 Development
May 2026: v1.1.0 Released
May-Jul 2026: v1.2.0 Development  
Aug 2026: v1.2.0 Released
Sep-Oct 2026: v1.3.0 Development
Nov 2026: v1.3.0 Released
Dec 2026 - Jan 2027: v2.0.0 Development
Feb 2027: v2.0.0 Released
```

This timeline is subject to change based on community feedback and available resources.

---

## 🤝 Contributing

Community contributions are welcome! Check [DEVELOPMENT.md](DEVELOPMENT.md) for contribution guidelines.

Priority areas for contributions:
- Standard library modules (v1.3+)
- Documentation and examples
- Bug fixes and optimizations
- Community packages (v2.0+)

---

**Last Updated**: February 2026  
**Next Review**: May 2026 (after v1.1.0 planning finalized)
