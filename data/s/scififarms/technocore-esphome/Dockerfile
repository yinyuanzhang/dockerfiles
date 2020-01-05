ARG BUILD_FROM=esphome/esphome-base-amd64:2.0.1
FROM ${BUILD_FROM}

# Had to set voluptuous version manually
# https://github.com/esphome/issues/issues/621
# https://github.com/esphome/issues/issues/591
# TODO: hvac 0.2.17 is pretty out of date.
RUN pip3 install --no-cache-dir ptvsd==4.1.4 hvac==0.2.17  voluptuous==0.11.5
COPY . .
RUN pip3 install --no-cache-dir -e .

ENV USERNAME=""
ENV PASSWORD=""

WORKDIR /config
ENTRYPOINT ["esphome"]
CMD ["/config", "dashboard"]
