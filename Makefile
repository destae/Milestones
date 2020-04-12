run:
	-make build

build:
	python3 -m verify.src 0

test:
	-python3 -m unittest discover -s verify

