FROM node:10
RUN apt update && npm config set unsafe-perm true && apt install -y netcat zip && npm install -g lerna @babel/core
RUN git clone https://github.com/nasa/cumulus && cd cumulus && npm run bootstrap-no-build \
  && (find ./packages -maxdepth 2 -name node_modules && find ./tasks -maxdepth 2 -name node_modules && echo "./node_modules"  && echo "./example/node_modules/") | zip -ry /bootstrapped_deps.zip -@ && rm -Rf *
