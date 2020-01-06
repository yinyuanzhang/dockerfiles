ARG BUNPUN=i3thuan5/taigi_bunpun

FROM ${BUNPUN} AS kiatko

RUN python manage.py startapp app
RUN mkdir -p app/management/commands/
RUN touch app/management/commands/__init__.py
RUN echo 'INSTALLED_APPS+=("app",)' >> hok8_bu7/settings.py

RUN pip install kau3-tian2-iong7-ji7

COPY 產生語句.py app/management/commands/
RUN python manage.py 產生語句
COPY 產生語言模型.py app/management/commands/
RUN python manage.py 產生語言模型
COPY 產生辭典.py ./
RUN python 產生辭典.py < ku.txt > su-tshoophue.txt
COPY bua̋i-liân.txt ./
RUN cat bua̋i-liân.txt | sed 's/./&-/g' | sed 's/-$//g' > bua̋i-han.txt
RUN cat su-tshoophue.txt | \
  grep -v '^..*的｜' | \
  grep -v '^予-' | \
  grep -v '\-無｜' | \
  grep -v 無法度匯入標點 | \
  grep -v -f bua̋i-han.txt | \
  cat > su.txt

FROM i3thuan5/hok8-bu7
COPY --from=kiatko \
  /usr/local/hok8-bu7/語言模型資料夾/語言模型.lm \
  /usr/local/hok8-bu7/su.txt \
  /usr/local/hok8-bu7/ku.txt \
  /usr/local/hok8-bu7/

