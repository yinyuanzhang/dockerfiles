FROM python:3

COPY . /app

WORKDIR /app

RUN pip install bs4

RUN pip install requests_html

RUN pip install pandas

RUN pip install firebase-admin

CMD [ "python", "./amazon-scraper.py" ]
