import os
import uuid
from datetime import datetime
import hashlib

def generate_unique_id(length=32):
    """Generate a unique identifier of a specified length."""
    return uuid.uuid4().hex[:length]

def get_current_timestamp():
    """Get the current timestamp in seconds."""
    return int(datetime.now().timestamp())

def hash_password(password):
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def is_valid_email(email):
    """Check if an email address is valid."""
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_pattern, email))

def get_file_extension(filename):
    """Get the file extension from a filename."""
    return os.path.splitext(filename)[1]

def get_file_size_in_mb(filename):
    """Get the file size in megabytes."""
    return os.path.getsize(filename) / (1024 * 1024)

def get_file_size_in_gb(filename):
    """Get the file size in gigabytes."""
    return os.path.getsize(filename) / (1024 * 1024 * 1024)