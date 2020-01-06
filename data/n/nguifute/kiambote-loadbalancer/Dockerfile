FROM nginx:stable
COPY nginx.conf /etc/nginx/conf.d/

COPY fullchain.pem /etc/letsencrypt/live/kiambote.com/fullchain.pem
COPY privkey.pem /etc/letsencrypt/live/kiambote.com/privkey.pem

COPY dannaxfull.pem /etc/letsencrypt/live/dannaxtheprinz.com/dannaxfull.pem
COPY dannaxprivatekey.pem /etc/letsencrypt/live/dannaxtheprinz.com/dannaxprivatekey.pem

COPY kiandacleanfull.pem /etc/letsencrypt/live/kiandaclean.com/kiandacleanfull.pem
COPY kiandacleanprivatekey.pem /etc/letsencrypt/live/kiandaclean.com/kiandacleanprivatekey.pem

COPY chain.pem /etc/letsencrypt/live/kiambote.com/chain.pem
COPY cert.pem /etc/letsencrypt/live/kiambote.com/cert.pem
COPY options-ssl-nginx.conf /etc/letsencrypt/options-ssl-nginx.conf

EXPOSE 80
EXPOSE 443 