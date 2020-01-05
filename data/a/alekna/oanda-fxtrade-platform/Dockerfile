FROM alekna/openbox-desktop-vnc

RUN dnf install -y tar unzip java-1.8.0-openjdk; \
    dnf clean all; \
    mkdir /root/Desktop; \
    curl -s -O https://fxtrade.oanda.com/fxgui/www/fxtrade/fxTrade_installer.tar; \
    curl -s -O https://fxtrade.oanda.com/fxgui/www/fxgame/fxTradePractice_installer.tar; \
    tar -xf fxTrade_installer.tar; sh fxTrade_installer.sh; \
    tar -xf fxTradePractice_installer.tar; sh fxTradePractice_installer.sh; \
    rm -f *.tar *.sh *.rpm; \
    sed -i "s/java.*/bash -c '& > \/dev\/null 2>\&1'/" /root/Desktop/*.desktop;
