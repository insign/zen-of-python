#!/usr/bin/make

# ARCHLINUX: paru -S minify

.DEFAULT_GOAL := minify

help:  ## Display this help
	@echo "I'll never make a help"

minify:
	minify index.html > dist/index.html
