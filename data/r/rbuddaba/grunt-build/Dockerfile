FROM node:5
USER root
# Install Bower & Grunt
RUN npm install -g bower grunt-cli && \
    echo '{ "allow_root": true }' > /root/.bowerrc

RUN apt-get update && apt-get install -y ruby-full && \
	gem install sass

USER root
# Define default command.
CMD ["bash"]
