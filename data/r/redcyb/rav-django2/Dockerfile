FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /ravenre
WORKDIR /ravenre
COPY ./ravenre/requirements.txt /ravenre/
COPY ./app-entrypoint.sh /
RUN pip install -r requirements.txt
EXPOSE 8000 9191
ENTRYPOINT ["/app-entrypoint.sh"]
