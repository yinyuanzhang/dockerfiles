# use debian as base image
FROM debian:latest

ARG snap_version=7

# get list of installable packets and install wget
RUN apt-get update && \
    apt-get -y install \
        'wget'

# download snap installer
RUN wget http://step.esa.int/downloads/${snap_version}.0/installers/esa-snap_sentinel_unix_${snap_version}_0.sh

#change file execution rights for snap installer
RUN chmod +x esa-snap_sentinel_unix_${snap_version}_0.sh

# install snap with gpt
RUN ./esa-snap_sentinel_unix_${snap_version}_0.sh -q

# link gpt so it can be used systemwide
RUN ln -s /usr/local/snap/bin/gpt /usr/bin/gpt

# set gpt max memory to 4GB
RUN sed -i -e 's/-Xmx1G/-Xmx4G/g' /usr/local/snap/bin/gpt.vmoptions

# add airflow sudo user
# RUN groupadd -g 999 -r airflow && useradd --no-log-init --create-home -u 999 -r -g airflow airflow && usermod -aG sudo airflow
# USER 999:999
RUN groupadd -g 1000 -r airflow && useradd --no-log-init --create-home -u 1000 -r -g airflow airflow && usermod -aG sudo airflow
USER 1000:1000

# set entrypoint
ENTRYPOINT ["/usr/local/snap/bin/gpt"]
CMD ["-h"]