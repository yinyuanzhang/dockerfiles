FROM python:alpine

ENV APIHOST=api-bracelet
ENV APIPORT=80



ADD __main__.py /root
ADD _version.py /root
ADD requirements.txt /root

RUN pip install -r /root/requirements.txt

EXPOSE ${APIPORT}

CMD python /root/__main__.py -H${APIHOST} -p${APIPORT}