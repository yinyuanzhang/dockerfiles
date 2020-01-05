FROM edraizen/haddock:latest

# install necessary dependencies
RUN apt-get update && \
    apt-get install -y python-pip

RUN pip install toil[all]

COPY QueueSubmit_toil.py /opt/haddock2.2/Haddock/Main/
RUN rm /opt/haddock2.2/Haddock/Main/QueueSubmit.py
RUN ln -s /opt/haddock2.2/Haddock/Main/QueueSubmit_toil.py /opt/haddock2.2/Haddock/Main/QueueSubmit.py

RUN rm /opt/haddock2.2/wrapper.sh

COPY wrapper.sh /opt/haddock2.2/

WORKDIR /data
ENTRYPOINT ["sh", "/opt/haddock2.2/wrapper.sh"]
