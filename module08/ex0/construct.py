import sys
import os
import site


def detect_virtual_environment():
    """Detect if running inside a virtual environment"""
    return hasattr(sys, "real_prefix") or (
        hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix
    )


def get_venv_name():
    """Extract virtual environment name from path"""
    venv_path = sys.prefix
    return os.path.basename(venv_path)


def get_site_packages():
    """Get site-packages directory path"""
    return site.getsitepackages()[0] if site.getsitepackages() else "Not found"


def main():
    in_venv = detect_virtual_environment()

    if in_venv:
        print("Inside the Construct")
        print()
        print(f"MATRIX STATUS: Welcome to the construct")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {get_venv_name()}")
        print(f"Environment Path: {sys.prefix}")
        print()
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print()
        print("Package installation path:")
        print(get_site_packages())
    else:
        print("Outside the Matrix")
        print()
        print(f"MATRIX STATUS: You're still plugged in")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print()
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print()
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows")
        print()
        print("Then run this program again.")


if __name__ == "__main__":
    main()
