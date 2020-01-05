from python:2
RUN apt-get -y update
RUN pip install pyjojo 
RUN apt-get -y install apache2-utils git && apt-get clean
RUN git clone https://github.com/imaidev/pyjojo-utils.git
RUN chmod +x /pyjojo-utils/srv/*
CMD /usr/local/bin/pyjojo -d --dir /pyjojo-utils/srv
