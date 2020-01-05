FROM bockpl/bocompute
MAINTAINER Seweryn Sitarski

# Narzedzia developerskie
RUN (yum -y groupinstall 'Development Tools') && \
(yum -y install openssl-devel.x86_64)

# Skrypty pomocne przy kompilacji/konfiguracji oprogramowania
ADD tools/make_python_env /root/tools/
