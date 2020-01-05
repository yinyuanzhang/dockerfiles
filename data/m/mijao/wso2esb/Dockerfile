FROM angeloevaldez/jdk8
MAINTAINER Angelo E. Valdez <angeloe.valdez@gmail.com>


RUN wget -P /opt --user-agent="testuser" \
		--referer="http://connect.wso2.com/wso2/getform/reg/new_product_download" \
		http://dist.wso2.org/products/enterprise-service-bus/5.0.0/wso2esb-5.0.0.zip 
RUN yum install -y unzip && unzip /opt/wso2esb-5.0.0.zip -d /opt
RUN rm /opt/wso2esb-5.0.0.zip

EXPOSE 8243 8280 9443 9763 9999 11111
ENTRYPOINT ["/opt/wso2esb-5.0.0/bin/wso2server.sh"]

