FROM python:3
ADD main.py /

VOLUME /download/

RUN pip install manga-py
RUN pip install sqlalchemy
RUN pip install pymysql


CMD ["python", "./main.py"]