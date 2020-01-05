FROM centos:centos7

RUN yum -y update; yum clean all
RUN yum -y install epel-release; yum clean all
RUN yum -y install redis; yum clean all

EXPOSE 6379

# log on stdout instead of writing to file
#RUN sed -i 's/^\(logfile\s*\).*$/\1""/g' /etc/redis.conf

# # Fix permissions to allow for running on openshift
# COPY fix-permissions.sh ./
# RUN ./fix-permissions.sh /var/log/redis/ && \
#     ./fix-permissions.sh /var/lib/redis/

# By default will run as random user on openshift and the redis user (997)
# everywhere else
USER 997
	
ENTRYPOINT ["redis-server"]
CMD ["/etc/redis.conf", "--bind", "0.0.0.0"]
