FROM abc3660170/nodemapnik:latest
RUN yum install zip -y
WORKDIR /home/fonts/noto
RUN wget https://noto-website-2.storage.googleapis.com/pkgs/Noto-unhinted.zip
RUN mkdir -p /usr/share/fonts/opentype/noto
RUN unzip -d /usr/share/fonts/opentype/noto Noto-unhinted.zip
RUN mkdir -p /usr/share/fonts/opentype/unifont
RUN wget http://unifoundry.com/pub/unifont/unifont-11.0.03/font-builds/unifont-11.0.03.ttf -P /usr/share/fonts/opentype/unifont/
RUN wget http://unifoundry.com/pub/unifont/unifont-11.0.03/font-builds/unifont_upper-11.0.03.ttf -P /usr/share/fonts/opentype/unifont/
RUN fc-cache -f -v
WORKDIR /home
RUN rm -rf /home/fonts