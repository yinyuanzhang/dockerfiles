FROM tomcat:8

# 设置时区
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
	sed -i "s/\$JAVA_OPTS \$JSSE_OPTS/\$JAVA_OPTS \$JSSE_OPTS -Duser.timezone=GMT+08/g" /usr/local/tomcat/bin/catalina.sh