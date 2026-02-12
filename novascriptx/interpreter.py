#!/usr/bin/env python3
"""
NovaScript Interpreter (Refactored for CLI and Web Runtime)
A Python-based interpreter for the NovaScript programming language.
Supports variables, functions, loops, conditionals, arithmetic operations, and more.

Features:
- Variables (var)
- Functions with return statements
- Print statements
- If/else conditionals
- While and for loops
- Arithmetic and comparison operators
- Logical operators (and, or, not)
- String concatenation with type coercion
- Recursion support
- Module system (require)
"""

import re
import sys
import io
from typing import Any, Dict, List, Optional, Tuple

__version__ = "1.0.0"


# ============================================================================
# LEXER: Tokenizes NovaScript source code
# ============================================================================

class Token:
    """Represents a single token in the source code."""
    
    def __init__(self, token_type: str, value: str, line: int = 0):
        self.type = token_type
        self.value = value
        self.line = line
    
    def __repr__(self):
        return f"Token({self.type}, {self.value!r})"


class Lexer:
    """Tokenizes NovaScript source code into a stream of tokens."""
    
    # Keywords recognized by NovaScript
    KEYWORDS = {
        'var': 'VAR',
        'function': 'FUNCTION',
        'print': 'PRINT',
        'if': 'IF',
        'else': 'ELSE',
        'for': 'FOR',
        'while': 'WHILE',
        'return': 'RETURN',
        'in': 'IN',
        'True': 'TRUE',
        'False': 'FALSE',
    }
    
    def __init__(self, source: str):
        self.source = source
        self.position = 0
        self.line = 1
        self.tokens: List[Token] = []
    
    def error(self, message: str):
        """Raise a lexer error."""
        raise SyntaxError(f"Lexer error at line {self.line}: {message}")
    
    def peek(self, offset: int = 0) -> Optional[str]:
        """Look at character without consuming it."""
        pos = self.position + offset
        if pos < len(self.source):
            return self.source[pos]
        return None
    
    def advance(self) -> Optional[str]:
        """Consume and return the next character."""
        if self.position < len(self.source):
            char = self.source[self.position]
            if char == '\n':
                self.line += 1
            self.position += 1
            return char
        return None
    
    def skip_whitespace(self):
        """Skip whitespace characters (but track newlines for line counting)."""
        while self.peek() and self.peek() in ' \t\n\r':
            self.advance()
    
    def skip_comment(self):
        """Skip comments starting with #."""
        if self.peek() == '#':
            while self.peek() and self.peek() != '\n':
                self.advance()
            if self.peek() == '\n':
                self.advance()
    
    def read_string(self, quote_char: str) -> str:
        """Read a string literal."""
        value = ""
        self.advance()  # Skip opening quote
        while self.peek() and self.peek() != quote_char:
            if self.peek() == '\\':
                self.advance()
                next_char = self.advance()
                if next_char == 'n':
                    value += '\n'
                elif next_char == 't':
                    value += '\t'
                elif next_char == 'r':
                    value += '\r'
                elif next_char == '\\':
                    value += '\\'
                else:
                    value += next_char
            else:
                value += self.advance()
        
        if self.peek() != quote_char:
            self.error("Unterminated string")
        self.advance()  # Skip closing quote
        return value
    
    def read_number(self) -> str:
        """Read a numeric literal."""
        value = ""
        while self.peek() and (self.peek().isdigit() or self.peek() == '.'):
            value += self.advance()
        return value
    
    def read_identifier(self) -> str:
        """Read an identifier or keyword."""
        value = ""
        while self.peek() and (self.peek().isalnum() or self.peek() == '_'):
            value += self.advance()
        return value
    
    def tokenize(self) -> List[Token]:
        """Tokenize the entire source code."""
        while self.position < len(self.source):
            self.skip_whitespace()
            
            if self.position >= len(self.source):
                break
            
            # Skip comments
            if self.peek() == '#':
                self.skip_comment()
                continue
            
            char = self.peek()
            line = self.line
            
            # String literals
            if char in '"\'':
                value = self.read_string(char)
                self.tokens.append(Token('STRING', value, line))
            
            # Numbers
            elif char.isdigit():
                value = self.read_number()
                self.tokens.append(Token('NUMBER', value, line))
            
            # Identifiers and keywords
            elif char.isalpha() or char == '_':
                value = self.read_identifier()
                token_type = self.KEYWORDS.get(value, 'IDENTIFIER')
                self.tokens.append(Token(token_type, value, line))
            
            # Operators and punctuation
            elif char == '+':
                self.advance()
                self.tokens.append(Token('PLUS', '+', line))
            elif char == '-':
                self.advance()
                self.tokens.append(Token('MINUS', '-', line))
            elif char == '*':
                self.advance()
                self.tokens.append(Token('MULTIPLY', '*', line))
            elif char == '/':
                self.advance()
                self.tokens.append(Token('DIVIDE', '/', line))
            elif char == '%':
                self.advance()
                self.tokens.append(Token('MODULO', '%', line))
            elif char == '=':
                self.advance()
                if self.peek() == '=':
                    self.advance()
                    self.tokens.append(Token('EQUAL', '==', line))
                else:
                    self.tokens.append(Token('ASSIGN', '=', line))
            elif char == '!':
                self.advance()
                if self.peek() == '=':
                    self.advance()
                    self.tokens.append(Token('NOT_EQUAL', '!=', line))
                else:
                    self.tokens.append(Token('NOT', '!', line))
            elif char == '<':
                self.advance()
                if self.peek() == '=':
                    self.advance()
                    self.tokens.append(Token('LESS_EQUAL', '<=', line))
                else:
                    self.tokens.append(Token('LESS', '<', line))
            elif char == '>':
                self.advance()
                if self.peek() == '=':
                    self.advance()
                    self.tokens.append(Token('GREATER_EQUAL', '>=', line))
                else:
                    self.tokens.append(Token('GREATER', '>', line))
            elif char == '(':
                self.advance()
                self.tokens.append(Token('LPAREN', '(', line))
            elif char == ')':
                self.advance()
                self.tokens.append(Token('RPAREN', ')', line))
            elif char == '{':
                self.advance()
                self.tokens.append(Token('LBRACE', '{', line))
            elif char == '}':
                self.advance()
                self.tokens.append(Token('RBRACE', '}', line))
            elif char == '[':
                self.advance()
                self.tokens.append(Token('LBRACKET', '[', line))
            elif char == ']':
                self.advance()
                self.tokens.append(Token('RBRACKET', ']', line))
            elif char == ',':
                self.advance()
                self.tokens.append(Token('COMMA', ',', line))
            elif char == ':':
                self.advance()
                self.tokens.append(Token('COLON', ':', line))
            elif char == '.':
                self.advance()
                self.tokens.append(Token('DOT', '.', line))
            else:
                self.error(f"Unexpected character: {char!r}")
        
        self.tokens.append(Token('EOF', '', line))
        return self.tokens


