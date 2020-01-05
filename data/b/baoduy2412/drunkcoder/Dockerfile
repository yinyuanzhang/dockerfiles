FROM  codercom/code-server

# update the repository sources list and install dependencies
RUN sudo apt-get update -yq
RUN sudo apt-get upgrade -yq && \
  sudo apt-get install -yq curl git nano

# Install Node
RUN curl -sL https://deb.nodesource.com/setup_11.x | sudo bash - && sudo apt-get install -yq nodejs
RUN sudo apt-get install gcc g++ make -yq

#install npm
RUN sudo apt-get install aptitude -yq
RUN sudo aptitude install npm -yq

# install Chrome
# follow the guideline here https://askubuntu.com/questions/220960/cannot-install-google-chrome-how-do-i-fix-it/250625#250625?newreg=d98caf6cc1544ef6a1ead88c0ac98b4c
RUN cd /tmp &&\
  sudo wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb &&\
  sudo dpkg -i google-chrome-stable_current_amd64.deb;\
  sudo apt-get install -f -yq

# confirm installation
RUN node -v
RUN npm -v

ENTRYPOINT ["code-server"]
