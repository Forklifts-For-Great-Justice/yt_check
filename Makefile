.PHONY: test

test:
	@echo "running pytest"
	@pipenv run python3 -m pytest
