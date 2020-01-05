FROM python:3.7.4

WORKDIR /root
RUN git clone https://github.com/lanmaster53/recon-ng.git
WORKDIR /root/recon-ng
RUN pip install -r REQUIREMENTS

CMD ["./recon-ng"]

# how to use
# docker run -it <IMAGE ID>
#
# Install missing Submodules , since 5.0.0 no submodules are installed
# Example .netcraft, 
# marketplace install netcraft
# modules load netcraft