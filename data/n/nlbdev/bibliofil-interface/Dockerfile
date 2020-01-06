FROM nlbdev/pentaho-pi:8.3-20191218
LABEL MAINTAINER Jostein Austvik Jacobsen <jostein@nlb.no> <http://www.nlb.no/>

# Install dependencies
RUN apt-get update && apt-get install -y \
    git \
    mariadb-client \
    openssh-client \
    python-mysqldb \
    wget \
    rsync \
    python3 \
    python3-pip

RUN mkdir -p /opt/bibliofil-interface/
WORKDIR /opt/bibliofil-interface/

# Install dependencies
COPY src/requirements.txt .
RUN pip3 install -r requirements.txt

# Set up automatic import of Bibliofil database
COPY src/ .

CMD /opt/bibliofil-interface/loop.sh 3600
