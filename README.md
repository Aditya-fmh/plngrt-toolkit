# PLNGRT Toolkit

Sebuah aplikasi yang dibuat untuk mempermudah pekerjaan di Pusat Laptop Nusantara Garut.


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
nuitka --onefile --windows-icon-from-ico="app icon 64x64.ico" plngrt-toolkit.py
```
