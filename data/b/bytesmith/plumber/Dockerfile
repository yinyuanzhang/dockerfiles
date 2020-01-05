FROM bytesmith/rclient:3.4.3
LABEL maintainer="info@bytesmith.de"

# install plumber
RUN Revo64 -e 'install.packages(c("plumber"))' --no-save

EXPOSE 8000
ENTRYPOINT ["Revo64", "-e", "pr <- plumber::plumb(commandArgs()[4]); pr$run(host='0.0.0.0', port=8000)"]
CMD ["/opt/microsoft/rclient/3.4.3/libraries/RServer/plumber/examples/10-welcome/plumber.R"]
