/**
 * NovaScript IDE Frontend JavaScript
 * Handles code editor, execution, and output display
 */

// ============================================================================
// Default NovaScript Code
// ============================================================================

const DEFAULT_CODE = `# NovaScript Example Program
# Variables and function calls
var x = 10
function greet(name):
{
    print("Hello, " + name)
}

greet("World")

# Arithmetic operations
var a = 5
var b = 3
print("Sum: " + (a + b))
print("Product: " + (a * b))

# Conditional statement
var age = 25
if (age >= 18): {
    print("You are an adult")
} else: {
    print("You are a minor")
}

# Loop statement
print("Counting:")
for (var i = 1 : i <= 3 : i = i + 1): {
    print("Count: " + i)
}

# Recursive function
function fibonacci(n):
{
    if (n <= 1): {
        return n
    }
    return fibonacci(n - 1) + fibonacci(n - 2)
}

print("Fibonacci(5) = " + fibonacci(5))`;

// ============================================================================
// CodeMirror Editor Setup
// ============================================================================

let editor;

function initializeEditor() {
    /**
     * Initialize the CodeMirror editor with custom configuration
     */
    editor = CodeMirror.fromTextArea(
        document.getElementById('codeEditor'),
        {
            mode: 'python',  // Use Python mode for similar syntax highlighting
            theme: 'material-darker',
            lineNumbers: true,
            lineWrapping: true,
            indentUnit: 4,
            tabSize: 4,
            indentWithTabs: false,
            matchBrackets: true,
            autoCloseBrackets: true,
            styleActiveLine: true,
            styleSelectedText: true,
            highlightSelectionMatches: { showToken: /\w/, annotateScrollbar: false },
            extraKeys: {
                'Ctrl-Enter': executeCode,      // Ctrl+Enter to run code
                'Cmd-Enter': executeCode        // Cmd+Enter for Mac
            }
        }
    );
    
    // Set default code
    editor.setValue(DEFAULT_CODE);
    
    // Refresh editor to ensure proper rendering
    setTimeout(() => editor.refresh(), 100);
}

// ============================================================================
// Code Execution
// ============================================================================

async function executeCode() {
    /**
     * Send code to backend for execution and display output
     */
    const code = editor.getValue().trim();
    
    if (!code) {
        addConsoleMessage('Please write some code!', 'console-warning');
        return;
    }
    
    // Reset console for new execution
    clearConsole();
    setStatus('Running...', 'loading');
    disableRunButton(true);
    
    try {
        const response = await fetch('/api/execute', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ code: code })
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        
        if (data.success) {
            // Display output
            if (data.output) {
                // Split output by lines and add each line
                const lines = data.output.split('\n');
                lines.forEach(line => {
                    if (line.trim()) {
                        addConsoleMessage(line, 'console-output');
                    }
                });
                
                if (lines.length === 1 || !data.output.endsWith('\n')) {
                    setStatus('Execution completed', 'success');
                }
            } else {
                addConsoleMessage('Code executed successfully (no output)', 'console-success');
                setStatus('Execution completed', 'success');
            }
        } else {
            // Display error
            addConsoleMessage(data.error || 'Unknown error occurred', 'console-error');
            setStatus('Error', 'error');
        }
    } catch (error) {
        console.error('Fetch error:', error);
        addConsoleMessage(`Network error: ${error.message}`, 'console-error');
        setStatus('Connection error', 'error');
    } finally {
        disableRunButton(false);
        focusEditor();
    }
}

// ============================================================================
// Console Output Functions
// ============================================================================

function addConsoleMessage(message, className = 'console-output') {
    /**
     * Add a message to the console output
     */
    const consoleDiv = document.getElementById('console');
    const lineDiv = document.createElement('div');
    lineDiv.className = `console-line ${className}`;
    
    // Escape HTML to prevent injection
    const textNode = document.createTextNode(message);
    lineDiv.appendChild(textNode);
    
    consoleDiv.appendChild(lineDiv);
    
    // Auto-scroll to bottom
    consoleDiv.scrollTop = consoleDiv.scrollHeight;
}

function clearConsole() {
    /**
     * Clear the console output
     */
    const consoleDiv = document.getElementById('console');
    consoleDiv.innerHTML = '';
}

// ============================================================================
// UI State Management
// ============================================================================

function setStatus(message, type = '') {
    /**
     * Update the status indicator
     */
    const statusElement = document.getElementById('status');
    statusElement.textContent = message;
    statusElement.className = `status ${type}`;
}

function disableRunButton(disabled) {
    /**
     * Enable or disable the run button
     */
    const runBtn = document.getElementById('runBtn');
    runBtn.disabled = disabled;
}

function focusEditor() {
    /**
     * Set focus to the editor
     */
    editor.focus();
}

// ============================================================================
// Event Listeners
// ============================================================================

document.addEventListener('DOMContentLoaded', function() {
    /**
     * Initialize IDE when DOM is loaded
     */
    
    // Initialize editor
    initializeEditor();
    
    // Run button
    document.getElementById('runBtn').addEventListener('click', executeCode);
    
    // Clear button
    document.getElementById('clearBtn').addEventListener('click', clearConsole);
    
    // Reset button
    document.getElementById('resetBtn').addEventListener('click', function() {
        if (confirm('Are you sure you want to reset the editor to the default example?')) {
            editor.setValue(DEFAULT_CODE);
            clearConsole();
            setStatus('Editor reset', '');
            focusEditor();
        }
    });
    
    // Focus editor on load
    setTimeout(() => focusEditor(), 200);
    
    // Optional: Add keyboard shortcuts info
    console.log('NovaScript IDE Shortcuts:');
    console.log('- Ctrl+Enter (or Cmd+Enter): Run code');
    console.log('- Click "Clear Output": Clear console');
    console.log('- Click "Reset": Reset to default example');
});

// ============================================================================
// Utility Functions
// ============================================================================

function getCodeStats() {
    /**
     * Get statistics about the current code
     */
    const code = editor.getValue();
    const lines = code.split('\n').length;
    const chars = code.length;
    const words = code.trim().split(/\s+/).length;
    
    return { lines, chars, words };
}

function downloadCode() {
    /**
     * Download the current code as a .nova file
     */
    const code = editor.getValue();
    const element = document.createElement('a');
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(code));
    element.setAttribute('download', 'program.nova');
    element.style.display = 'none';
    document.body.appendChild(element);
    element.click();
    document.body.removeChild(element);
}

// ============================================================================
// Optional: Advanced Features
// ============================================================================

/**
 * Monitor editor changes in real-time (example)
 */
editor.on('change', function(cm) {
    // Could be used for auto-save, auto-complete, etc.
    // Currently just tracks changes
});

/**
 * Optional: Syntax highlighting for NovaScript keywords
 * This extends CodeMirror's Python mode to highlight NovaScript keywords
 */
function setupNovaScriptHighlighting() {
    // Get NovaScript keywords from backend
    fetch('/api/highlight-keywords')
        .then(response => response.json())
        .then(data => {
            const keywords = data.keywords;
            // Could implement custom syntax highlighting here
            console.log('Available NovaScript keywords:', keywords);
        })
        .catch(error => console.error('Error fetching keywords:', error));
}

// Call on load
setupNovaScriptHighlighting();
