DOCKER_RUN_BASH:=docker-compose run app bash -c

local_shell:
	@docker-compose run --service-ports --workdir /usr/src/app --rm app /bin/bash

format-code:
	$(DOCKER_RUN_BASH) "black ."

check-types:
	@$(DOCKER_RUN_BASH) "mypy ./python"

all-in:
	$(DOCKER_RUN_BASH) "mypy ./python && black . && PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -p no:cacheprovider tests/unit tests/e2e tests/integration"

run:
	$(DOCKER_RUN_BASH) "INPUT=$(INPUT) python3 -m python.application.main"
