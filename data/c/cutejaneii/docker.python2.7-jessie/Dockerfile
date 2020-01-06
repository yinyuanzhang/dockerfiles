FROM python:2.7.16-jessie

RUN pip install flask wget
RUN pip install pandas cassandra-driver
RUN pip install Pillow scp

WORKDIR /
RUN mkdir nfs

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV HDF5_USE_FILE_LOCKING FALSE
ENV pyfile main.py

COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

COPY . /app

CMD ["sh","entrypoint.sh"]
