#!/usr/bin/make

# ARCHLINUX: paru -S minify

.DEFAULT_GOAL := minify

help:  ## Display this help
	@echo "I'll never make a help"

minify:
	minify -b index.html -o dist/index.html
dev:
	minify -wb index.html -o dist/index.html