# ============================================================================
# PARSER: Parses tokens into executable statements
# ============================================================================

class Parser:
    """Parses tokens into a list of executable statements."""
    
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.position = 0
    
    def error(self, message: str):
        """Raise a parser error."""
        token = self.current_token()
        raise SyntaxError(f"Parser error at line {token.line}: {message}")
    
    def current_token(self) -> Token:
        """Get the current token."""
        if self.position < len(self.tokens):
            return self.tokens[self.position]
        return self.tokens[-1]  # EOF token
    
    def peek_token(self, offset: int = 1) -> Token:
        """Look ahead at a token."""
        pos = self.position + offset
        if pos < len(self.tokens):
            return self.tokens[pos]
        return self.tokens[-1]
    
    def advance(self) -> Token:
        """Consume and return the current token."""
        token = self.current_token()
        if token.type != 'EOF':
            self.position += 1
        return token
    
    def expect(self, token_type: str) -> Token:
        """Consume a token of the expected type or raise an error."""
        token = self.current_token()
        if token.type != token_type:
            self.error(f"Expected {token_type}, got {token.type}")
        return self.advance()
    
    def parse(self) -> List[Dict[str, Any]]:
        """Parse the token stream into statements."""
        statements = []
        while self.current_token().type != 'EOF':
            stmt = self.parse_statement()
            if stmt:
                statements.append(stmt)
        return statements
    
    def parse_statement(self) -> Optional[Dict[str, Any]]:
        """Parse a single statement."""
        token_type = self.current_token().type
        
        if token_type == 'VAR':
            return self.parse_var_declaration()
        elif token_type == 'FUNCTION':
            return self.parse_function_declaration()
        elif token_type == 'PRINT':
            return self.parse_print()
        elif token_type == 'IF':
            return self.parse_if()
        elif token_type == 'WHILE':
            return self.parse_while()
        elif token_type == 'FOR':
            return self.parse_for()
        elif token_type == 'RETURN':
            return self.parse_return()
        elif token_type == 'IDENTIFIER':
            return self.parse_assignment_or_call()
        else:
            self.error(f"Unexpected token: {token_type}")
    
    def parse_var_declaration(self) -> Dict[str, Any]:
        """Parse: var x = value"""
        self.expect('VAR')
        name = self.expect('IDENTIFIER').value
        self.expect('ASSIGN')
        value = self.parse_expression()
        return {'type': 'var', 'name': name, 'value': value}
    
    def parse_function_declaration(self) -> Dict[str, Any]:
        """Parse: function name(args): body"""
        self.expect('FUNCTION')
        name = self.expect('IDENTIFIER').value
        self.expect('LPAREN')
        
        # Parse parameters
        params = []
        while self.current_token().type != 'RPAREN':
            params.append(self.expect('IDENTIFIER').value)
            if self.current_token().type == 'COMMA':
                self.advance()
        
        self.expect('RPAREN')
        self.expect('COLON')
        
        # Parse function body
        body = self.parse_block()
        
        return {'type': 'function', 'name': name, 'params': params, 'body': body}
    
    def parse_block(self) -> List[Dict[str, Any]]:
        """Parse a block of statements (indented or in braces)."""
        statements = []
        
        # Handle brace-based blocks
        if self.current_token().type == 'LBRACE':
            self.advance()
            while self.current_token().type != 'RBRACE':
                stmt = self.parse_statement()
                if stmt:
                    statements.append(stmt)
            self.expect('RBRACE')
        else:
            # Handle single statement or indented block
            stmt = self.parse_statement()
            if stmt:
                statements.append(stmt)
        
        return statements
    
    def parse_print(self) -> Dict[str, Any]:
        """Parse: print(expression)"""
        self.expect('PRINT')
        self.expect('LPAREN')
        value = self.parse_expression()
        self.expect('RPAREN')
        return {'type': 'print', 'value': value}
    
    def parse_if(self) -> Dict[str, Any]:
        """Parse: if (condition): body else: body"""
        self.expect('IF')
        self.expect('LPAREN')
        condition = self.parse_expression()
        self.expect('RPAREN')
        self.expect('COLON')
        
        then_body = self.parse_block()
        
        else_body = []
        if self.current_token().type == 'ELSE':
            self.advance()
            self.expect('COLON')
            else_body = self.parse_block()
        
        return {'type': 'if', 'condition': condition, 'then': then_body, 'else': else_body}
    
    def parse_while(self) -> Dict[str, Any]:
        """Parse: while (condition): body"""
        self.expect('WHILE')
        self.expect('LPAREN')
        condition = self.parse_expression()
        self.expect('RPAREN')
        self.expect('COLON')
        
        body = self.parse_block()
        
        return {'type': 'while', 'condition': condition, 'body': body}
    
    def parse_for(self) -> Dict[str, Any]:
        """Parse: for (var i = 0 : i < 10 : i = i + 1): body"""
        self.expect('FOR')
        self.expect('LPAREN')
        
        # Initialize
        init = None
        if self.current_token().type == 'VAR':
            init = self.parse_var_declaration()
        
        self.expect('COLON')
        
        # Condition
        condition = self.parse_expression()
        
        self.expect('COLON')
        
        # Update
        update = self.parse_assignment_or_call()
        
        self.expect('RPAREN')
        self.expect('COLON')
        
        body = self.parse_block()
        
        return {
            'type': 'for',
            'init': init,
            'condition': condition,
            'update': update,
            'body': body
        }
    
    def parse_return(self) -> Dict[str, Any]:
        """Parse: return value"""
        self.expect('RETURN')
        
        # Handle optional return value
        value = None
        if self.current_token().type not in ['EOF', 'RBRACE']:
            value = self.parse_expression()
        
        return {'type': 'return', 'value': value}
    
    def parse_assignment_or_call(self) -> Dict[str, Any]:
        """Parse assignment or function call."""
        expr = self.parse_expression()
        
        if self.current_token().type == 'ASSIGN':
            self.advance()
            value = self.parse_expression()
            return {'type': 'assignment', 'target': expr, 'value': value}
        
        return {'type': 'expression', 'value': expr}
    
    def parse_expression(self) -> Dict[str, Any]:
        """Parse expressions with operator precedence."""
        return self.parse_or()
    
    def parse_or(self) -> Dict[str, Any]:
        """Parse logical OR."""
        left = self.parse_and()
        
        while self.current_token().type == 'IDENTIFIER' and self.current_token().value == 'or':
            self.advance()
            right = self.parse_and()
            left = {'type': 'binary_op', 'op': 'or', 'left': left, 'right': right}
        
        return left
    
    def parse_and(self) -> Dict[str, Any]:
        """Parse logical AND."""
        left = self.parse_equality()
        
        while self.current_token().type == 'IDENTIFIER' and self.current_token().value == 'and':
            self.advance()
            right = self.parse_equality()
            left = {'type': 'binary_op', 'op': 'and', 'left': left, 'right': right}
        
        return left
    
    def parse_equality(self) -> Dict[str, Any]:
        """Parse equality operators."""
        left = self.parse_comparison()
        
        while self.current_token().type in ['EQUAL', 'NOT_EQUAL']:
            op = self.advance().value
            right = self.parse_comparison()
            left = {'type': 'binary_op', 'op': op, 'left': left, 'right': right}
        
        return left
    
    def parse_comparison(self) -> Dict[str, Any]:
        """Parse comparison operators."""
        left = self.parse_additive()
        
        while self.current_token().type in ['LESS', 'GREATER', 'LESS_EQUAL', 'GREATER_EQUAL']:
            op = self.advance().value
            right = self.parse_additive()
            left = {'type': 'binary_op', 'op': op, 'left': left, 'right': right}
        
        return left
    
    def parse_additive(self) -> Dict[str, Any]:
        """Parse addition and subtraction."""
        left = self.parse_multiplicative()
        
        while self.current_token().type in ['PLUS', 'MINUS']:
            op = self.advance().value
            right = self.parse_multiplicative()
            left = {'type': 'binary_op', 'op': op, 'left': left, 'right': right}
        
        return left
    
    def parse_multiplicative(self) -> Dict[str, Any]:
        """Parse multiplication, division, modulo."""
        left = self.parse_unary()
        
        while self.current_token().type in ['MULTIPLY', 'DIVIDE', 'MODULO']:
            op = self.advance().value
            right = self.parse_unary()
            left = {'type': 'binary_op', 'op': op, 'left': left, 'right': right}
        
        return left
    
    def parse_unary(self) -> Dict[str, Any]:
        """Parse unary operators."""
        if self.current_token().type == 'NOT':
            self.advance()
            expr = self.parse_unary()
            return {'type': 'unary_op', 'op': '!', 'expr': expr}
        elif self.current_token().type == 'MINUS':
            self.advance()
            expr = self.parse_unary()
            return {'type': 'unary_op', 'op': '-', 'expr': expr}
        
        return self.parse_primary()
    
    def parse_primary(self) -> Dict[str, Any]:
        """Parse primary expressions (literals, identifiers, function calls, parenthesized expressions)."""
        token = self.current_token()
        
        if token.type == 'NUMBER':
            self.advance()
            value = float(token.value) if '.' in token.value else int(token.value)
            return {'type': 'literal', 'value': value}
        
        elif token.type == 'STRING':
            self.advance()
            return {'type': 'literal', 'value': token.value}
        
        elif token.type == 'TRUE':
            self.advance()
            return {'type': 'literal', 'value': True}
        
        elif token.type == 'FALSE':
            self.advance()
            return {'type': 'literal', 'value': False}
        
        elif token.type == 'IDENTIFIER':
            name = self.advance().value
            
            # Handle member access (e.g., object.property or object.method())
            while self.current_token().type == 'DOT':
                self.advance()  # consume DOT
                member_name = self.expect('IDENTIFIER').value
                
                # Check if it's a method call
                if self.current_token().type == 'LPAREN':
                    self.advance()
                    args = []
                    while self.current_token().type != 'RPAREN':
                        args.append(self.parse_expression())
                        if self.current_token().type == 'COMMA':
                            self.advance()
                    
                    self.expect('RPAREN')
                    # Create a member call node
                    name = {'type': 'member_call', 'object': name, 'member': member_name, 'args': args}
                else:
                    # Create a member access node
                    name = {'type': 'member_access', 'object': name, 'member': member_name}
            
            # Check if the final identifier (or member expression) is a function call
            if isinstance(name, str) and self.current_token().type == 'LPAREN':
                self.advance()
                args = []
                while self.current_token().type != 'RPAREN':
                    args.append(self.parse_expression())
                    if self.current_token().type == 'COMMA':
                        self.advance()
                
                self.expect('RPAREN')
                return {'type': 'call', 'name': name, 'args': args}
            else:
                return name if isinstance(name, dict) else {'type': 'identifier', 'name': name}
        
        elif token.type == 'LPAREN':
            self.advance()
            expr = self.parse_expression()
            self.expect('RPAREN')
            return expr
        
        else:
            self.error(f"Unexpected token in expression: {token.type}")


