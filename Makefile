DOCKER_RUN_BASH:=docker-compose run app bash -c

build:
	@docker-compose build

local_shell:
	@docker-compose run --service-ports --workdir /usr/src/app --rm app /bin/bash

format-code:
	$(DOCKER_RUN_BASH) "black ."

check-types:
	@$(DOCKER_RUN_BASH) "mypy ./python"

all-in:
	$(DOCKER_RUN_BASH) "mypy ./python && black . && PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -p no:cacheprovider tests"

test:
	$(DOCKER_RUN_BASH) "black . && PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -p no:cacheprovider tests"

run-baseline:
	$(DOCKER_RUN_BASH) "INPUT=$(INPUT) python3 -m python.application.baseline"

run-correct-upper:
	$(DOCKER_RUN_BASH) "INPUT=$(INPUT) python3 -m python.application.upper"

run-correct-lower:
	$(DOCKER_RUN_BASH) "INPUT=$(INPUT) python3 -m python.application.lower"

run-memory-profile:
	$(DOCKER_RUN_BASH) "INPUT=$(INPUT) python3 -m memory_profiler python.application.main"
