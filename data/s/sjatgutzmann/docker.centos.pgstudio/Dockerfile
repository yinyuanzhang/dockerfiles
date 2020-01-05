#!Dockerfile
#AUTOR: sjatgutzmann

FROM sjatgutzmann/docker.centos.tomcat
MAINTAINER Sven Jörns <sjatgutzmann@gmail.com>
ARG HTTP_PORT=9898

WORKDIR ${CATALINA_HOME}

RUN git clone https://github.com/sjatgutzmann/pgstudio.git

WORKDIR ${CATALINA_HOME}/pgstudio

# because ant need bash profile, use exec mode with --login of RUN
RUN ["/bin/bash", "--login", "-c", "ant clean && ant deploy"]
# bug in Dockerfiles an inherit Volumes https://github.com/docker/docker/issues/3639#issuecomment-144206271
RUN cp -va war ${CATALINA_HOME}/webapps/pgstudio
ENTRYPOINT ["/run.bash"]
# start as bash with the user tomcat
CMD ["bash"]
# start tomcat in console (defualt)
CMD ["run"]
