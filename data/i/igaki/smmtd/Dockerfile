FROM igaki/sshmonitmongo

MAINTAINER igaki version:0.1

RUN yum update -y

##fluentd install
ADD ./td.repo /etc/yum.repos.d/td.repo
RUN yum install -y td-agent
RUN sed -i -e "s/---user td-agent/---user root/" /etc/init.d/td-agent;sed -i -e "s/--group td-agent/--group root/" /etc/init.d/td-agent
RUN /usr/lib64/fluent/ruby/bin/fluent-gem install fluent-plugin-record-modifier

ADD ./td-agent.conf /etc/td-agent/
ADD ./td-agent_monit.conf /etc/monit/conf.d/

RUN chown root:root -R /etc/monit*;chmod 700 /etc/monit.conf

#ssh
EXPOSE 22
#monit
EXPOSE 8001
#mongo
EXPOSE 27017

CMD ["/usr/bin/monit", "-I", "-c", "/etc/monit.conf"]