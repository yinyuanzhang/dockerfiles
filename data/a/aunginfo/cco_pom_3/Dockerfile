FROM ubuntu:latest

RUN apt-get update \
 && apt-get -y -q install python3-pip unzip wget

RUN pip3 install -U pip

COPY requirements.txt /tmp/requirements.txt

RUN  pip3 install -r /tmp/requirements.txt

RUN wget –no-verbose https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

RUN dpkg -–assume-yes install google-chrome-stable_current_amd64.deb; apt-get –fix-broken

RUN CHROMEDRIVER_VERSION=`wget --no-verbose --output-document - https://chromedriver.storage.googleapis.com/LATEST_RELEASE`\
 && wget --no-verbose --output-document /tmp/chromedriver_linux64.zip http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip \
 && unzip -qq /tmp/chromedriver_linux64.zip -d /opt/chromedriver \ 
 && chmod +x /opt/chromedriver/chromedriver \
 && ln -fs /opt/chromedriver/chromedriver /usr/local/bin/chromedriver
    
ENTRYPOINT [‘/run_tests.sh’]

#image creation
RUN docker build -t cco_pom_3:latest bash
#container creation
RUN docker run --name="test_container3" -d -t cco_pom_3
#conntainer run
RUN docker exec -it test_container3 bash -c './run_tests.sh’

RUN docker cp C:\Users\aung\Documents\TC_Results_from_jenkins test_container3:./app/results 
