FROM node:7.4

MAINTAINER ITGEL GANBOLD <itgel.ganbold1@gmail.com>

RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y install python3 && \
    apt-get -y install python3-pip && \
    apt-get install -y python3-pandas && \
    pip3 install matplotlib && \
    pip3 install scikit-learn && \
    pip3 install seaborn && \	
    pip3 install jupyter

WORKDIR /srv/notebooks/

EXPOSE 8888

CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=*"]
