# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_data_files, copy_metadata

# 收集 streamlit 的静态资源和元数据（缺失会导致打包后组件失效/闪退）
datas = collect_data_files("streamlit") + copy_metadata("streamlit")
# 附加我们自己的资源文件夹
datas += [("resources", "resources")]

a = Analysis(
    ['run_app.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=[
        'streamlit',
        'streamlit.web.cli',
        'streamlit.runtime.scriptrunner',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='VoiceAnalysisApp',
    console=False,          # 等价于 --windowed，隐藏终端
    disable_windowed_traceback=False,
    icon='resources/app_icon.icns',
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='VoiceAnalysisApp',
)
app = BUNDLE(
    coll,
    name='VoiceAnalysisApp.app',
    icon='resources/app_icon.icns',
    bundle_identifier='com.student.voiceanalysis',
)
