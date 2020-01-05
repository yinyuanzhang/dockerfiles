FROM centos
MAINTAINER KUNIYOSHI Kouji <kuniyoshi.kouji@gmail.com>
RUN ["yum", "install", "-y", "epel-release"]
RUN ["yum", "install", "-y", "R"]
RUN ["yum", "install", "-y", "libjpeg-devel"]
RUN ["yum", "install", "-y", "libpng-devel"]
RUN ["mkdir", "-p", "/opt/R/library"]
ADD library/ /opt/R/library/
RUN find /opt/R/library -type f -print0 | xargs -0 R CMD INSTALL
WORKDIR /opt/R/
CMD ["R", "--no-save"]
