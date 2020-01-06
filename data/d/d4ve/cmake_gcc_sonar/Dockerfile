
FROM d4ve/gcc_extended:1.0.0

RUN  apt-get update
RUN  apt-get install --yes unzip lcov

RUN cd /usr/local/share &&  wget https://sonarcloud.io/static/cpp/build-wrapper-linux-x86.zip &&  unzip build-wrapper-linux-x86.zip &&  ln -s /usr/local/share/build-wrapper-linux-x86/build-wrapper-linux-x86-64 /usr/local/bin/build-wrapper-linux
RUN cd /usr/local/share &&  wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-3.2.0.1227-linux.zip &&  unzip sonar-scanner-cli-3.2.0.1227-linux.zip &&  ln -s /usr/local/share/sonar-scanner-3.2.0.1227-linux/bin/sonar-scanner /usr/local/bin/sonar-scanner

CMD ["/bin/bash"]
