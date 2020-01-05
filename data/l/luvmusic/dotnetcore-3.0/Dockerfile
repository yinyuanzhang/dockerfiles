FROM centos:centos7
RUN rpm -Uvh https://packages.microsoft.com/config/rhel/7/packages-microsoft-prod.rpm
RUN yum install -y dotnet-sdk-3.0
RUN /bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo 'Asia/Shanghai' >/etc/timezone
