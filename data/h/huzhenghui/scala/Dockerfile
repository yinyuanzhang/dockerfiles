FROM huzhenghui/java:version-9.0.4-oracle

LABEL maintainer="hu@daonao.com"

LABEL trigger_comment="ERROR: Highland: unable to process this request"

RUN bash -c 'source /root/.sdkman/bin/sdkman-init.sh; sdk version; echo -e "\n----------" $? "----------\n"' && \
    bash -c 'source /root/.sdkman/bin/sdkman-init.sh; export' && \
    bash -c 'source /root/.sdkman/bin/sdkman-init.sh; ${JAVA_HOME}/bin/java --version' && \
    bash -c 'source /root/.sdkman/bin/sdkman-init.sh; sdk install scala 2.12.4; echo -e "\n----------" $? "----------\n"' && \
    bash -c 'source /root/.sdkman/bin/sdkman-init.sh; export'
