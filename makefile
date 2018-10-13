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
	./cpptest ${ModelFolder}/model.dumped ${TestFolder}/tmp  ${OutputFolder}/Result.out
 
sb:
	rm -rf ${ModelFolder}/model.dumped
	rm -rf ${TestFolder}/tmp

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

yuvtest:
	mkdir ${OutputFolder}/yuvOutput
	cp ./keras_model.cc ${OutputFolder}/yuvOutput
	cp ./keras_model.h ${OutputFolder}/yuvOutput
	cp ./yuvtest.h ${OutputFolder}/yuvOutput
	cp ${ModelFolder}/model.dumped ${OutputFolder}/yuvOutput
