# Minimal makefile for Structurizr
#

# You can set these variables from the command line, and also
# from the environment for the first two.
STRUCTURIZR_IMAGE ?= docker.io/structurizr/cli
STRUCTURIZR_CLI   ?= docker run --rm -v $(PWD):/usr/local/structurizr $(STRUCTURIZR_IMAGE)
FORMAT            = plantuml
OUTPUT_DIR        = _build

# Put it first so that "make" without argument is like "make help".
help:
	@echo "make help | all | myWorkspaceFile.dsl"

.PHONY: help all Makefile

all: *.dsl

# Catch-all target: route all unknown targets to Structurizr using the new
# "make mode" option.  $(O) is meant as a shortcut for $(STRUCTURIZR_OPTS).
%: Makefile
	@$(STRUCTURIZR_CLI) export \
		-workspace "$@" \
		-format $(FORMAT) \
		-output "$(OUTPUT_DIR)/$(shell basename -s .dsl $@)"
