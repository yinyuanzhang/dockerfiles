FROM phusion/baseimage:0.9.18

CMD ["python3", "api.py"]
ENV ENV docker
ENV DEPLOY_FLD /var/www/onfido/app
ENV REDIS_HOST redis

RUN mkdir -p ${DEPLOY_FLD}
WORKDIR ${DEPLOY_FLD}

EXPOSE 5000

RUN apt-get update && apt-get install -y python3-pip

ADD app/* ./

RUN pip3 install -r requirements.txt
RUN rm -f requirements.txt

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
