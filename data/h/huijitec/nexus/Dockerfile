FROM sonatype/nexus3:latest

EXPOSE 8081
USER nexus

ENV TZ="Asia/Shanghai" \
  INSTALL4J_ADD_VM_PARAMS="-Xms2703m -Xmx2703m -XX:MaxDirectMemorySize=2703M -Djava.util.prefs.userRoot=${NEXUS_DATA}/javaprefs"

# RUN timedatectl set-timezone Asia/Shanghai \
#   && echo "Asia/Shanghai" > /etc/timezone \
#   && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

CMD ["sh", "-c", "${SONATYPE_DIR}/start-nexus-repository-manager.sh"]
