FROM python:3.6-slim

COPY . /

WORKDIR /

RUN pip install -r requirements.txt

RUN chmod +x ./start.sh

CMD ["./start.sh"]