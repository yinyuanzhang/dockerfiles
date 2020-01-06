FROM sonarqube:6.7.4
ENV HOME /opt/sonarqube 
RUN mkdir /opt/sonar
COPY ./conf /tmp/conf  

# Download Sonarqubes plugins.
RUN wget -P /opt/sonarqube/extensions/plugins/ \
    https://github.com/lequal/sonar-cnes-scan-plugin/releases/download/v1.2.0/sonar-cnes-scan-plugin-1.2.jar \
    https://github.com/checkstyle/sonar-checkstyle/releases/download/3.7/checkstyle-sonar-plugin-3.7.jar \
    https://github.com/lequal/sonar-cnes-cxx-plugin/releases/download/v1.1.0/sonar-cnes-cxx-plugin-1.1.jar \
    https://github.com/lequal/sonar-cnes-export-plugin/releases/download/v1.1.0/sonar-cnes-export-plugin-1.1.jar \
    https://github.com/lequal/sonar-cnes-python-plugin/releases/download/1.1/sonar-cnes-python-plugin-1.1.jar \
    https://github.com/galexandre/sonar-cobertura/releases/download/1.9.1/sonar-cobertura-plugin-1.9.1.jar \
    https://github.com/SonarSource/sonar-csharp/releases/download/6.1.0.2359/sonar-csharp-plugin-6.1.0.2359.jar \
    https://github.com/SonarOpenCommunity/sonar-cxx/releases/download/cxx-0.9.7/sonar-cxx-plugin-0.9.7.jar \
    https://github.com/spotbugs/sonar-findbugs/releases/download/3.7.0/sonar-findbugs-plugin-3.7.0.jar \
    https://binaries.sonarsource.com/Distribution/sonar-flex-plugin/sonar-flex-plugin-2.4.0.1222.jar \
    https://binaries.sonarsource.com/Distribution/sonar-java-plugin/sonar-java-plugin-5.4.0.14284.jar \
    https://binaries.sonarsource.com/Distribution/sonar-javascript-plugin/sonar-javascript-plugin-3.1.1.5128.jar \
    https://binaries.sonarsource.com/Distribution/sonar-php-plugin/sonar-php-plugin-2.10.0.2087.jar \
    https://binaries.sonarsource.com/Distribution/sonar-pmd-plugin/sonar-pmd-plugin-2.5.jar \
    https://binaries.sonarsource.com/Distribution/sonar-python-plugin/sonar-python-plugin-1.8.0.1496.jar \
    https://github.com/willemsrb/sonar-rci-plugin/releases/download/sonar-rci-plugin-1.0.1/sonar-rci-plugin-1.0.1.jar \
    https://binaries.sonarsource.com/Distribution/sonar-scm-git-plugin/sonar-scm-git-plugin-1.2.jar \
    https://binaries.sonarsource.com/Distribution/sonar-scm-svn-plugin/sonar-scm-svn-plugin-1.4.0.522.jar \
    #Outdated
    #https://github.com/stefanrinderle/sonar-softvis3d-plugin/releases/download/sonar-softVis3D-plugin-0.3.5/sonar-softVis3D-plugin-0.3.5.jar \
    https://binaries.sonarsource.com/Distribution/sonar-typescript-plugin/sonar-typescript-plugin-1.1.0.1079.jar \
    https://binaries.sonarsource.com/Distribution/sonar-web-plugin/sonar-web-plugin-2.5.0.476.jar \
    https://binaries.sonarsource.com/Distribution/sonar-xml-plugin/sonar-xml-plugin-1.4.3.1027.jar \
    && ls /opt/sonarqube/extensions/plugins

# CNES report installation
RUN wget -P /opt/sonar/extensions/cnes/ \
    https://github.com/lequal/sonar-cnes-report/releases/download/v1.1.0/sonar-report-cnes.jar \
    https://github.com/lequal/sonar-cnes-report/releases/download/v1.1.0/issues-template.xlsx \
    https://github.com/lequal/sonar-cnes-report/releases/download/v1.1.0/code-analysis-template.docx

	
# Make sonarqube owner of it's installation directories	
RUN chown sonarqube:sonarqube -R /opt \
    && ls -lrta /opt/ \
    && chown sonarqube:sonarqube -R /home \
    && ls -lrta /home/ \
    && chown sonarqube:sonarqube -R /tmp/conf

# jq required for configure-cat script.	
RUN apt update && apt install -y jq && rm -rf /var/lib/apt/lists/*
# Entry point files
COPY ./configure-cat.bash /tmp/
COPY ./init.bash /tmp/
RUN chmod 750 /tmp/init.bash
ENTRYPOINT ["/tmp/init.bash"]

