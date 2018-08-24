
.PHONY: clean-pyc
clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

.PHONY: devel
devel:
	pip3 install -r requirements.txt

.PHONY: env-info
env-info:
	uname -a
	pip list

.PHONY: lint
lint:
	flake8 --exclude=.eggs --ignore=E501,F401,F403,F405 .

.PHONY: test
test:
	python3 setup.py test