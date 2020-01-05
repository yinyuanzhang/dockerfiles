FROM alpine:latest
MAINTAINER boredazfcuk
ENV SAB3BASE="/SABnzbd3" \
   N2MBASE="/nzbToMedia" \
   BUILDDEPENDENCIES="gcc python3-dev musl-dev libffi-dev py3-setuptools openssl-dev automake autoconf g++ make" \
	APPDEPENDENCIES="git python3 py3-pip tzdata libgomp unrar unzip p7zip ffmpeg" \
   SABPYTHONDEPENDENCIES="cheetah3 cryptography sabyenc" \
	CONFIGDIR="/config" \
	SABREPO="sabnzbd/sabnzbd" \
	PARREPO="Parchive/par2cmdline" \
   N2MREPO="clinton-hall/nzbToMedia"

COPY start-sabnzbd3.sh /usr/local/bin/start-sabnzbd3.sh

RUN echo "$(date '+%d/%m/%Y - %H:%M:%S') | ***** BUILD STARTED *****" && \
echo "$(date '+%d/%m/%Y - %H:%M:%S') | Create directories" && \
   mkdir -p "${SAB3BASE}" "${N2MBASE}" && \
echo "$(date '+%d/%m/%Y - %H:%M:%S') | Install build dependencies" && \
   apk add --no-cache --no-progress --virtual=build-deps ${BUILDDEPENDENCIES} && \
echo "$(date '+%d/%m/%Y - %H:%M:%S') | Install application dependencies" && \
   apk add --no-cache --no-progress ${APPDEPENDENCIES} && \
echo "$(date '+%d/%m/%Y - %H:%M:%S') | Install ${SABREPO}" && \
   git clone -b master "https://github.com/${SABREPO}.git" "${SAB3BASE}" && \
   cd "${SAB3BASE}" && \
   git checkout py3 && \
echo "$(date '+%d/%m/%Y - %H:%M:%S') | Install ${SABREPO} python dependencies" && \
   PYTHONMAJOR="$(python3 --version | grep -Eo '[0-9]{1,3}\.[0-9]{1,3}')" && \
   ln -s "/usr/bin/python${PYTHONMAJOR}" "/usr/bin/python" && \
   pip3 install --no-cache-dir --upgrade pip && \
   pip3 install --no-cache-dir -r requirements.txt && \
   "${SAB3BASE}/tools/make_mo.py" && \
echo "$(date '+%d/%m/%Y - %H:%M:%S') | Install ${PARREPO}" && \
   TEMP="$(mktemp -d)" && \
   git clone -b master "https://github.com/${PARREPO}.git" "${TEMP}" && \
   cd "${TEMP}" && \
   aclocal && \
   automake --add-missing && \
   autoconf && \
   ./configure && \
   make && \
   make check && \
   make install && \
echo "$(date '+%d/%m/%Y - %H:%M:%S') | Clean up" && \
   chmod +x /usr/local/bin/start-sabnzbd3.sh && \
   apk del --no-progress --purge build-deps && \
   rm -rv "/root/.cache/pip" "${TEMP}" && \
echo "$(date '+%d/%m/%Y - %H:%M:%S') | ***** BUILD COMPLETE *****"

HEALTHCHECK --start-period=10s --interval=1m --timeout=10s \
   CMD wget --quiet --tries=1 --spider "http://${HOSTNAME}:8080/sabnzbd" || exit 1

VOLUME "${CONFIGDIR}" "/shared"

CMD /usr/local/bin/start-sabnzbd3.sh