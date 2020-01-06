FROM python:3.7.5-slim-buster
RUN apt-get -y update && apt-get install -y gcc

WORKDIR usr/src/app

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./bot.py" ]
