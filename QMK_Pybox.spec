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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          exclude_binaries=False,
          name='QMK_Pybox',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          runtime_tmpdir=None,
          console=False,
          icon='C:\\Users\\ellio\\Documents\\code\\qmk_pybox\\resources\\icon.ico' )
            
