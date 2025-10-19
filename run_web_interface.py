"""
TMDL Best Practices Analyzer - Web Interface Launcher

Run this script to start the web interface for analyzing Power BI TMDL files.
"""

import sys
from pathlib import Path

# Add src directory to Python path
src_path = Path(__file__).parent / 'src'
sys.path.insert(0, str(src_path))

# Import and run the web interface
from web_interface import app

if __name__ == '__main__':
    print("=" * 60)
    print("TMDL Best Practices Analyzer - Web Interface")
    print("=" * 60)
    print()
    print("Starting web server...")
    print("Open your browser and go to: http://localhost:5000")
    print()
    print("Press CTRL+C to stop the server")
    print("=" * 60)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
