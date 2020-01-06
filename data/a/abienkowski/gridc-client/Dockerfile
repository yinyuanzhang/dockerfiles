FROM ubuntu:16.04
# -- define environment variables; all shall be provided at run-time
ENV SERVER_ADDR="" \
    GRID_KEY="" \
    GRID_SECRET=""
# -- update image
RUN apt-get update \
  && apt-get -y upgrade \
  && apt-get -y install python-pip jq \
  && pip install envtpl \
  && rm -rf /var/lib/apt/lists/*
# -- install grid connect client
ADD gridc-1.1-linux_64 /usr/local/bin/gridc
# -- add entrypoint script
COPY ./gridc-options.sh /
RUN chmod +x /gridc-options.sh \
  && mkdir -p /etc/gridc
# -- copy template file
ADD config-tunnels.cfg.j2 /etc/gridc/config-tunnels.cfg.j2
ADD config-tunnelsperslave.cfg.j2 /etc/gridc/config-tunnelsperslave.cfg.j2
# -- set entrypoint script
ENTRYPOINT ["/usr/loca/bin/gridc"]
# -- set grid connect options
CMD ["gridc-options.sh"]
