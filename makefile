t=1
p=0

main:
	@python3 main.py -t ${p} ${t}

test:
	@python3 main.py -t ${p} ${t}

ctinit:
	@python3 dump2simple.py

ctest:
	include tmp
	@./ctest ${ModelFolder}/model.dumped ${TestFolder} ${OutputFolder}/Result.out

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

