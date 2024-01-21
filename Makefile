version=0.0.5a0

prepare:
	pip install twine

clean:
	rm -rf ./dist
	rm -rf ./build
uninstall:
	pip uninstall flomo -y

all: uninstall clean
	python setup.py sdist bdist_wheel
	pip install -U dist/flomo-${version}-py3-none-any.whl

upload:
	twine upload dist/*