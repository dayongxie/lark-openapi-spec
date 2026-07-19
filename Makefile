PYTHON ?= python3
CLI ?= lark-cli

.PHONY: fetch build shortcuts changelog update validate

## fetch: download the latest registry snapshot into raw/registry.json
fetch:
	$(PYTHON) tools/fetch_registry.py

## build: regenerate openapi/*.yaml + manifest.yaml from the raw registry
build:
	PYTHONPATH=tools $(PYTHON) tools/build_openapi.py

## shortcuts: regenerate shortcuts/*.yaml from the local lark-cli binary
shortcuts:
	$(PYTHON) tools/extract_shortcuts.py --cli $(CLI)

## update: fetch + build in one go
update: fetch build

## validate: parse every YAML and validate OpenAPI docs (needs openapi-spec-validator)
validate:
	$(PYTHON) -c "\
import glob, yaml; \
[yaml.safe_load(open(f)) for f in glob.glob('openapi/*.yaml') + glob.glob('shortcuts/*.yaml') + ['manifest.yaml']]; \
print('all YAML files parse OK')"
