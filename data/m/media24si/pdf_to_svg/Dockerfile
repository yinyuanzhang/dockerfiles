# Pull a minimal Alpine Linux master image
FROM alpine:latest

# Install dependencies
RUN apk --no-cache add \
    bash \
    inkscape \
    sed \
    ttf-dejavu \
    python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    pip3 install scour && \
    adduser -D inkscape

# Set home
ENV HOME /home/inkscape
VOLUME $HOME/workspace
WORKDIR $HOME/workspace

# Add the conversion script
ADD ./pdf_to_svg.sh /home/inkscape/
RUN chmod a+x /home/inkscape/pdf_to_svg.sh

# Add user
USER inkscape

# Expose the command
ENTRYPOINT [ "/home/inkscape/pdf_to_svg.sh" ]