# ============================================================================
# EXECUTOR: Executes the parsed statements
# ============================================================================

class ReturnException(Exception):
    """Used to implement return statements."""
    def __init__(self, value):
        self.value = value


class Executor:
    """Executes parsed NovaScript statements."""
    
    def __init__(self, stdout=None):
        """Initialize executor with optional custom stdout for testing."""
        self.global_scope: Dict[str, Any] = {}
        self.local_scope: Optional[Dict[str, Any]] = None
        self.stdout = stdout or io.StringIO()
        self.debug = False
    
    def get_scope(self) -> Dict[str, Any]:
        """Get the current scope (local or global)."""
        return self.local_scope if self.local_scope is not None else self.global_scope
    
    def execute(self, statements: List[Dict[str, Any]]) -> Any:
        """Execute a list of statements."""
        result = None
        for stmt in statements:
            result = self.execute_statement(stmt)
        return result
    
    def execute_statement(self, stmt: Dict[str, Any]) -> Any:
        """Execute a single statement."""
        stmt_type = stmt['type']
        
        if stmt_type == 'var':
            scope = self.get_scope()
            scope[stmt['name']] = self.evaluate_expression(stmt['value'])
        
        elif stmt_type == 'function':
            scope = self.get_scope()
            scope[stmt['name']] = stmt  # Store function definition
        
        elif stmt_type == 'print':
            value = self.evaluate_expression(stmt['value'])
            print(self.to_string(value), file=self.stdout)
        
        elif stmt_type == 'if':
            condition = self.evaluate_expression(stmt['condition'])
            if self.is_truthy(condition):
                self.execute(stmt['then'])
            elif stmt['else']:
                self.execute(stmt['else'])
        
        elif stmt_type == 'while':
            while self.is_truthy(self.evaluate_expression(stmt['condition'])):
                try:
                    self.execute(stmt['body'])
                except ReturnException as e:
                    raise e
        
        elif stmt_type == 'for':
            # Initialize
            if stmt['init']:
                self.execute_statement(stmt['init'])
            
            # Loop
            while self.is_truthy(self.evaluate_expression(stmt['condition'])):
                try:
                    self.execute(stmt['body'])
                except ReturnException as e:
                    raise e
                
                # Update
                self.execute_statement(stmt['update'])
        
        elif stmt_type == 'return':
            value = self.evaluate_expression(stmt['value']) if stmt['value'] else None
            raise ReturnException(value)
        
        elif stmt_type == 'assignment':
            if stmt['target']['type'] == 'identifier':
                name = stmt['target']['name']
                value = self.evaluate_expression(stmt['value'])
                
                # Look up through scope chain
                if self.local_scope is not None and name in self.local_scope:
                    self.local_scope[name] = value
                elif name in self.global_scope:
                    self.global_scope[name] = value
                else:
                    scope = self.get_scope()
                    scope[name] = value
            else:
                raise RuntimeError("Invalid assignment target")
        
        elif stmt_type == 'expression':
            return self.evaluate_expression(stmt['value'])
        
        return None
    
    def evaluate_expression(self, expr: Dict[str, Any]) -> Any:
        """Evaluate an expression."""
        expr_type = expr['type']
        
        if expr_type == 'literal':
            return expr['value']
        
        elif expr_type == 'identifier':
            name = expr['name']
            # Look up in local scope first, then global
            if self.local_scope is not None and name in self.local_scope:
                return self.local_scope[name]
            elif name in self.global_scope:
                return self.global_scope[name]
            else:
                raise NameError(f"Undefined variable: {name}")
        
        elif expr_type == 'member_access':
            obj = self.evaluate_expression({'type': 'identifier', 'name': expr['object']} if isinstance(expr['object'], str) else expr['object'])
            member = expr['member']
            
            if not isinstance(obj, dict):
                raise TypeError(f"Cannot access member '{member}' on non-object type: {type(obj).__name__}")
            
            if member not in obj:
                raise AttributeError(f"Object has no member '{member}'")
            
            return obj[member]
        
        elif expr_type == 'member_call':
            obj = self.evaluate_expression({'type': 'identifier', 'name': expr['object']} if isinstance(expr['object'], str) else expr['object'])
            member = expr['member']
            args = [self.evaluate_expression(arg) for arg in expr['args']]
            
            if not isinstance(obj, dict):
                raise TypeError(f"Cannot call method '{member}' on non-object type: {type(obj).__name__}")
            
            if member not in obj:
                raise AttributeError(f"Object has no method '{member}'")
            
            method = obj[member]
            
            # Check if it's callable
            if not callable(method):
                raise TypeError(f"'{member}' is not a method")
            
            # Call the method
            return method(*args)
        
        elif expr_type == 'binary_op':
            return self.evaluate_binary_op(expr)
        
        elif expr_type == 'unary_op':
            return self.evaluate_unary_op(expr)
        
        elif expr_type == 'call':
            return self.evaluate_call(expr)
        
        else:
            raise RuntimeError(f"Unknown expression type: {expr_type}")
    
    def evaluate_binary_op(self, expr: Dict[str, Any]) -> Any:
        """Evaluate binary operations."""
        op = expr['op']
        left = self.evaluate_expression(expr['left'])
        right = self.evaluate_expression(expr['right'])
        
        if op == '+':
            if isinstance(left, str) or isinstance(right, str):
                return self.to_string(left) + self.to_string(right)
            return left + right
        elif op == '-':
            return left - right
        elif op == '*':
            return left * right
        elif op == '/':
            if isinstance(left, int) and isinstance(right, int):
                return left // right
            return left / right
        elif op == '%':
            return left % right
        elif op == '==':
            return left == right
        elif op == '!=':
            return left != right
        elif op == '<':
            return left < right
        elif op == '>':
            return left > right
        elif op == '<=':
            return left <= right
        elif op == '>=':
            return left >= right
        elif op == 'and':
            return self.is_truthy(left) and self.is_truthy(right)
        elif op == 'or':
            return left if self.is_truthy(left) else right
        else:
            raise RuntimeError(f"Unknown operator: {op}")
    
    def evaluate_unary_op(self, expr: Dict[str, Any]) -> Any:
        """Evaluate unary operations."""
        op = expr['op']
        operand = self.evaluate_expression(expr['expr'])
        
        if op == '-':
            return -operand
        elif op == '!':
            return not self.is_truthy(operand)
        else:
            raise RuntimeError(f"Unknown unary operator: {op}")
    
    def evaluate_call(self, expr: Dict[str, Any]) -> Any:
        """Evaluate function calls."""
        name = expr['name']
        args = [self.evaluate_expression(arg) for arg in expr['args']]
        
        # Handle built-in require() function
        if name == 'require':
            return self.builtin_require(args)
        
        # Look up function
        if name not in self.global_scope:
            raise NameError(f"Undefined function: {name}")
        
        func_def = self.global_scope[name]
        
        if not isinstance(func_def, dict) or func_def['type'] != 'function':
            raise TypeError(f"{name} is not a function")
        
        # Check parameter count
        if len(args) != len(func_def['params']):
            raise TypeError(
                f"{name}() takes {len(func_def['params'])} arguments "
                f"({len(args)} given)"
            )
        
        # Create local scope
        prev_local = self.local_scope
        self.local_scope = {}
        
        # Bind parameters
        for param, arg in zip(func_def['params'], args):
            self.local_scope[param] = arg
        
        # Execute function body
        result = None
        try:
            self.execute(func_def['body'])
        except ReturnException as e:
            result = e.value
        finally:
            self.local_scope = prev_local
        
        return result
    
    def builtin_require(self, args: List[Any]) -> Dict[str, Any]:
        """
        Built-in require() function to load standard library modules.
        
        Usage:
            var fs = require("fs")
            var math = require("math")
            var console = require("console")
            var random = require("random")
            var date = require("date")
            var http = require("http")
        
        Args:
            args: List containing module name as string
            
        Returns:
            Dict with module functions and constants
        """
        if len(args) != 1:
            raise TypeError(f"require() takes exactly 1 argument ({len(args)} given)")
        
        module_name = args[0]
        
        if not isinstance(module_name, str):
            raise TypeError(f"Module name must be a string, not {type(module_name).__name__}")
        
        # Load module from stdlib
        try:
            if module_name == 'fs':
                from novascriptx.stdlib.fs import create_module
                return create_module()
            
            elif module_name == 'console':
                from novascriptx.stdlib.console import create_module
                return create_module()
            
            elif module_name == 'math':
                from novascriptx.stdlib.math import create_module
                return create_module()
            
            elif module_name == 'random':
                from novascriptx.stdlib.random import create_module
                return create_module()
            
            elif module_name == 'date':
                from novascriptx.stdlib.date import create_module
                return create_module()
            
            elif module_name == 'http':
                from novascriptx.stdlib.http import create_module
                return create_module()
            
            else:
                raise ModuleNotFoundError(f"No module named '{module_name}'. "
                                         f"Available modules: fs, console, math, random, date, http")
        
        except ImportError as e:
            raise ModuleNotFoundError(f"Failed to load module '{module_name}': {str(e)}")
    
    def is_truthy(self, value: Any) -> bool:
        """Determine if a value is truthy."""
        if value is None or value is False:
            return False
        if value == 0 or value == "" or value == []:
            return False
        return True
    
    def to_string(self, value: Any) -> str:
        """Convert a value to a string for printing."""
        if isinstance(value, bool):
            return "true" if value else "false"
        elif value is None:
            return "null"
        return str(value)


