echo "building executable using upx"
echo "use -w to without console"
python3 pyinstaller -F --add-data "templates:templates" main.py --upx-dir=upx-3.96-amd64_linux -y --onefile
echo "Done"