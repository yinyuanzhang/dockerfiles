FROM python:3.5-jessie

WORKDIR /nferx_gateway

ADD . /nferx_gateway

RUN mkdir ~/.pip

RUN cp /nferx_gateway/pip.conf ~/.pip

RUN apt-get -y update

RUN pip install .

EXPOSE 9916

CMD ["python", "service.py", "run", "-H", "n2-r16.w2v.servers.nferx.com", "-p", "9916", "-C", "'host=n2-r15.w2v.servers.nferx.com:db=1:password=rockofgibraltar'"]
