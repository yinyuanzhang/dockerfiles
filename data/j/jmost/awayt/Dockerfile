FROM python:3.8.0-buster
WORKDIR /usr/src/app
COPY requirements.txt ./
COPY awayt.py ./
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["./awayt.py"]
