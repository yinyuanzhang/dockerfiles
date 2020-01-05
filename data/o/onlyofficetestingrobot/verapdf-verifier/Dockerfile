FROM ruby:2.6

RUN apt-get -y update && \
    apt-get -y install default-jre-headless \
                       unzip \
                       wget

# Install verapdf
ADD verapdf-auto-install.xml /tmp/verapdf-auto-install.xml
RUN wget http://software.verapdf.org/releases/1.14/verapdf-greenfield-1.14.8-installer.zip -O /tmp/verapdf-installer.zip
RUN unzip /tmp/verapdf-installer.zip -d /tmp/verapdf-installer
RUN java -jar /tmp/verapdf-installer/*/verapdf-izpack-installer-*.jar /tmp/verapdf-auto-install.xml
RUN rm -rf /tmp/verapdf*

COPY . /verapdf_verifier
WORKDIR /verapdf_verifier
RUN bundle install --without development test
CMD ruby verapdf_verifier.rb -p 80 -s Puma -e production
