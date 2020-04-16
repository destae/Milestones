run:
	-make build

build:
	-cd final_project/data; unzip data.zip


test:
	-python3 -m unittest discover -s final_project


clean:
	-rm final_project/mainUI
	-rm final_project/clientUI
	-rm final_project/data/data.sor

.PHONY: clean
