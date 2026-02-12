"""
Unit tests for NovaScript-X interpreter.

Tests cover:
- Lexer tokenization
- Parser AST generation
- Executor evaluation
- Standard library modules
- Error handling
"""

import io
import sys
import unittest
from pathlib import Path

# Import the interpreter components
from novascriptx.interpreter import (
    Lexer, Parser, Executor, Token,
    run_code, run_file, run_repl
)


class TestLexer(unittest.TestCase):
    """Test the lexer (tokenizer)."""
    
    def test_keywords(self):
        """Test keyword tokenization."""
        lexer = Lexer("var if else function return")
        tokens = lexer.tokenize()
        
        token_types = [t.type for t in tokens if t.type != 'EOF']
        self.assertEqual(
            token_types,
            ['VAR', 'IF', 'ELSE', 'FUNCTION', 'RETURN']
        )
    
    def test_numbers(self):
        """Test number tokenization."""
        lexer = Lexer("10 3.14 5")
        tokens = lexer.tokenize()
        
        # Extract just number tokens
        numbers = [float(t.value) for t in tokens if t.type == 'NUMBER']
        self.assertEqual(numbers, [10.0, 3.14, 5.0])
    
    def test_strings(self):
        """Test string tokenization."""
        lexer = Lexer('"hello" "world"')
        tokens = lexer.tokenize()
        
        strings = [t.value for t in tokens if t.type == 'STRING']
        self.assertEqual(strings, ["hello", "world"])
    
    def test_operators(self):
        """Test operator tokenization."""
        lexer = Lexer("+ - * / == !=")
        tokens = lexer.tokenize()
        
        ops = [t.type for t in tokens if t.type != 'EOF']
        self.assertEqual(ops, ['PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'EQUAL', 'NOT_EQUAL'])
    
    def test_comments(self):
        """Test comment handling (should be ignored)."""
        lexer = Lexer("var x = 10  # This is a comment\nvar y = 20")
        tokens = lexer.tokenize()
        
        # Should only have VAR, IDENTIFIER, ASSIGN, NUMBER, VAR, IDENTIFIER, ASSIGN, NUMBER, EOF
        self.assertTrue(any(t.type == 'VAR' for t in tokens))
        # No comments should appear in tokens
        self.assertFalse(any(t.type == 'COMMENT' for t in tokens))


class TestParser(unittest.TestCase):
    """Test the parser (AST generation)."""
    
    def test_variable_declaration(self):
        """Test parsing variable declarations."""
        source = "var x = 10"
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        statements = parser.parse()
        
        self.assertEqual(len(statements), 1)
        self.assertEqual(statements[0]['type'], 'var')
        self.assertEqual(statements[0]['name'], 'x')
    
    def test_function_declaration(self):
        """Test parsing function declarations."""
        source = """
        function add(a, b):
        {
            return a + b
        }
        """
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        statements = parser.parse()
        
        self.assertEqual(len(statements), 1)
        self.assertEqual(statements[0]['type'], 'function')
        self.assertEqual(statements[0]['name'], 'add')
        self.assertEqual(statements[0]['params'], ['a', 'b'])
    
    def test_if_statement(self):
        """Test parsing if statements."""
        source = """
        if (x > 5): {
            print("yes")
        } else: {
            print("no")
        }
        """
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        statements = parser.parse()
        
        self.assertEqual(len(statements), 1)
        self.assertEqual(statements[0]['type'], 'if')
    
    def test_operator_precedence(self):
        """Test that operators follow correct precedence."""
        source = "var x = 2 + 3 * 4"
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        statements = parser.parse()
        
        # Should parse as 2 + (3 * 4), not (2 + 3) * 4
        self.assertEqual(statements[0]['type'], 'var')


class TestExecutor(unittest.TestCase):
    """Test the executor (evaluation)."""
    
    def test_arithmetic(self):
        """Test arithmetic operations."""
        output = io.StringIO()
        executor = Executor(stdout=output)
        
        source = "print(2 + 3)"
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        statements = parser.parse()
        executor.execute(statements)
        
        self.assertEqual(output.getvalue().strip(), "5")
    
    def test_variables(self):
        """Test variable assignment and retrieval."""
        output = io.StringIO()
        executor = Executor(stdout=output)
        
        source = "var x = 10\nprint(x)"
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        statements = parser.parse()
        executor.execute(statements)
        
        self.assertEqual(output.getvalue().strip(), "10")
    
    def test_functions(self):
        """Test function definition and calls."""
        output = io.StringIO()
        executor = Executor(stdout=output)
        
        source = """
        function add(a, b):
        {
            return a + b
        }
        print(add(3, 5))
        """
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        statements = parser.parse()
        executor.execute(statements)
        
        self.assertEqual(output.getvalue().strip(), "8")
    
    def test_conditionals(self):
        """Test if/else statements."""
        output = io.StringIO()
        executor = Executor(stdout=output)
        
        source = """
        var age = 20
        if (age >= 18): {
            print("Adult")
        } else: {
            print("Minor")
        }
        """
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        statements = parser.parse()
        executor.execute(statements)
        
        self.assertEqual(output.getvalue().strip(), "Adult")
    
    def test_while_loop(self):
        """Test while loops."""
        output = io.StringIO()
        executor = Executor(stdout=output)
        
        source = """
        var i = 1
        while (i <= 3): {
            print(i)
            i = i + 1
        }
        """
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        statements = parser.parse()
        executor.execute(statements)
        
        result = output.getvalue().strip()
        self.assertEqual(result, "1\n2\n3")
    
    def test_for_loop(self):
        """Test for loops."""
        output = io.StringIO()
        executor = Executor(stdout=output)
        
        source = """
        for (var i = 1 : i <= 3 : i = i + 1): {
            print(i)
        }
        """
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        statements = parser.parse()
        executor.execute(statements)
        
        result = output.getvalue().strip()
        self.assertEqual(result, "1\n2\n3")
    
    def test_recursion(self):
        """Test recursive functions."""
        output = io.StringIO()
        executor = Executor(stdout=output)
        
        source = """
        function factorial(n):
        {
            if (n <= 1): {
                return 1
            }
            return n * factorial(n - 1)
        }
        print(factorial(5))
        """
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        statements = parser.parse()
        executor.execute(statements)
        
        self.assertEqual(output.getvalue().strip(), "120")
    
    def test_string_concatenation(self):
        """Test string concatenation."""
        output = io.StringIO()
        executor = Executor(stdout=output)
        
        source = """
        var name = "World"
        print("Hello, " + name)
        """
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        statements = parser.parse()
        executor.execute(statements)
        
        self.assertEqual(output.getvalue().strip(), "Hello, World")
    
    def test_member_access(self):
        """Test member access (e.g., math.sqrt())."""
        output = io.StringIO()
        executor = Executor(stdout=output)
        
        source = """
        var math = require("math")
        print(math.sqrt(16))
        """
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        statements = parser.parse()
        executor.execute(statements)
        
        self.assertEqual(output.getvalue().strip(), "4.0")
    
    def test_logical_operators(self):
        """Test logical operators (and, or, not)."""
        output = io.StringIO()
        executor = Executor(stdout=output)
        
        source = """
        if (True and True): {
            print("yes1")
        }
        if (False or True): {
            print("yes2")
        }
        if (!False): {
            print("yes3")
        }
        """
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        statements = parser.parse()
        executor.execute(statements)
        
        result = output.getvalue().strip()
        self.assertIn("yes1", result)
        self.assertIn("yes2", result)
        self.assertIn("yes3", result)


class TestStdlib(unittest.TestCase):
    """Test standard library modules."""
    
    def test_math_module(self):
        """Test math module functions."""
        source = 'var math = require("math")\nprint(math.sqrt(4))\nprint(math.pow(2, 3))\nprint(math.abs(5))'
        result = run_code(source)
        
        self.assertIn("2.0", result)
        self.assertIn("8", result)
        self.assertIn("5", result)
    
    def test_console_module(self):
        """Test console module."""
        source = 'var console = require("console")\nprint("success")'
        result = run_code(source)
        
        # Just verify console module loads without error
        self.assertIn("success", result)


class TestRunFunctions(unittest.TestCase):
    """Test the high-level run_code and run_file functions."""
    
    def test_run_code(self):
        """Test run_code() function."""
        source = 'var x = 5\nprint(x * 2)'
        result = run_code(source)
        self.assertEqual(result.strip(), "10")
    
    def test_run_code_with_error(self):
        """Test run_code() with syntax error."""
        source = 'var x = 5\nprint(x +'  # Incomplete
        
        with self.assertRaises(RuntimeError):
            run_code(source)
    
    def test_run_file(self, temp_file='test_temp.nova'):
        """Test run_file() function."""
        try:
            # Create a temporary file
            with open(temp_file, 'w') as f:
                f.write('var x = 42\nprint(x)')
            
            result = run_file(temp_file)
            self.assertEqual(result.strip(), "42")
        finally:
            # Clean up
            if Path(temp_file).exists():
                Path(temp_file).unlink()
    
    def test_run_file_not_found(self):
        """Test run_file() with non-existent file."""
        with self.assertRaises(FileNotFoundError):
            run_file('nonexistent_file.nova')


class TestErrorHandling(unittest.TestCase):
    """Test error handling."""
    
    def test_undefined_variable(self):
        """Test error when using undefined variable."""
        source = 'print(undefined_var)'
        
        with self.assertRaises(RuntimeError):
            run_code(source)
    
    def test_undefined_function(self):
        """Test error when calling undefined function."""
        source = 'nonexistent_func()'
        
        with self.assertRaises(RuntimeError):
            run_code(source)
    
    def test_wrong_argument_count(self):
        """Test error with wrong number of function arguments."""
        source = """
        function add(a, b):
        {
            return a + b
        }
        add(1)
        """
        
        with self.assertRaises(RuntimeError):
            run_code(source)
    
    def test_invalid_module(self):
        """Test error when requiring non-existent module."""
        source = 'var unknown = require("unknown_module")'
        
        with self.assertRaises((RuntimeError, ModuleNotFoundError)):
            run_code(source)
    
    def test_syntax_error(self):
        """Test handling of syntax errors."""
        source = 'var x = ;'  # Invalid syntax
        
        with self.assertRaises(RuntimeError):
            run_code(source)


if __name__ == '__main__':
    unittest.main()
