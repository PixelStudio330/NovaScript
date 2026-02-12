"""
NovaScript Standard Library: Date/Time Module

Provides date and time operations.

Usage:
    var date = require("date")
    print(date.now())                  # Current timestamp
    print(date.format("%Y-%m-%d"))     # Current date formatted
    var future = date.addDays(5)       # Date 5 days from now
"""

from datetime import datetime, timedelta
from typing import Any, Dict, Union


class DateModule:
    """Provides date and time operations."""
    
    @staticmethod
    def now() -> int:
        """
        Get current timestamp (seconds since epoch).
        
        Returns:
            Current Unix timestamp
        """
        return int(datetime.now().timestamp())
    
    @staticmethod
    def nowMs() -> int:
        """
        Get current timestamp in milliseconds.
        
        Returns:
            Current Unix timestamp in milliseconds
        """
        return int(datetime.now().timestamp() * 1000)
    
    @staticmethod
    def format(pattern: str = "%Y-%m-%d %H:%M:%S") -> str:
        """
        Get current time formatted according to pattern.
        
        Args:
            pattern: strftime format string
            
        Returns:
            Formatted current datetime
        """
        return datetime.now().strftime(pattern)
    
    @staticmethod
    def getYear() -> int:
        """Get current year."""
        return datetime.now().year
    
    @staticmethod
    def getMonth() -> int:
        """Get current month (1-12)."""
        return datetime.now().month
    
    @staticmethod
    def getDay() -> int:
        """Get current day of month (1-31)."""
        return datetime.now().day
    
    @staticmethod
    def getDayOfWeek() -> int:
        """Get day of week (0-6, Monday is 0)."""
        return datetime.now().weekday()
    
    @staticmethod
    def getHour() -> int:
        """Get current hour (0-23)."""
        return datetime.now().hour
    
    @staticmethod
    def getMinute() -> int:
        """Get current minute (0-59)."""
        return datetime.now().minute
    
    @staticmethod
    def getSecond() -> int:
        """Get current second (0-59)."""
        return datetime.now().second
    
    @staticmethod
    def addDays(days: int) -> str:
        """
        Get date string for N days from now.
        
        Args:
            days: Number of days to add
            
        Returns:
            Formatted date string
        """
        future = datetime.now() + timedelta(days=days)
        return future.strftime("%Y-%m-%d")
    
    @staticmethod
    def addHours(hours: int) -> str:
        """
        Get datetime string for N hours from now.
        
        Args:
            hours: Number of hours to add
            
        Returns:
            Formatted datetime string
        """
        future = datetime.now() + timedelta(hours=hours)
        return future.strftime("%Y-%m-%d %H:%M:%S")
    
    @staticmethod
    def fromTimestamp(timestamp: int) -> str:
        """
        Convert Unix timestamp to formatted datetime.
        
        Args:
            timestamp: Unix timestamp (seconds since epoch)
            
        Returns:
            Formatted datetime string
        """
        dt = datetime.fromtimestamp(timestamp)
        return dt.strftime("%Y-%m-%d %H:%M:%S")


def create_module() -> Dict[str, Any]:
    """Create date module with callable functions."""
    return {
        'now': DateModule.now,
        'nowMs': DateModule.nowMs,
        'format': DateModule.format,
        'getYear': DateModule.getYear,
        'getMonth': DateModule.getMonth,
        'getDay': DateModule.getDay,
        'getDayOfWeek': DateModule.getDayOfWeek,
        'getHour': DateModule.getHour,
        'getMinute': DateModule.getMinute,
        'getSecond': DateModule.getSecond,
        'addDays': DateModule.addDays,
        'addHours': DateModule.addHours,
        'fromTimestamp': DateModule.fromTimestamp,
    }
