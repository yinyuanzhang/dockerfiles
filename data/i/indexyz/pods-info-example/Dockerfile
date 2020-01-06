FROM python:3.7.5-alpine3.10

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY app /app

ENTRYPOINT [ "python" ]
CMD [ "/app/api.py" ]