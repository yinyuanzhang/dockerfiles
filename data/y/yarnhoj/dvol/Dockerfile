FROM debian:jessie

#Install git to clone repos
RUN apt-get update && apt-get install -y\
    git\
    && apt-get clean

#Create my user
RUN useradd jray

#Install my config files (denv) github repo
RUN git clone https://github.com/YarNhoj/dvol.git /home/jray 

#Setup my ENV
ENV PATH /home/jray/scripts:$PATH

#Create shared Volumes
VOLUME /home/jray

RUN chown -R jray: /home/jray

CMD ["echo", "Volume Container Started"]
