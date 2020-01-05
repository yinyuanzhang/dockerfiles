FROM diko316/alnode:v2.3

ADD https://raw.githubusercontent.com/diko316/alnode-webtest/master/bin/xvfb-run.sh /opt/tools/webtest/xvfb-run.sh

RUN auto-build \
        --no-builer \
		--apk-permanent \
            coreutils \
            udev \
            xvfb \
            dbus \
            fontconfig \
            ttf-freefont \
            firefox-esr \
            mesa-gl && \
    chmod +x /opt/tools/webtest/xvfb-run.sh && \
    ln -s /opt/tools/webtest/xvfb-run.sh /usr/local/bin/xvfb-run
