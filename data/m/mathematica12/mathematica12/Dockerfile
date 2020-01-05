FROM cocalc/cocalc

ADD https://github.com/navigaid/mathematica-keygen/releases/download/12/keygen /bin/keygen
ADD ./activate /bin/activate
RUN chmod 755 /bin/activate /bin/keygen

WORKDIR /root
