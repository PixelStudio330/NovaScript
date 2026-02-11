#!/usr/bin/env python3
"""
NovaScript Web IDE Backend
Flask server that handles code execution and output capture

Access the IDE at: http://127.0.0.1:5000
"""

import json
import sys
import io
import os
import socket
from contextlib import redirect_stdout, redirect_stderr
from flask import Flask, render_template, request, jsonify
from nova_interpreter import Lexer, Parser, Executor, Token

# Get the absolute path to the project directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Initialize Flask with absolute paths
app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, 'templates'),
    static_folder=os.path.join(BASE_DIR, 'static')
)

# Configure Flask
app.config['JSON_SORT_KEYS'] = False


@app.route('/')
def index():
    """Serve the main IDE page."""
    return render_template('index.html')


@app.route('/api/execute', methods=['POST'])
def execute_code():
    """
    Execute NovaScript code and capture output.
    
    Expected JSON input:
    {
        "code": "var x = 10\nprint(x)"
    }
    
    Returns JSON output:
    {
        "success": true/false,
        "output": "...",
        "error": "..." (if applicable)
    }
    """
    try:
        data = request.get_json()
        
        if not data or 'code' not in data:
            return jsonify({
                'success': False,
                'error': 'No code provided'
            }), 400
        
        source_code = data['code'].strip()
        
        if not source_code:
            return jsonify({
                'success': True,
                'output': ''
            })
        
        # Capture stdout and stderr
        output_buffer = io.StringIO()
        error_buffer = io.StringIO()
        
        try:
            # Lexical analysis
            lexer = Lexer(source_code)
            tokens = lexer.tokenize()
            
            # Parsing
            parser = Parser(tokens)
            statements = parser.parse()
            
            # Execution with output capture
            executor = Executor()
            with redirect_stdout(output_buffer):
                executor.execute(statements)
            
            output = output_buffer.getvalue()
            
            return jsonify({
                'success': True,
                'output': output
            }), 200
        
        except (SyntaxError, NameError, TypeError, RuntimeError, ZeroDivisionError) as e:
            error_message = f"Error: {str(e)}"
            return jsonify({
                'success': False,
                'error': error_message
            }), 200
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f"Server error: {str(e)}"
        }), 500


@app.route('/api/highlight-keywords', methods=['GET'])
def get_keywords():
    """Return NovaScript keywords for syntax highlighting."""
    keywords = list(Lexer.KEYWORDS.keys())
    return jsonify({'keywords': keywords}), 200


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Page not found'}), 404


@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors."""
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    print("NovaScript Web IDE Server")
    print("=" * 70)
    print("Starting NovaScript Web IDE Server...")
    print("=" * 70)
    print("")
    print("Access the IDE from your browser:")
    print("  → http://127.0.0.1:5000/")
    print("")
    print("Press Ctrl+C to stop the server")
    print("=" * 70)
    print("")
    
    # Run Flask development server
    # host='127.0.0.1' binds to IPv4 loopback interface only
    app.run(
        debug=True,
        host='127.0.0.1',    # IPv4 loopback interface
        port=5000,
        threaded=True,       # Important for Windows: enables threading
        use_reloader=True    # Auto-reload on code changes
    )
