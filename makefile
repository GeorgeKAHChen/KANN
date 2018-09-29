include tmp
t=1
p=0

main:
	@python3 main.py -t ${p} ${t}

test:
	@python3 main.py -t ${p} ${t}

cinit:
	@python3 main.py -ci ${p} ${t}

ctest:
	./ctest ${ModelFolder}/model.dumped ${TestFolder}/data.dat ${OutputFolder}/Result.out

train:
	@python3 main.py -l ${p} ${t}

clean:
	@bash clean.sh

help:
	@sh help.sh

install:
	@python3 main.py -i ${p} ${t}

set:
	@vi Setting.py

