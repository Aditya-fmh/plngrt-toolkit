# PLNGRT Toolkit

Sebuah aplikasi yang dibuat untuk mempermudah pekerjaan di Pusat Laptop Nusantara Garut.

## Updating From v1.3

- Please apply this update first - [PLNGRT Toolkit 1.3.5](https://github.com/Aditya-fmh/plngrt-toolkit/releases/tag/1.3.5)
  
## Prequisite

- [Python 3.11](https://www.python.org/downloads/release/python-3110/)
- [Nuitka](https://nuitka.net/index.html)
- [Inno Setup](https://jrsoftware.org/isinfo.php)

## How to Build

To build this, we gonna use nuitka. First, install nuitka

```bash
pip install nuitka
```

Then after nuitka installed, we can build the script with this command
```bash
nuitka --enable-plugin=tk-inter --onefile --windows-icon-from-ico="app icon 64x64.ico" plngrt-toolkit.py
```

## App Preview

![Preview 1](https://i.imgur.com/CYqvpUi.png)
