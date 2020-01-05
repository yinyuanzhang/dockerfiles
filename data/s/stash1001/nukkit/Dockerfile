FROM java

ADD https://ci.nukkitx.com/job/NukkitX/job/Nukkit/job/master/lastSuccessfulBuild/artifact/target/nukkit-1.0-SNAPSHOT.jar /opt/nukkit-jar/nukkit.jar

VOLUME ["/opt/data"]

ADD nukkit.yml /opt/nukkit-files/nukkit.yml

ADD plugins /opt/nukkit-files/plugins

EXPOSE 19132

CMD cd /opt/data && cp -R /opt/nukkit-files/* /opt/data/ && /bin/sh -c "java -Xmx1024M -Xms1024M -jar /opt/nukkit-jar/nukkit.jar"