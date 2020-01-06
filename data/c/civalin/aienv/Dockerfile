FROM python:latest
MAINTAINER kevin@house108.com.tw

RUN apt-get update \
    && apt-get -y --no-install-recommends install wget \
    && arch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \
    && wget -nv -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/1.10/gosu-$arch" \
    && chmod +x /usr/local/bin/gosu \
    && rm -r /var/lib/apt/lists/*
RUN pip3 install wheel \
    && pip3 install tensorflow keras scikit-learn h5py jupyter pandas numpy matplotlib pyfunctional
RUN mkdir -p /notebook

COPY docker-entrypoint.sh /usr/local/bin/entrypoint.sh
COPY jupyter_config /jupyter_config_template

VOLUME ["/notebook"]
EXPOSE 8888

WORKDIR /notebook
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
CMD ["jupyter", "notebook"]
