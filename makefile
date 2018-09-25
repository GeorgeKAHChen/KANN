p = 1

main:
	@python3 main.py

test:
	@python3 main.py -t ${p}

ctest:
	gcc test.c -o ./test
	./test 

train:
	@python3 main.py -l ${p}

retrain:
	@python3 main.py -rl ${p}

clean:
	@bash clean.sh

help:
	@sh help.sh

install:
	@sh setup.sh

set:
	@vi Setting.py
