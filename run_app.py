import sys
import os
import streamlit.web.cli as stcli

if __name__ == "__main__":
    # PyInstaller 打包后资源在 sys._MEIPASS，开发时在脚本所在目录
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    os.chdir(base_path)
    app_path = os.path.join(base_path, "main.py")
    if not os.path.exists(app_path):
        print("错误：未找到 main.py")
        sys.exit(1)
    sys.argv = ["streamlit", "run", app_path,
                "--server.headless=true",
                "--global.developmentMode=false"]
    stcli.main()
