FROM mpender/ansible-docker 

RUN yum install wget java -y &&  wget https://kent.dl.sourceforge.net/project/jasypt/jasypt/jasypt%201.9.2/jasypt-1.9.2-dist.zip
RUN unzip jasypt-1.9.2-dist.zip && chmod -R +x jasypt-1.9.2/bin
RUN sh jasypt-1.9.2/bin/encrypt.sh input="This is what I want to encrypt" password="EncryptionKey12345"