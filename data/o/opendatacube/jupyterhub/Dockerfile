FROM opendatacube/datacube-core

RUN apt-get update && apt-get install -y npm nodejs
RUN npm install -g configurable-http-proxy

# Get dependencies for Jupyter
RUN pip3 install \
    jupyter jupyterhub jupyterlab matplotlib folium \
    && rm -rf $HOME/.cache/pip

RUN mkdir /conf && chmod -R 777 /conf
ENV DATACUBE_CONFIG_PATH=/conf/datacube.conf

RUN chmod -R 777 /opt/odc

ENV HOME=/home/jovyan
RUN mkdir -p $HOME && chmod -R 777 $HOME

WORKDIR $HOME

CMD ["jupyterhub", "--ip=\"*\""]
