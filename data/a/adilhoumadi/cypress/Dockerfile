FROM cypress/browsers:chrome69
RUN npm install --save-dev cypress
RUN npm install --save-dev chance
RUN npm install --save-dev serve
RUN npm install --save-dev cypress-testing-library
RUN apt-get update
RUN apt-get install unzip python-pip libpython-dev groff -y
RUN pip install --upgrade pip
RUN pip install awscli --upgrade
