# -*- mode: python -*-

block_cipher = None


a = Analysis(['entry_point.py'],
             pathex=['C:\\Users\\ellio\\Documents\\code\\qmk_pybox'],
             binaries=[],
             datas=[('C:\\Users\\ellio\\Documents\\code\\qmk_pybox\\resources\\Icon.ico', '.'),
             ('C:\\Users\\ellio\\Documents\\code\\qmk_pybox\\dfu-programmer.exe', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='QMK Pybox ins',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          icon='C:\\Users\\ellio\\Documents\\code\\qmk_pybox\\resources\\Icon.ico' )

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='QMK Pybox')
