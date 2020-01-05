FROM jodogne/orthanc-plugins

LABEL name="orthanc-examples"
LABEL version="0.3"
LABEL maintainer="casaper"

RUN apt-get update \
  && apt-get install -y \
    dcmtk \
    curl \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

COPY ./OrthancConfiguration.json /etc/orthanc/orthanc.json
COPY ./images /images
COPY ./scripts /scripts

# make scripts and jq globally accaccible through path
RUN chmod uga+x /scripts/*.sh /scripts/jq-linux64 \
  && ln -sf /scripts/delete_images.sh /usr/bin/delete_images \
  && ln -sf /scripts/upload_images.sh /usr/bin/upload_images \
  && ln -sf /scripts/jq-linux64 /usr/bin/jq

EXPOSE 4242
EXPOSE 8042

ENTRYPOINT [ "Orthanc" ]
CMD [ "/etc/orthanc/" ]
