#
# Grunt runtime Dockerfile
#
# https://github.com/sameronline/grunt-runtime
#

# Pull base image.
FROM library/node
MAINTAINER Samer Ali (samer@sameronline.com)

# Install Bower & Grunt
RUN npm install -g grunt-cli

# Set instructions on build.
ONBUILD ADD package.json /app
ONBUILD RUN npm install

# Define default command.
CMD ["grunt", "watch"]

# Expose default livereload port
EXPOSE 35729