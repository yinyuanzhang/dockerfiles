FROM centos:latest

# Keep general RPM stuff up to date.
RUN yum -y update && yum -y install maven git

# Put a build script in a sensible location
COPY build /usr/local/bin
ENTRYPOINT [ "/usr/local/bin/build" ]


