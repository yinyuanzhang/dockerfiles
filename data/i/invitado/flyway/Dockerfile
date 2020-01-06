FROM boxfuse/flyway:5.2.1-alpine

# Add entrypoint script.
COPY ./command /opt/command
RUN chmod 755 /opt/command

ENTRYPOINT []
CMD ["/opt/command"]
