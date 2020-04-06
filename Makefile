run:
	-make build

build:
	python3 -m milestone_4.src

test:
	-python3 -m unittest discover -s milestone_4

