FROM python:3.7
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "./my_script.py"]

# ---- Base Node ----
FROM node:alpine AS base
# Copy project file
COPY . .
# Build project
RUN npm run build

FROM nginx
COPY nginx.config /etc/nginx/conf.d/default.conf
COPY --from=base build /usr/share/nginx/html