def run_code(source: str, debug: bool = False) -> str:
    """
    Execute NovaScript source code and return output.
    
    Args:
        source: NovaScript source code as string
        debug: If True, enable debug output
        
    Returns:
        Captured stdout output from execution
    """
    try:
        output = io.StringIO()
        
        # Lexical analysis
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        
        # Parsing
        parser = Parser(tokens)
        statements = parser.parse()
        
        # Execution
        executor = Executor(stdout=output)
        executor.debug = debug
        executor.execute(statements)
        
        return output.getvalue()
    
    except (SyntaxError, NameError, TypeError, RuntimeError) as e:
        raise RuntimeError(str(e))


def run_file(filename: str, debug: bool = False) -> str:
    """
    Read and execute a NovaScript file.
    
    Args:
        filename: Path to .nova file
        debug: If True, enable debug output
        
    Returns:
        Captured stdout output from execution
    """
    try:
        with open(filename, 'r') as f:
            source = f.read()
        return run_code(source, debug=debug)
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' not found")


def run_repl():
    """Interactive Read-Eval-Print Loop for NovaScript."""
    executor = Executor()
    print("NovaScript Interpreter v" + __version__)
    print("Type 'exit' to quit\n")
    
    while True:
        try:
            source = input("nova> ")
            
            if source.lower() == 'exit':
                break
            
            if not source.strip():
                continue
            
            # Lexical analysis
            lexer = Lexer(source)
            tokens = lexer.tokenize()
            
            # Parsing
            parser = Parser(tokens)
            statements = parser.parse()
            
            # Execution
            executor.execute(statements)
        
        except (SyntaxError, NameError, TypeError, RuntimeError) as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nInterrupted")
            break
