FROM python:alpine3.7
COPY ./app/app.py /var
COPY ./app /var
COPY requirements.txt /var
WORKDIR /var
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]
