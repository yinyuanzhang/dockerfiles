from ubuntu


#Install nikto
RUN apt-get update && apt-get install wget git python-pip -y
RUN pip2 install --upgrade pip
RUN pip2 install xmltodict amqplib


#Instal sqlmap
WORKDIR /opt/
RUN wget https://github.com/Arachni/arachni/releases/download/v1.5.1/arachni-1.5.1-0.5.12-linux-x86_64.tar.gz
RUN tar zxvf arachni-1.5.1-0.5.12-linux-x86_64.tar.gz
RUN rm arachni-1.5.1-0.5.12-linux-x86_64.tar.gz
RUN mv arachni-1.5.1-0.5.12 arachni

COPY  ./code /code
RUN chmod +x /code/scanner.py


CMD python /code/scanner.py
