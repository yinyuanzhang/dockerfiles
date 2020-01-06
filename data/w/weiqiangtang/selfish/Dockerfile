FROM python:3.6

RUN echo hello
RUN echo wanna trigger github and dockerhub hook

WORKDIR /application

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "selfish.py"]