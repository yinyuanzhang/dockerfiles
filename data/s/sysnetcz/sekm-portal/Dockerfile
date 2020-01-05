FROM python:3
RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean

ARG PROJECT=sekm-portal
ARG PROJECT_DIR=/var/www/${PROJECT}
RUN mkdir -p $PROJECT_DIR
WORKDIR $PROJECT_DIR
ADD . $PROJECT_DIR
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV RUN_DIR=$PROJECT_DIR 
ENV DJANGO_DB_NAME=default
ENV DJANGO_SU_NAME=admin
ENV DJANGO_SU_EMAIL=admin3@sekm.cz
ENV DJANGO_SU_PASSWORD=Sekm312345
ENV DJANGO_SU_FIRSTNAME=admin
ENV DJANGO_SU_LASTNAME=admin
#ENV DJANGO_SETTINGS_MODULE sekm_portal.settings.testing

EXPOSE 8000
STOPSIGNAL SIGINT

#ENTRYPOINT ["python", "manage.py"]
#CMD ["collectstatic", "--noinput"]
#CMD ["migrate"]
#CMD [ "runserver", "0.0.0.0:8000" ]
  
RUN chmod +x ${RUN_DIR}/docker-entrypoint.sh
ENTRYPOINT ${RUN_DIR}/docker-entrypoint.sh
