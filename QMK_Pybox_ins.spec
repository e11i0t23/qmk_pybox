# -*- mode: python -*-

block_cipher = None


a = Analysis(['entry_point.py'],
             pathex=['S:\\Coding\\qmk_pybox'],
             binaries=[],
             datas=[('S:\\Coding\\qmk_pybox\\resources\\Icon.ico', '.'),
             ('S:\\Coding\\qmk_pybox\\dfu-programmer.exe', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='QMK Pybox',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          icon='S:\\Coding\\qmk_pybox\\resources\\Icon.ico' )

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='QMK Pybox')
