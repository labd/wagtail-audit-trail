.PHONY: install test upload docs sandbox


install:
	pip install -e .[docs,test]

test:
	py.test

retest:
	py.test -vvv --lf

coverage:
	py.test --cov=wagtail_audit_trail --cov-report=term-missing --cov-report=html


sandbox:
	cd sandbox && ./manage.py migrate
	cd sandbox && ./manage.py loaddata fixtures/users.json
	cd sandbox && ./manage.py runserver

release:
	rm -rf dist/*
	python setup.py sdist bdist_wheel
	twine upload --repository-url=https://pypi.labdigital.nl/repo/default/ dist/*
