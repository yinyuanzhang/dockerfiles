FROM piperbuilder/raspbian-nodejs
ARG SOURCE_COMMIT

# invoke QEMU binaries for shell calls
RUN [ "cross-build-start" ]

WORKDIR /usr/local/games/pipercode

# Copy files
COPY . ./

# Build
ENV NPM_CONFIG_PREFIX "~/.npm-global"
RUN npm install
RUN npm rebuild node-sass
RUN npm run build

# Electron install
WORKDIR /usr/local/games/release
RUN npm install

COPY pipercode.desktop ./

# Generate version hash
RUN echo "$SOURCE_COMMIT" > version.hash

WORKDIR /usr/local/games/pipercode

# end shell calls via QEMU binaries
RUN [ "cross-build-end" ]

CMD ["bash"]
