main:
	@python3 main.py

test:
	@python3 main.py -t

ctest:
	gcc test.c -o ./test
	./test 

train:
	@python3 main.py -l

retrain:
	@python3 ${filename} -rl

clean:
	@bash clean.sh

help:
	@sh help.sh

install:
	@sh setup.sh
