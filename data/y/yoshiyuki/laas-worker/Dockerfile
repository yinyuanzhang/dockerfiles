FROM yoshiyuki/node-chromium

ADD services/worker/app /app
ADD protos /protos
ENV PROTO_DIRPATH /protos
WORKDIR /app
RUN npm install --production
ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD true
ENV CHROME_BIN /usr/bin/chromium-browser
RUN npm install puppeteer@1.4.0
RUN addgroup -S pptruser && adduser -S -g pptruser pptruser \
    && mkdir -p /home/pptruser/Downloads \
    && chown -R pptruser:pptruser /home/pptruser \
    && chown -R pptruser:pptruser /app
USER pptruser
CMD ["npm", "start"]