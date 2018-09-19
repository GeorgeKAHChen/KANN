#!/bin/bash
echo "WARNING: This command will clean all model and I/O data in this program, are you sure you "
echo "         want to delete all of them? (yes / no)"
read choice
tem='yes'

if [ "${choice}" == "${tem}" ]; then
	rm -rf Input
	rm -rf Output
	rm -rf Model
	mkdir Input
	mkdir Output
	mkdir Model
fi


