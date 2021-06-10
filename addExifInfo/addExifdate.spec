# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['addExifdate.py'],
             pathex=['C:\\Users\\zhangdehua\\PycharmProjects\\helloworld'],
             binaries=[],
             datas=[('C:\\Users\zhangdehua\\PycharmProjects\\helloworld\\mtc7seg.ttf','.'),('C:\\Users\zhangdehua\\PycharmProjects\\helloworld\\logo.ico','.')],
             hiddenimports=['pkg_resources.py2_warn','pkg_resources.markers'],
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
          name='addExifdate',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon='logo.ico')
