import sys
import os
from pathlib import Path

# Get the absolute path of the project root
project_root = Path(__file__).parent.absolute()

# Add the project root to the Python path
sys.path.insert(0, str(project_root))

from src.main import main

if __name__ == "__main__":
    main()