FROM huzhenghui/sdkman

LABEL maintainer="hu@daonao.com"

LABEL trigger_comment="SDKMAN updated to 5.6.2+294"

RUN bash -c 'source /root/.sdkman/bin/sdkman-init.sh; sdk version; echo -e "\n----------" $? "----------\n"' && \
    bash -c 'source /root/.sdkman/bin/sdkman-init.sh; echo y | sdk install java 8.0.181-oracle; echo -e "\n----------" $? "----------\n"' && \
    bash -c 'source /root/.sdkman/bin/sdkman-init.sh; export' && \
    bash -c 'source /root/.sdkman/bin/sdkman-init.sh; ${JAVA_HOME}/bin/java -version'
