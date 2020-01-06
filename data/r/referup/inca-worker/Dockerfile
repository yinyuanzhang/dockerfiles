FROM referup/apache:bionic

RUN \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive \
    apt-get -y install \
      inotify-tools \
      moreutils \
  && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

RUN \
  mkdir -vp \
    /usr/share/google/ \
    /etc/cloe_run/first-run.d/ \
    /etc/cloe_run/pre-run.d/ \
  && \
  curl --location --silent --show-error \
    --output /usr/share/google/get_metadata_value \
    https://raw.githubusercontent.com/GoogleCloudPlatform/compute-image-packages/legacy/google-startup-scripts/usr/share/google/get_metadata_value \
  && \
  curl --location --silent --show-error \
    --output /etc/cloe_run/pre-run.d/10-gcp-suspend-by-metadata \
    https://raw.githubusercontent.com/pataquets/cloe_run/master/scripts/gcp-suspend-by-metadata

COPY files/etc/default/cloe_run /etc/default/cloe_run

COPY files/usr/local/bin/cloe_run /usr/local/bin/
COPY files/etc/cloe_run/ /etc/cloe_run/
RUN \
  chmod -v a+x \
    /usr/local/bin/cloe_run \
    /etc/cloe_run/first-run.d/* \
    /etc/cloe_run/pre-run.d/* \
    /usr/share/google/get_metadata_value

RUN phpdismod -s ALL referup-newrelic

CMD [ "sudo", "-Eu", "www-data", "cloe_run" ]
