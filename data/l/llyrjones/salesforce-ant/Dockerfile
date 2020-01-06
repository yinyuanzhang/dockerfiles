# Use an image with ant 
FROM webratio/ant

#update and install unzip
RUN apt-get update -y && \
    apt-get install -y zip unzip \
    git

ENV LIB_VERSION 46.0

# Download salesforce ant lib file and move to ant lib folder
RUN cd tmp && \
    wget -q https://gs0.salesforce.com/dwnld/SfdcAnt/salesforce_ant_${LIB_VERSION}.zip && \
    unzip salesforce_ant_${LIB_VERSION}.zip && \
    cp ant-salesforce.jar /opt/ant/lib/ && \
    rm -rf *.* && \
    rm -rf sample
    


