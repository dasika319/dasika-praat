# -*- coding: utf-8 -*-
"""PyInstaller 打包专用入口：定位 main.py 并启动 Streamlit。"""
import sys
import os

if __name__ == "__main__":
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    app_path = os.path.join(base_path, "main.py")

    if not os.path.exists(app_path):
        print("找不到 main.py，搜索路径:", app_path)
        sys.exit(1)

    sys.argv = [
        "streamlit", "run", app_path,
        "--server.headless", "true",
        "--global.developmentMode", "false",
        "--server.port", "8501",
        "--browser.gatherUsageStats", "false",
    ]

    from streamlit.web import cli as stcli
    sys.exit(stcli.main())
