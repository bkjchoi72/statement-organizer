build: clean
	pyinstaller main.py

clean:
	rm -rf build dist __pycache__ main.spec
