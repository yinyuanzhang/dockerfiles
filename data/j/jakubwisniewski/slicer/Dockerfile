FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y python3-pip 
RUN pip3 install awscli boto3

# set work directory
RUN mkdir /slicer
WORKDIR /slicer

COPY requirements.txt /slicer/

RUN pip3 install -r requirements.txt --no-cache-dir 


ADD slicer.py /
CMD ["/slicer.py"]
