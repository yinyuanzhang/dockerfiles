
FROM python:3

WORKDIR /SOA_APIGATEWAY

COPY . /SOA_APIGATEWAY

RUN python -m pip install -r requirements.txt

EXPOSE 5000

ENV NAME Catalog

CMD ["python","app.py"]
