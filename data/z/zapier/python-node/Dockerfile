FROM zapier/python:2019.12.13

# Node.js

RUN apt-get update && \
apt-get install -yq --no-install-recommends \
curl gnupg && \
curl -sL https://deb.nodesource.com/setup_10.x | bash - && \
apt-get install -y nodejs && \
node --version

# Yarn

RUN npm install --global yarn && \
yarn --version

# direnv

RUN apt-get update && \
apt-get install -yq --no-install-recommends \
direnv && \
direnv version

# Validation

COPY verchew.ini /opt/
RUN pip install verchew
CMD verchew --root=/opt/ --exit-code
