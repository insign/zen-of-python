#!/usr/bin/make

# ARCHLINUX: paru -S minify

.DEFAULT_GOAL := minify

help:  ## Display this help
	@echo "I'll never make a help"

minify:
	npm install && npm run build
dev:
	npm run build
