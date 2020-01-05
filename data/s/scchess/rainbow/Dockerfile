FROM ubuntu

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y vim && \
    apt-get install -y g++ && \
    apt-get install -y python3-pip && \
	apt-get install -y zip && \
	apt-get install -y curl && \
	apt-get install -y ffmpeg && \
	apt-get install -y imagemagick && \
    apt-get install -y git-core

RUN pip3 install bs4 && \
	pip3 install bottle && \
	pip3 install python-chess && \
	pip3 install waitress && \
	pip3 install pymysql && \
    pip3 install scipy && \
    pip3 install tensorflow==1.5 && \
    pip3 install Pillow && \
    pip3 install ipython && \
	pip3 install requests

RUN curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
RUN chmod a+rx /usr/local/bin/youtube-dl

RUN pip3 install awscli --upgrade --user
ENV PATH="~/.local/bin:${PATH}"

COPY . /opt/Rainbow

RUN mkdir -p ~/.aws
RUN cp -rf /opt/Rainbow/config ~/.aws
RUN cp -rf /opt/Rainbow/credentials ~/.aws

EXPOSE 9100

WORKDIR /opt/Rainbow
CMD ["python3", "/opt/Rainbow/server.py", "/opt/Rainbow/models/allModel", "9100"]
