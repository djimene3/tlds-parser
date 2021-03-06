
all: client server

client:
	go get
	protoc parser.proto --go_out=plugins=grpc:.

server:
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. parser.proto

docker: docker-build docker-run

docker-build:
	docker build -t puradox/tlds-parser:1.1.0 -t puradox/tlds-parser:latest .

docker-run:
	docker run -it puradox/tlds-parser:latest

publish: docker-build
	docker push puradox/tlds-parser:1.1.0
	docker push puradox/tlds-parser:latest
