# Use the Bitbucket image
FROM atlassian/default-image:2

# Update and install dependencies
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y libssl-dev 
RUN apt-get install -y openssl

# Make and install openssl
ADD https://www.openssl.org/source/openssl-1.1.1c.tar.gz .
RUN tar xzvf openssl-1.1.1c.tar.gz
RUN cd openssl-1.1.1c && ./config -Wl,--enable-new-dtags,-rpath,'$(LIBRPATH)'
RUN cd openssl-1.1.1c && make && make install
RUN rm /usr/bin/openssl
RUN cd openssl-1.1.1c && ln -s /usr/local/bin/openssl /usr/bin/openssl && ldconfig

# Install boon
ADD https://github.com/camchenry/boon/releases/download/master/boon-master-x86_64-unknown-linux-gnu.tar.gz .
RUN tar -zxvf boon-master-x86_64-unknown-linux-gnu.tar.gz
RUN chmod +x boon/boon
RUN mv boon/boon /usr/local/sbin/

#Download love
RUN boon love download 11.2
ENTRYPOINT [ "boon" ]