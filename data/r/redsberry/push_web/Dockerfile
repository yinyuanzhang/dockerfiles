# --------------------------------------------
# Eberry redsBerry PUSH solution TEST DRIVE
# 
# 2019.04.25
# --------------------------------------------
FROM nginx:1.15.12

# copy run module
RUN mv /usr/share/nginx/html/index.html /usr/share/nginx/html/index.html.bak
ADD ./dist/src.tar /usr/share/nginx/html/
