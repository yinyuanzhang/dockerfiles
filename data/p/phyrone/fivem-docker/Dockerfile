FROM mono:4.8

MAINTAINER Phyrone

# Allow use of editors like nano/vi/vim
ENV TERM xterm

RUN apt-get -qq update && \

    # install other requirements
    apt-get -qq install nano tzdata

# Set the timezone
RUN echo Europe/Oslo | tee /etc/timezone && dpkg-reconfigure --frontend noninteractive tzdata

# Add needed folders
COPY server /app/fivem-server
COPY resources /app/_resources
RUN mkdir /app/resources

# Switch current working directory
WORKDIR /app/fivem-server

# Expose FiveM port
EXPOSE 30120
EXPOSE 30120/udp

# Entrypoint that merges user mapped
# resource directory with ours on startup.
COPY entry.sh /app/entry.sh
RUN chmod a+x /app/entry.sh
ENTRYPOINT ["/app/entry.sh"]
CMD ["/app/fivem-server/run.sh","+exec","server.cfg"]

# Make info file about this build
RUN printf "Build of wearingstorm/fivem:latest, date: %s\n"  `date -u +"%Y-%m-%dT%H:%M:%SZ"`
