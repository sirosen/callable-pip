VIRTUALENV=.venv

.PHONY: build upload clean help

help:
	@echo "These are our make targets and what they do."
	@echo "All unlisted targets are internal."
	@echo ""
	@echo "  help:      Show this helptext"
	@echo "  build:     Create the distributions which we like to upload to pypi"
	@echo "  upload:    [build], but also upload to pypi using twine"
	@echo "  clean:     Remove typically unwanted files, mostly from [build]"


$(VIRTUALENV):
	virtualenv $(VIRTUALENV)
	$(VIRTUALENV)/bin/pip install --upgrade pip
	$(VIRTUALENV)/bin/pip install --upgrade setuptools
	$(VIRTUALENV)/bin/pip install --upgrade twine


build: $(VIRTUALENV)
	$(VIRTUALENV)/bin/python setup.py sdist bdist_egg


$(VIRTUALENV)/bin/twine: $(VIRTUALENV)


upload: $(VIRTUALENV)/bin/twine build
	$(VIRTUALENV)/bin/twine upload dist/*


clean:
	-rm -r $(VIRTUALENV)
	-rm -r dist
	-rm -r build
	-rm -r *.egg-info
