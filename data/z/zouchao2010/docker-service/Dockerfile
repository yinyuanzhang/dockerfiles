FROM python:2.7

VOLUME /var/lib/docker-service
ADD . /opt/docker-service

WORKDIR /opt/docker-service

RUN pip install tornado \

    && rm -rf /tmp/pip-*

CMD ["python2", "service.py", "--log_file_prefix=/var/lib/docker-service/service.log", "--logging=debug", "--log_to_stderr"]

#python service.py --log_file_prefix=/Users/chao/docker-service.log --logging=debug --log_to_stderr