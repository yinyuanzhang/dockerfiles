FROM homeassistant/home-assistant:0.84.6

# Install tshark & iw
RUN apt update -qq
RUN DEBIAN_FRONTEND=noninteractive apt-get install -yq --force-yes iw tshark
