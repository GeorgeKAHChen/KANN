p=0

main:
	@python3 main.py

test:
	@python3 main.py -t ${p}

ctinit:
	@python3 dump2simple.py

ctest:
	include tmp
	@./ctest ${ModelFolder}/model.dumped ${TestFolder} ${OutputFolder}/Result.out

train:
	@python3 main.py -l ${p}

clean:
	@bash clean.sh

help:
	@sh help.sh

install:
	@python3 main.py -i 

set:
	@vi Setting.py

