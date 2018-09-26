main:
	@python3 main.py

test:
	@python3 main.py -t 0

ctest:
	gcc test.c -o ./test
	./test 

train:
	@python3 main.py -l 0

clean:
	@bash clean.sh

help:
	@sh help.sh

install:
	@sh setup.sh

set:
	@vi Setting.py
