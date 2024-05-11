# -*- mode: python ; coding: utf-8 -*-


block_cipher = pyi_crypto.PyiBlockCipher(key="'qwer1234'")


a = Analysis(
    ['main_ui.py'],
    pathex=['.'],
    binaries=[],
    datas=[('source/qml/main.qml', 'source/qml'), ('source/img', 'source/img')],
    hiddenimports=['source.py.pdf_to_dataframe', 'source.py.convert', 'source.py.edit', 'openpyxl', 'pdfplumber', 'pandas'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='test',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='./source/icon/profile.ico'
)
