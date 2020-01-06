FROM maven:3.6.1
COPY ./jar/Excel_Parameter_Updated.jar ./jar/pCloudy-java-connector-11.0.5-jar-with-dependencies.jar ./jar/ACATS-1.0-tests.jar ./
RUN mvn install:install-file -Dfile=Excel_Parameter_Updated.jar -DgroupId=com.hw -DartifactId=cuc-framework -Dversion=1.0-SNAPSHOT -Dpackaging=jar
RUN mvn install:install-file -Dfile=pCloudy-java-connector-11.0.5-jar-with-dependencies.jar -DgroupId=pCloudy-java-connector -DartifactId=pCloudy-java-connector -Dversion=11.0.5 -Dpackaging=jar
RUN mvn install:install-file -Dfile=ACATS-1.0-tests.jar -DgroupId=com.acats.core -DartifactId=ACATS -Dversion=1.0 -Dpackaging=jar
RUN rm *.jar