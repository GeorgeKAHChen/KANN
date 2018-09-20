filename = main.py

main:
	python3 setup.py

test:
	python3 ${filename} -t

train:
	python3 ${filename} -t

retrain:
	python3 ${filename} -rt

clean:
	bash clean.sh

help:
	sh help.sh
