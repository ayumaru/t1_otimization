# define the name of the virtual environment directory
VENV := venv

# default target, when make executed without arguments
all: venv

$(VENV)/bin/activate:
	virtualenv -p python3 $(VENV)
	. $(PWD)/$(VENV)/bin/activate
	touch tempo
	echo "#!/bin/sh" >> tempo
	echo ". venv/bin/activate" >> tempo
	echo "python3 ./main.py" >> tempo
	chmod +x $(PWD)/main.py
	chmod +x $(PWD)/tempo

# venv is a shortcut target
venv: $(VENV)/bin/activate

clean:
	rm -rf $(VENV)
	rm tempo
	find . -type f -name '*.pyc' -delete

.PHONY: all venv clean