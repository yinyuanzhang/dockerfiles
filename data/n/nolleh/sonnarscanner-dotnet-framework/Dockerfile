FROM mono:5.12.0
# dotnetframework + sonarcube

# openjdk-8-jre-headless 에서 씀
RUN mkdir /usr/share/man/man1

#RUN apt update && apt install -y openjdk-8-jre
#https://xmoexdev.com/wordpress/installing-openjdk-8-debian-jessie/
RUN set -ex && \
    echo 'deb http://deb.debian.org/debian jessie-backports main' \
      > /etc/apt/sources.list.d/jessie-backports.list && \
      apt update -y && apt install -t jessie-backports openjdk-8-jre-headless ca-certificates-java -y

## windows 전용이라고 써있긴한데 쓸 수 있을까 ?
## 다른 운영체제용은 dotnet core 뿐임
#https://docs.sonarqube.org/display/SCAN/Analyzing+with+SonarQube+Scanner+for+MSBuild#AnalyzingwithSonarQubeScannerforMSBuild-Features
#Note: On macOS or Linux, you can also use “mono <path to SonarScanner.MSBuild.exe>”.
COPY sonar-scanner-msbuild-4.3.1.1372-net46 .