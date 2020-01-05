FROM python:3.7.3
ARG SERVICE_NAME
ARG SERVICE_VERSION
ENV SERVICE_NAME $SERVICE_NAME
ENV SERVICE_VERSION $SERVICE_VERSION
RUN mkdir /app
COPY . /app
RUN touch /app/.env
RUN pip install --find-links /app/wheels -r /app/requirements.txt
RUN pip install gunicorn
WORKDIR /app
EXPOSE 5001
CMD ["./boot.sh"]
