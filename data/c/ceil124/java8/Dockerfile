FROM ceil124/ctbase

RUN yum update -y \
  && yum install -y java-1.8.0-openjdk-devel \
  && yum clean all \
  && rm -rf /tmp/* rm -rf /var/cache/yum/*

CMD ["java", "-jar", "/app/app.jar"]