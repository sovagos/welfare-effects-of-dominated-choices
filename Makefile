DOCKER_RUN_BASH:=docker-compose run app bash -c

local_shell:
	@docker-compose run --service-ports --workdir /usr/src/app --rm app /bin/bash

test:
	$(DOCKER_RUN_BASH) "PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -p no:cacheprovider tests/unit"

test-e2e:
	$(DOCKER_RUN_BASH) "PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -p no:cacheprovider tests/e2e"

format-code:
	$(DOCKER_RUN_BASH) "black ."

check-types:
	@$(DOCKER_RUN_BASH) "mypy ./python"

all-in:
	$(DOCKER_RUN) "mypy ./python && black . && PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -p no:cacheprovider tests/unit test/e2e"
