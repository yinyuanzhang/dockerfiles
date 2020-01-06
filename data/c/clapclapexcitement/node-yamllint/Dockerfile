FROM node

COPY sample.yml /sample.yml

RUN npm install --global yaml-lint && \
  yamllint /sample.yml && \
  rm /sample.yml
