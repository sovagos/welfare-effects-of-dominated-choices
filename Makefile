APP_NAME:=welfare-effects-of-dominated-choices

DOCKER_UP:=docker-compose up -d
DOCKER_DOWN:=docker-compose down
DOCKER_BUILD:= docker build \
	--build-arg http_proxy=$(http_proxy)\
	--build-arg https_proxy=$(https_proxy)\
	--build-arg APP_NAME=$(APP_NAME)

up:
	@$(DOCKER_UP)
down:
	@$(DOCKER_DOWN)
start:
	@$(DOCKER_UP)
stop:
	@$(DOCKER_DOWN)

build: image-base

image-%: suffix=$(subst image-,,$@)
image-%:
	@echo Building: $(APP_NAME)-$(suffix)
	@$(DOCKER_BUILD) \
		--no-cache\
		-f docker-build/Dockerfile.$(suffix) \
		-t $(APP_NAME):$(suffix) \
		.

local_shell:
	@docker-compose run --service-ports --workdir /usr/src/app --rm python_shell /bin/bash

test:
	@docker-compose run test bash -c "PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -p no:cacheprovider tests/unit"

test-e2e:
	@docker-compose run test bash -c "PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -p no:cacheprovider tests/e2e"

.PHONY: start up down stop
.PHONY: local_shell
.PHONY: test
.PHONY: build image-%
