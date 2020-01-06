FROM	python:alpine

ADD	. /app
WORKDIR	/app

RUN	pip install -r req.txt

CMD	["python", "server.py"]
