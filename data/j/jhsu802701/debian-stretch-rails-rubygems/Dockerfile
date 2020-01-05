FROM rubyonracetracks/debian-stretch-dev
MAINTAINER Jason Hsu

COPY usr_local_bin/* /usr/local/bin/

# sync: needed to avoid "text file busy" error
RUN sudo chmod +x /usr/local/bin/*; sync; sudo /usr/local/bin/rails-rubygems-root;

USER winner

WORKDIR /home/winner
