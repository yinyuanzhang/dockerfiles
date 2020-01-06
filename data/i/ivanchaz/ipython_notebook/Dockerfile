FROM debian:jessie

MAINTAINER ivan.chaz@gmail.com

WORKDIR /root

RUN apt-get update \
	&& apt-get install -y --force-yes --no-install-recommends \
		wget ca-certificates build-essential \
                gfortran libopenblas-dev liblapack-dev libpng12-dev libfreetype6-dev pkg-config \
                python3 python3-dev python3-pip \
	&& rm -rf /var/lib/apt/lists/* \
        && ln -s /usr/bin/python3 /usr/bin/python \
        && chmod +x /usr/bin/python \
        && pip3 install jupyter matplotlib numpy scipy sklearn cython pandas \ 
        && jupyter notebook --generate-config \
        && sed -i "s/.*c.NotebookApp.ip.*/c.NotebookApp.ip = '*'/" ~/.jupyter/jupyter_notebook_config.py

RUN wget -O dropbox.tar.gz "https://www.dropbox.com/download?plat=lnx.x86_64" \
        && tar -xzf dropbox.tar.gz \
        && rm dropbox.tar.gz
 
RUN apt-get purge -y build-essential wget gfortran

EXPOSE 8888

ADD start.sh ./
RUN sed -i "s///" ./start.sh \
       && chmod a+x ./start.sh

CMD ./start.sh
