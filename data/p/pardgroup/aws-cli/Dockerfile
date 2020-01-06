FROM python:3

RUN pip install awsebcli --upgrade --user

COPY loop.sh ./
COPY boot.sh /etc/profile.d/boot.sh

RUN echo "source /etc/profile.d/boot.sh" >> /root/.bashrc

RUN pip install awscli --upgrade --user

RUN apt-get update
RUN apt-get install -y -qq groff

CMD [ "bash", "loop.sh" ]
