FROM backstopjs/backstopjs:4.3.2
RUN whoami
USER root

RUN npm install -g yarn@1.17.3

RUN curl --silent --show-error --location --fail --retry 3 --output /tmp/font.deb http://ftp.us.debian.org/debian/pool/main/f/fonts-noto-color-emoji/fonts-noto-color-emoji_0~20180810-1_all.deb \
      && (sudo dpkg -i /tmp/font.deb || sudo apt-get -fy install)  \
      && rm -rf /tmp/font.deb

RUN mkdir -p ~/.config/fontconfig/conf.d
RUN touch ~/.config/fontconfig/conf.d/noto-color-emoji.conf
COPY ./noto-color-emoji.conf ~/.config/fontconfig/conf.d
RUN wget https://osdn.net/downloads/users/17/17406/NSCJKaR.tar.xz ; wget https://osdn.net/downloads/users/17/17409/fonts.conf ; tar xavf NSCJKaR.tar.xz ; rm NSCJKaR.tar.xz ; mkdir -p ~/.local/share/fonts/ ~/.config/fontconfig/ ; rm -rf ~/.local/share/fonts/NSCJKaR/ ; mv NSCJKaR/ ~/.local/share/fonts/ ; mv fonts.conf ~/.config/fontconfig/
RUN fc-cache -f
