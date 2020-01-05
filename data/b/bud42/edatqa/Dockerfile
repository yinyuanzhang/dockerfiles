FROM ubuntu:trusty

# Install packages required by dax
RUN apt-get update && apt-get install -y \
python-pip libfreetype6-dev pkg-config libxml2-dev libxslt1-dev \
python-dev zlib1g-dev python-numpy python-scipy python-requests \
python-urllib3 python-pandas

RUN pip install matplotlib --upgrade
RUN pip install pandas --upgrade
RUN pip install seaborn --upgrade
RUN pip install pydicom==0.9.9

# Install dax
RUN pip install https://github.com/VUIIS/dax/archive/v0.7.1.zip

# Install src
COPY src /opt/src/

# Make bind points for I/O
RUN mkdir /INPUTS
RUN mkdir /OUTPUTS

# Get the spider code
COPY spider.py /opt/spider.py
ENTRYPOINT ["python", "/opt/spider.py"]
