# HTTPS-Scan Docker image to scan/crawl a given URL for insecure dependencies
#
# based upon:
#   - phantomjs
#   - https-scan (https://github.com/zordius/https-scan)
#
# building:
#   docker build -t https-scan .
#
# running:
#   docker run -itd -v $(pwd):/data --name https-scan https-scan
#
# using (through shell):
#   docker exec -it https-scan /bin/bash
#
# using directly
#   docker exec -it https-scan https-scan --verbose https://www.url.com
#
# running wiht file input directly
#   docker exec -it https-scan https-scan --verbose --file file.txt

FROM ubuntu

# Install LXDE and VNC server.
RUN \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get install -y screen nodejs npm libfreetype6 libfontconfig1 && \
  rm -rf /var/lib/apt/lists/*

RUN ln /usr/bin/nodejs /usr/bin/node
RUN npm install -g https-scan

RUN cp -R /usr/local/lib/node_modules/https-scan/node_modules/phantomjs /usr/local/share/phantomjs
RUN ln -sf /usr/local/lib/node_modules/https-scan/node_modules/phantomjs/bin/phantomjs /usr/local/bin

RUN export PATH="$HOME/opt/bin:$PATH"

# Define working directory.
WORKDIR /data

# Define default command.
CMD ["/bin/bash"]
