FROM debian:9

CMD apt update
CMD apt install -y wget
CMD wget https://raw.githubusercontent.com/jeedom/core/release/install/install.sh
CMD chmod +x install.sh
CMD sudo ./install.sh

EXPOSE 80 443
