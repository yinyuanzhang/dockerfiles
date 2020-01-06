FROM  	java:openjdk-7-jre

# Add ADS Testtools
ADD   	cisstub /opt/cisstub

# Use identical group as the sftp/adi-unzip one, in case the folders are shared with host. 
RUN     addgroup --gid 30100 cisstubgroup
RUN     useradd -u 30102 -M -N -g cisstubgroup cisstubuser

COPY    docker-entrypoint.sh /

WORKDIR /opt/cisstub/

ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 	8092

CMD 	[ "/opt/cisstub/ads.sh" ]