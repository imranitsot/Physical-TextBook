import sys
import os

# Try importing from local directory first (Vercel Self-Contained)
try:
    from backend.main import app
except ImportError:
    # Create a robust path to the project root (Local Dev / Monorepo Root)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    sys.path.append(project_root)
    from backend.main import app

# This 'app' object is what Vercel needs to see
