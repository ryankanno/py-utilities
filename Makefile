NOSETESTS ?= nosetests

.PHONY: nosetests nosetests.coverage test test.coverage flake8

test: nosetests flake8
test.profile: nosetests.profile flake8
test.coverage: nosetests.coverage flake8

nosetests:
	@$(NOSETESTS) --with-doctest

nosetests.profile:
	@$(NOSETESTS) --with-doctest --with-profile

nosetests.coverage:
	@$(NOSETESTS) --with-xcoverage --cover-package=py_utilities --cover-tests --cover-erase --with-doctest

flake8:
	@flake8 py_utilities tests

clean:
	@rm -rf .coverage
	@rm -rf coverage.xml
