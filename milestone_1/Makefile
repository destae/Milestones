run: 
	- make build

build:
	cd data; unzip data.zip 
	docker build -t cs4500:0.1 .

run_test:
	-python3 -m unittest

clean:
	- rm data/*.csv
	- rm data/*.sor


.PHONY: clean
