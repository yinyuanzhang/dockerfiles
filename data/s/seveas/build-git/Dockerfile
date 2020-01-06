FROM seveas/build-debian-minimal

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get -y build-dep git && \
    apt-get -y install rpm libssl-dev acl time apache2 gnupg1 libpcre2-dev locales python-distro-info xzip && \
    rm -r /var/cache/apt/archives /var/lib/apt/lists
