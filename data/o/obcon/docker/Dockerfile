FROM obcon/alpine
USER root
RUN apk --update add docker@community
EXPOSE 2375
#CMD ["docker", "daemon", "-H", "unix:///var/run/docker.sock", "-H", "tcp://0.0.0.0"]
CMD ["docker", "daemon", "-H", "unix:///var/run/docker.sock", "-H", "tcp://0.0.0.0", "--insecure-registry", "registry:5000", "--registry-mirror", "http://registry:5000"]
