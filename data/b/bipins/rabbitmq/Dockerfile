FROM rabbitmq:latest
 
MAINTAINER Bipindra Shrestha "bipindra.shrestha@gmail.com"

RUN rabbitmq-plugins enable --offline rabbitmq_management rabbitmq_auth_backend_ldap rabbitmq_shovel rabbitmq_shovel_management
 
EXPOSE 5672
EXPOSE 15672
