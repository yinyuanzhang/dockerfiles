FROM flexberry/mono-ember as backend

ENV PROJECT=EmberFlexberry

ARG TAG=1.0.0-beta09-backend

RUN	git clone --depth=50 --branch=$TAG https://github.com/Flexberry/FlexberryEmberTestStand.ODataBackend.git /backend-src && \
	cd /backend-src/$PROJECT ; \
	nuget restore $PROJECT.sln ; \
	msbuild /p:Configuration=Release $PROJECT.sln

FROM flexberry/alt.p8-apache2-mono:latest

RUN	rm -r /var/www/vhosts/test

COPY --from=backend /backend-src/EmberFlexberry/ODataBackend /var/www/vhosts/test
COPY vhosts.conf /conf

