# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['wizard_main.py'],
             pathex=['C:\\Users\\conta\\Documents\\script\\Wizard\\App'],
             binaries=[],
             datas=[],
             hiddenimports=['PyQt5.QtPrintSupport'],
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
          name='wizard_console',
          debug=False,
          bootloader_ignore_signals=True,
          strip=False,
          upx=True,
          console=True,
          version = 'version.rc',
          icon="C:\\Users\\conta\\Documents\\script\\Wizard\\App\\ressources\\images\\console.ico")
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='wizard_console')
