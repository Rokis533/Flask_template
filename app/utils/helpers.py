from urllib.parse import urlparse
from flask import request


def get_safe_redirect(target):
    """Get a safe redirect URL to prevent open redirects"""
    if not target:
        return None
    
    # Parse the target URL
    parsed = urlparse(target)
    
    # Only allow relative URLs or URLs to the same host
    if parsed.netloc and parsed.netloc != request.host:
        return None
    
    # Ensure the path is safe
    if target.startswith('//'):
        return None
    
    return target


def format_datetime(dt, format='%Y-%m-%d %H:%M'):
    """Format datetime for display"""
    if dt:
        return dt.strftime(format)
    return ''


def truncate_text(text, length=100, suffix='...'):
    """Truncate text to specified length"""
    if text and len(text) > length:
        return text[:length].rstrip() + suffix
    return text or ''