@echo "building executable using upx"
@echo "use -w to without console"
pyinstaller -F --add-data "templates;templates" main.py --upx-dir=upx-3.96-win64 -y --onefile
@echo "Done"
pause