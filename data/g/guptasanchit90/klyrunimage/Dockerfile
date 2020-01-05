FROM guptasanchit90/klybuildimage as build-image

FROM guptasanchit90/klybaserunimage

# Copy Kylo source to this image
RUN mkdir -p /opt/kylo
COPY --from=build-image /opt/kylo/ /opt/kylo

# Installing Kylo
RUN useradd -r -G users kylo
RUN cd /opt/kylo/ && tar zxvf kylo-*-dependencies.tar.gz && rm -f kylo-*-dependencies.tar.gz
RUN /opt/kylo/setup/install/post-install.sh

# Create additional shells required for Docker
RUN sed -E 's/(^java .*) > .+/\1/' /opt/kylo/kylo-ui/bin/run-kylo-ui.sh > /opt/kylo/kylo-ui/bin/run-kylo-ui-interactive.sh && chmod +x /opt/kylo/kylo-ui/bin/run-kylo-ui-interactive.sh
RUN sed -i 's/file/console/g' /opt/kylo/kylo-ui/conf/log4j.properties && sed -i 's/DailyRollingFileAppender/ConsoleAppender/g' /opt/kylo/kylo-ui/conf/log4j.properties
RUN sed 's/localhost:8400/$1:$2/g' /opt/kylo/setup/data/install-templates-locally.sh > /opt/kylo/setup/data/install-templates.sh && chmod +x /opt/kylo/setup/data/install-templates.sh

RUN sed -E 's/(^java .*) > .+/\1/' /opt/kylo/kylo-services/bin/run-kylo-services.sh > /opt/kylo/kylo-services/bin/run-kylo-services-interactive.sh && chmod +x /opt/kylo/kylo-services/bin/run-kylo-services-interactive.sh
RUN sed -i 's/file/console/g' /opt/kylo/kylo-services/conf/log4j.properties && sed -i 's/DailyRollingFileAppender/ConsoleAppender/g' /opt/kylo/kylo-services/conf/log4j.properties

# Enable plugins
RUN cp /opt/kylo/setup/plugins/kylo-service-monitor-ambari-*.jar /opt/kylo/kylo-services/plugin/
RUN cp /opt/kylo/setup/plugins/kylo-service-monitor-activemq-*.jar /opt/kylo/kylo-services/plugin/
RUN cp /opt/kylo/setup/plugins/kylo-service-monitor-kylo-cluster-*.jar /opt/kylo/kylo-services/plugin/

# Install spark
RUN ln -s /opt/spark/spark-2.3.1-bin-hadoop2.7 /opt/spark/current

# Configure Nifi
RUN useradd -r nifi
RUN /opt/kylo/setup/nifi/install-nifi.sh 1.6.0 /opt/nifi nifi nifi
RUN sed -i 's/SPARK_SUBMIT=.*/SPARK_SUBMIT=\/opt\/spark\/current\/bin\/spark-submit/' /opt/kylo/setup/nifi/create-symbolic-links.sh
RUN /opt/kylo/setup/nifi/install-kylo-components.sh /opt/nifi /opt/kylo/ nifi nifi

# Install wait-for-it util
RUN ln -s /opt/wait-for-it/wait-for-it.sh /usr/sbin

## Set entrypoint
WORKDIR /opt/kylo
COPY entrypoint*.sh /
RUN chmod +x /entrypoint*.sh