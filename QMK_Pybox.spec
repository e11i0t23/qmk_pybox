# -*- mode: python -*-

block_cipher = None


a = Analysis(['entry_point.py'],
             pathex=['C:\\Users\\ellio\\Documents\\code\\qmk_pybox'],
             binaries=[],
             datas=[('resources\icon.ico', 'recources')],
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

extras_toc = Tree('C:\\Users\\ellio\\Documents\\code\\qmk_pybox\\resources', prefix='resources')

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='QMK_Pybox',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
