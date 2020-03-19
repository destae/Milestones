run: 
	- make build

build:
	docker build -t cs4500:0.1 .
	- docker run -ti -v "$$(pwd)/src":/src cs4500:0.1 bash -c "cd ./src; python3 main.py"