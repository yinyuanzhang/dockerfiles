FROM 	oraclelinux:7-slim
MAINTAINER Michel Belleau <michel.belleau@malaiwah.com>

RUN	yum install -y --enablerepo=ol7_optional_latest,ol7_developer_EPEL gcc python2-pip libxml2-devel cairo-devel glib-devel pango-devel groff-base python-devel rrdtool-devel && \
	yum clean all --enablerepo=ol7_optional_latest,ol7_developer_EPEL && rm -rf /var/cache/yum

RUN	pip install sickmuse
CMD	["sickmuse", "--port=8080"]
EXPOSE	8080
