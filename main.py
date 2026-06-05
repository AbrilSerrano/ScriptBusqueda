import sys
import os

if getattr(sys, 'frozen', False):
    bundle_dir = sys._MEIPASS
else:
    bundle_dir = os.path.dirname(os.path.abspath(__file__))

from streamlit.web import cli as stcli

if __name__ == "__main__":
    if getattr(sys, 'frozen', False):
        script = os.path.join(bundle_dir, "buscador.py")
    else:
        script = os.path.join(bundle_dir, "buscador.py")

    sys.argv = [
        "streamlit", "run", script,
        "--global.developmentMode=false",
        "--server.headless=true",
    ]
    sys.exit(stcli.main())
