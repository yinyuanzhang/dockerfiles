FROM python:alpine

ENV APIHOST=api-bracelet
ENV MONGOHOST=api-bracelet-mongodb
ENV MONGOPORT=27017
ENV MONGODB=bracelet
ENV MONGOUSER=admin
ENV MONGOPASSWORD=api-bracelet

ADD __main__.py /root
ADD _version.py /root
ADD requirements.txt /root

RUN pip install -r /root/requirements.txt

EXPOSE 80

CMD python /root/__main__.py -A${APIHOST} -H${MONGOHOST} -P${MONGOPORT} -D${MONGODB} -u${MONGOUSER} -p${MONGOPASSWORD}