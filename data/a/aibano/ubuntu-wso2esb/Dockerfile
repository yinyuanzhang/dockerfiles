#
# WSO2 ESB 4.9
#

FROM aibano/ubuntu-java-8
MAINTAINER Osama Alaiban, megdam@gmail.com

# Set WSO2ESB Version as environment variable and use it when fetching the ZIP file
ENV WSO2ESB_VER=4.9.0

RUN wget -P /opt --user-agent="testuser" --referer="http://connect.wso2.com/wso2/getform/reg/new_product_download" http://dist.wso2.org/products/enterprise-service-bus/$WSO2ESB_VER/wso2esb-$WSO2ESB_VER.zip && \
    apt-get update && \
    apt-get install -y zip && \
    apt-get clean && \
    unzip /opt/wso2esb-4.9.0.zip -d /opt && \
    rm /opt/wso2esb-4.9.0.zip

# Expose the ports
EXPOSE 9443 9763 8243 8289

ENTRYPOINT ["/opt/wso2esb-4.9.0/bin/wso2server.sh"]
