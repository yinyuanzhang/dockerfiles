FROM jenkins/jenkins:2.176.3
USER root
RUN wget http://mirrors.tuna.tsinghua.edu.cn/apache/maven/maven-3/3.5.4/binaries/apache-maven-3.5.4-bin.tar.gz&&tar xzvf apache-maven-3.5.4-bin.tar.gz -C /opt/
ENV PATH /opt/apache-maven-3.5.4/bin:$PATH
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py&&python get-pip.py -i http://pypi.douban.com/simple --trusted-host pypi.douban.com&&pip install ansible==2.6.2 -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
ENV JAVA_HOME /usr/local/openjdk-8
ENV PATH /usr/local/openjdk-8/bin:$PATH
RUN apt-get update&&apt-get install -y sshpass
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -&&apt-get install -y nodejs