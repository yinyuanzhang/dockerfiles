FROM azelinskyy/mo2-backend-develop

MAINTAINER Andriy Zelinskyy <andriy.zelinskyy@gmail.com>

# Create release structure
RUN cp -r  /usr/src/build/dist/* /usr/src/ \
	&& rm -rf /usr/src/build  \
	&& rm -rf /usr/src/tests 

WORKDIR /usr/src/

# Install release dependencies
RUN npm install

#expose application port
EXPOSE 8000

ENTRYPOINT ["node"]
CMD ["app/index.js"]
