FROM ubuntu:18.04
RUN apt-get update && apt-get upgrade -y && apt-get install -y software-properties-common python-pip
# nano wget unzip
ADD ./ /opt/fotomap
WORKDIR /opt/fotomap
RUN pip install -r requirements.txt
CMD ["python", "app.py"]