FROM gitea/gitea:latest

RUN apk --no-cache add asciidoctor freetype freetype-dev gcc g++ libpng python-dev py-pip python3-dev py3-pip
RUN apk --no-cache add zeromq zeromq-dev

RUN pip3 install --upgrade pip
RUN pip3 install -U setuptools
RUN pip3 install pyzmq >=17
RUN pip3 install jupyter matplotlib docutils 
