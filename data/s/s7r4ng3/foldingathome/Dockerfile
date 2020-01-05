FROM ubuntu

# If you set USERNAME to Anonymous, the folding@home client pauses for 5 minutes, but will then begin processing data.
ENV USERNAME S7R4nG3
ENV TEAM 235221
ENV POWER medium

# Install updates
RUN apt-get update -y
RUN apt-get install -y wget python

# Install Folding@home
RUN wget https://download.foldingathome.org/releases/public/release/fahclient/debian-testing-64bit/v7.4/fahclient_7.4.4_amd64.deb
RUN wget https://download.foldingathome.org/releases/public/release/fahcontrol/debian-testing-64bit/v7.4/fahcontrol_7.4.4-1_all.deb
ADD config.xml /etc/fahclient/
RUN sed -i -e "s/{{USERNAME}}/$USERNAME/;s/{{TEAM}}/$TEAM/;s/{{POWER}}/$POWER/" /etc/fahclient/config.xml
RUN dpkg -i --force-depends fahclient_7.4.4_amd64.deb
RUN dpkg -i --force-depends fahcontrol_7.4.4-1_all.deb

CMD /etc/init.d/FAHClient start && tail -f /var/lib/fahclient/log.txt
