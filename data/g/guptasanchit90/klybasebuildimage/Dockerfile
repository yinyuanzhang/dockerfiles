FROM centos

RUN yum install -yy wget git which java-1.8.0-openjdk-devel bzip2 rpm-build

# Install NodeJS and Yarn
RUN curl --silent --location https://rpm.nodesource.com/setup_8.x | bash - && yum install nodejs -yy
RUN curl -sL https://dl.yarnpkg.com/rpm/yarn.repo -o /etc/yum.repos.d/yarn.repo && yum install yarn -yy

# Install Maven
RUN mkdir -p /usr/local/src && cd /usr/local/src && wget http://apache.crihan.fr/dist/maven/maven-3/3.5.4/binaries/apache-maven-3.5.4-bin.tar.gz
RUN cd /usr/local/src && tar -xf apache-maven-3.5.4-bin.tar.gz && rm -f apache-maven-3.5.4-bin.tar.gz && mv apache-maven-3.5.4/ apache-maven/