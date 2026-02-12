"""
NovaScript Standard Library: Math Module

Provides mathematical functions and constants.

Usage:
    var math = require("math")
    print(math.sqrt(16))        # 4.0
    print(math.pow(2, 3))       # 8
    print(math.pi)              # 3.14159...
    print(math.abs(-5))         # 5
"""

import math as _math
from typing import Any, Dict, Union


class MathModule:
    """Provides math operations and constants."""
    
    PI = _math.pi
    E = _math.e
    TAU = _math.tau
    INF = float('inf')
    NAN = float('nan')
    
    @staticmethod
    def abs(x: Union[int, float]) -> Union[int, float]:
        """Return absolute value."""
        return abs(x)
    
    @staticmethod
    def sqrt(x: Union[int, float]) -> float:
        """Return square root."""
        return _math.sqrt(x)
    
    @staticmethod
    def pow(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
        """Return x raised to power y."""
        return x ** y
    
    @staticmethod
    def floor(x: Union[int, float]) -> int:
        """Return floor of x."""
        return _math.floor(x)
    
    @staticmethod
    def ceil(x: Union[int, float]) -> int:
        """Return ceiling of x."""
        return _math.ceil(x)
    
    @staticmethod
    def round(x: Union[int, float], digits: int = 0) -> Union[int, float]:
        """Return x rounded to given decimal places."""
        return round(x, digits)
    
    @staticmethod
    def min(*args) -> Union[int, float]:
        """Return minimum value."""
        return min(*args)
    
    @staticmethod
    def max(*args) -> Union[int, float]:
        """Return maximum value."""
        return max(*args)
    
    @staticmethod
    def sin(x: Union[int, float]) -> float:
        """Return sine of x (in radians)."""
        return _math.sin(x)
    
    @staticmethod
    def cos(x: Union[int, float]) -> float:
        """Return cosine of x (in radians)."""
        return _math.cos(x)
    
    @staticmethod
    def tan(x: Union[int, float]) -> float:
        """Return tangent of x (in radians)."""
        return _math.tan(x)
    
    @staticmethod
    def log(x: Union[int, float], base: Union[int, float] = _math.e) -> float:
        """Return logarithm of x (default natural log)."""
        return _math.log(x, base)
    
    @staticmethod
    def exp(x: Union[int, float]) -> float:
        """Return e raised to power x."""
        return _math.exp(x)


def create_module() -> Dict[str, Any]:
    """Create math module with callable functions and constants."""
    return {
        'abs': MathModule.abs,
        'sqrt': MathModule.sqrt,
        'pow': MathModule.pow,
        'floor': MathModule.floor,
        'ceil': MathModule.ceil,
        'round': MathModule.round,
        'min': MathModule.min,
        'max': MathModule.max,
        'sin': MathModule.sin,
        'cos': MathModule.cos,
        'tan': MathModule.tan,
        'log': MathModule.log,
        'exp': MathModule.exp,
        'pi': MathModule.PI,
        'e': MathModule.E,
        'tau': MathModule.TAU,
        'inf': MathModule.INF,
        'nan': MathModule.NAN,
    }
