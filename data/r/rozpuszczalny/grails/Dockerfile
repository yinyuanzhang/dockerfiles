FROM java:8
MAINTAINER Tomasz Domański <rozpuszczalny@gmail.com>

RUN /bin/bash -c "apt-get update -qq && apt-get install -y -qq unzip zip;\
curl -sSL https://get.sdkman.io | bash;\
echo sdkman_auto_answer=true > /root/.sdkman/etc/config;\
source /root/.sdkman/bin/sdkman-init.sh;\
sdk install grails 2.5.6 < /dev/null;\
sdk use grails 2.5.6"
