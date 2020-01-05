FROM phenompeople/oraclejre
ENV JAVA_OPTS="-XX:+UseConcMarkSweepGC -XX:CMSInitiatingOccupancyFraction=75 -XX:+UseCMSInitiatingOccupancyOnly -XX:+AlwaysPreTouch -server -Xss1m -Djava.awt.headless=true -Dfile.encoding=UTF-8 \
	 -Djna.nosys=true -Djdk.io.permissionsUseCanonicalPath=true -Dlog4j.shutdownHookEnabled=false \
	 -Dlog4j2.disable.jmx=true -Dlog4j.skipJansi=true -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/opt/phenom/dumps"
