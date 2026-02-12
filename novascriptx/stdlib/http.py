"""
NovaScript Standard Library: HTTP Module

Provides HTTP request functionality.

Usage:
    var http = require("http")
    var response = http.get("https://api.example.com/data")
    print(response)
"""

import urllib.request
import urllib.parse
import json as _json
from typing import Any, Dict, Union


class HTTPModule:
    """Provides HTTP operations."""
    
    @staticmethod
    def get(url: str, headers: Dict = None) -> str:
        """
        Make HTTP GET request.
        
        Args:
            url: URL to request
            headers: Optional dict of HTTP headers
            
        Returns:
            Response body as string
        """
        try:
            req = urllib.request.Request(url)
            if headers:
                for key, value in headers.items():
                    req.add_header(key, value)
            with urllib.request.urlopen(req) as response:
                return response.read().decode('utf-8')
        except Exception as e:
            raise RuntimeError(f"HTTP GET failed: {str(e)}")
    
    @staticmethod
    def post(url: str, data: Union[str, Dict], headers: Dict = None) -> str:
        """
        Make HTTP POST request.
        
        Args:
            url: URL to request
            data: POST data (string or dict)
            headers: Optional dict of HTTP headers
            
        Returns:
            Response body as string
        """
        try:
            if isinstance(data, dict):
                data = _json.dumps(data).encode('utf-8')
            elif isinstance(data, str):
                data = data.encode('utf-8')
            
            req = urllib.request.Request(url, data=data)
            req.add_header('Content-Type', 'application/json')
            
            if headers:
                for key, value in headers.items():
                    req.add_header(key, value)
            
            with urllib.request.urlopen(req) as response:
                return response.read().decode('utf-8')
        except Exception as e:
            raise RuntimeError(f"HTTP POST failed: {str(e)}")
    
    @staticmethod
    def put(url: str, data: Union[str, Dict], headers: Dict = None) -> str:
        """
        Make HTTP PUT request.
        
        Args:
            url: URL to request
            data: PUT data (string or dict)
            headers: Optional dict of HTTP headers
            
        Returns:
            Response body as string
        """
        try:
            if isinstance(data, dict):
                data = _json.dumps(data).encode('utf-8')
            elif isinstance(data, str):
                data = data.encode('utf-8')
            
            req = urllib.request.Request(url, data=data, method='PUT')
            req.add_header('Content-Type', 'application/json')
            
            if headers:
                for key, value in headers.items():
                    req.add_header(key, value)
            
            with urllib.request.urlopen(req) as response:
                return response.read().decode('utf-8')
        except Exception as e:
            raise RuntimeError(f"HTTP PUT failed: {str(e)}")
    
    @staticmethod
    def delete(url: str, headers: Dict = None) -> str:
        """
        Make HTTP DELETE request.
        
        Args:
            url: URL to request
            headers: Optional dict of HTTP headers
            
        Returns:
            Response body as string
        """
        try:
            req = urllib.request.Request(url, method='DELETE')
            
            if headers:
                for key, value in headers.items():
                    req.add_header(key, value)
            
            with urllib.request.urlopen(req) as response:
                return response.read().decode('utf-8')
        except Exception as e:
            raise RuntimeError(f"HTTP DELETE failed: {str(e)}")


def create_module() -> Dict[str, Any]:
    """Create http module with callable functions."""
    return {
        'get': HTTPModule.get,
        'post': HTTPModule.post,
        'put': HTTPModule.put,
        'delete': HTTPModule.delete,
    }
