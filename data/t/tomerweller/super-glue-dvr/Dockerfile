FROM nelsond/ffmpeg

RUN apt-get update
RUN apt-get -y install software-properties-common
RUN add-apt-repository -y ppa:george-edison55/cmake-3.x
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
		git \
		python2.7-dev \
		python-pip \
        wget \
        unzip \
        cmake \
        build-essential

RUN wget -qO- -O ccextractor.zip https://www.dropbox.com/s/to3gnfctrsdmooe/ccextractor.zip?dl=1 --no-check-certificate
RUN unzip ccextractor.zip
RUN rm ccextractor.zip
WORKDIR /ccextractor/src
RUN cmake . && make && make install

WORKDIR /

RUN echo "version3.0"

RUN mkdir /super-glue-dvr
COPY . /super-glue-dvr

WORKDIR /super-glue-dvr
RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED True
ENV SUPERGLUE_HOST="http://super-glue.media.mit.edu"
ENV BUBBLE_HOST="http://um-bubble.media.mit.edu:10022"
ENV MONGO_HOST="mongodb://um.media.mit.edu:27017/super-glue"

ENV PAPERTRAIL_ADDRESS="logs5.papertrailapp.com"
ENV PAPERTRAIL_PORT=26276
ENV TMS_API_KEY="rm34r663sdax6ggvpcerjfs3"
ENV TMS_LINEUP_ID="USA-DITV506-DEFAULT"

EXPOSE 5050:5050
EXPOSE 1234:1234/udp

CMD python supergluedvr/record_manager.py
