FROM alpine
RUN apk add aircrack-ng
RUN apk add pciutils
COPY . /src
WORKDIR /src
CMD \
	airodump-ng-oui-update && \
	airmon-ng start wlan1 && \
	airodump-ng wlan1mon -w demo --manufacturer
