
# Pull base image.
FROM jenkinsci/blueocean 

USER root

RUN sed -i "s|ping:x:999:|ping:x:101:|g" /etc/group && \ 
 sed -i "s|docker:x:101:|docker:x:999:jenkins|g" /etc/group 

USER jenkins

ENTRYPOINT ["/sbin/tini", "--", "/usr/local/bin/jenkins.sh"]
