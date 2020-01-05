
FROM python:3.4

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
# ssh

RUN apt-get update \
	&& apt-get install -y --no-install-recommends openssh-server \
	&& echo "root:Docker!" | chpasswd 

COPY sshd_config /etc/ssh/
COPY init_container.sh /bin
RUN chmod 777 /bin/init_container.sh
	
EXPOSE 8000 2222
ENTRYPOINT ["/bin/init_container.sh"]