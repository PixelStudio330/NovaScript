"""
NovaScript Standard Library: Random Module

Provides random number generation functions.

Usage:
    var random = require("random")
    print(random.randInt(1, 100))      # Random int between 1-100
    print(random.randFloat())          # Random float 0.0-1.0
    var arr = require("array")
    print(random.choice([1, 2, 3]))    # Random element from array
"""

import random as _random
from typing import Any, Dict, Union, List


class RandomModule:
    """Provides random number generation."""
    
    @staticmethod
    def random() -> float:
        """
        Return random float between 0.0 and 1.0.
        
        Returns:
            Random float value
        """
        return _random.random()
    
    @staticmethod
    def randInt(start: int, end: int) -> int:
        """
        Return random integer between start and end (inclusive).
        
        Args:
            start: Lower bound
            end: Upper bound
            
        Returns:
            Random integer
        """
        return _random.randint(start, end)
    
    @staticmethod
    def randFloat() -> float:
        """
        Return random float between 0.0 and 1.0.
        
        Returns:
            Random float value
        """
        return _random.random()
    
    @staticmethod
    def uniform(a: Union[int, float], b: Union[int, float]) -> float:
        """
        Return random float between a and b.
        
        Args:
            a: Lower bound
            b: Upper bound
            
        Returns:
            Random float
        """
        return _random.uniform(a, b)
    
    @staticmethod
    def choice(seq):
        """
        Choose random element from sequence.
        
        Args:
            seq: Sequence to choose from
            
        Returns:
            Random element from sequence
        """
        if isinstance(seq, str):
            return _random.choice(seq)
        elif isinstance(seq, (list, tuple)):
            return _random.choice(seq)
        else:
            raise TypeError(f"Cannot choose from {type(seq)}")
    
    @staticmethod
    def shuffle(lst):
        """
        Shuffle list in place.
        
        Args:
            lst: List to shuffle
        """
        if isinstance(lst, list):
            _random.shuffle(lst)
            return lst
        else:
            raise TypeError(f"Cannot shuffle {type(lst)}")
    
    @staticmethod
    def seed(value: int) -> None:
        """
        Seed the random number generator.
        
        Args:
            value: Seed value
        """
        _random.seed(value)


def create_module() -> Dict[str, Any]:
    """Create random module with callable functions."""
    return {
        'random': RandomModule.random,
        'randInt': RandomModule.randInt,
        'randFloat': RandomModule.randFloat,
        'uniform': RandomModule.uniform,
        'choice': RandomModule.choice,
        'shuffle': RandomModule.shuffle,
        'seed': RandomModule.seed,
    }
