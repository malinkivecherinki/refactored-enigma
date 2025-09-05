#!/usr/bin/env python3
"""
CryptoUtils - Cryptographic utilities and encryption helpers.
"""

import hashlib
import base64
from typing import str

class CryptoUtils:
    """Cryptographic utilities."""
    @staticmethod
    def hash_md5(data: str) -> str:
        """Generate MD5 hash."""
        return hashlib.md5(data.encode()).hexdigest()
    
    @staticmethod
    def hash_sha256(data: str) -> str:
        """Generate SHA256 hash."""
        return hashlib.sha256(data.encode()).hexdigest()
    
    @staticmethod
    def encode_base64(data: str) -> str:
        """Encode to base64."""
        return base64.b64encode(data.encode()).decode()
    
    @staticmethod
    def decode_base64(data: str) -> str:
        """Decode from base64."""
        return base64.b64decode(data.encode()).decode()

if __name__ == "__main__":
    crypto = CryptoUtils()
    print("CryptoUtils initialized")
