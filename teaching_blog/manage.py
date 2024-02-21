#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    try:
        # Check if DJANGO_SETTINGS_MODULE is already set
        if not os.environ.get('DJANGO_SETTINGS_MODULE'):
            # If not set, set it to 'teaching_blog.settings'
            os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'teaching_blog.settings')
        
        # Import Django only after setting DJANGO_SETTINGS_MODULE
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Handle ImportError by providing more detailed error message
        raise ImportError(
            f"Couldn't import Django. {exc}. Are you sure it's installed and "
            f"available on your PYTHONPATH environment variable? Did you "
            f"forget to activate a virtual environment?"
        ) from exc
    except Exception as e:
        # Handle other exceptions gracefully and print out the error
        print(f"An error occurred: {e}")
        sys.exit(1)

    # Execute Django management commands
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
