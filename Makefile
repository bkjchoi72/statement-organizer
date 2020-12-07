build: clean
	pyinstaller main.py

clean:
	rm -rf build dist __pycache__ main.spec

unit:
	pytest test/unit

e2e:
	pytest test/e2e

test: unit e2e

