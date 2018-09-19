FileName = main.py

main:
	python3 ${filename} -t

t:
	python3 ${filename} -t

f:
	python3 ${filename} -f

h:
	sh help.sh
