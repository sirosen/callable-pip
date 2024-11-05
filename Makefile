.PHONY: build upload clean

build:
	pipx run build .
upload:
	pipx run twine upload dist/*

clean:
	-rm -r dist
	-rm -r *.egg-info
