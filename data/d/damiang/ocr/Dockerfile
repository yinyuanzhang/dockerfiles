FROM ubuntu:18.04

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

RUN apt-get update && apt-get install -y tesseract-ocr-all
RUN apt -y install python3-opencv
RUN apt -y install python3-pip

RUN mkdir /app
WORKDIR /app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./ ./

EXPOSE 5000

CMD ["gunicorn", "-b 0.0.0.0:5000", "index:app"]