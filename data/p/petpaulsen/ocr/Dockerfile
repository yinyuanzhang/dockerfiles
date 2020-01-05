FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
	tesseract-ocr \
	tesseract-ocr-all \
	pdfsandwich
WORKDIR ~
ENTRYPOINT ["pdfsandwich"]
