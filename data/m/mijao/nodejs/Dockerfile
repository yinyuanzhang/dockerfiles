FROM centos
MAINTAINER  Angelo E. Valdez "angeloe.valdez@gmail.com"
RUN yum -y install epel-release && yum -y install nodejs npm git nano curl 
ADD /example /home/example
WORKDIR /home/
ENTRYPOINT ["/bin/node"]
CMD ["example/hello.js"]
EXPOSE 8000
