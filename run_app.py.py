# -*- coding: utf-8 -*-
"""
run_app.py - PyInstaller 打包专用入口脚本
负责定位 main.py 并启动 Streamlit 服务。
"""

import sys
import os

if __name__ == "__main__":
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    app_path = os.path.join(base_path, "main.py")
    if not os.path.exists(app_path):
        print("错误：找不到 main.py，搜索路径:", app_path)
        sys.exit(1)

    sys.argv = [
        "streamlit",
        "run",
        app_path,
        "--server.headless", "true",
        "--global.developmentMode", "false",
        "--server.port", "8501",
        "--browser.serverAddress", "localhost",
    ]

    from streamlit.web import cli as stcli
    sys.exit(stcli.main())
