FROM python:3.6-slim-stretch

WORKDIR /app
VOLUME /data

COPY requirements.txt ./
COPY app.py /app/

RUN apt-get update
RUN apt-get install -y --no-install-recommends gcc build-essential libsnappy-dev
RUN rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get purge -y --auto-remove gcc build-essential

CMD ["python3", "app.py"]

