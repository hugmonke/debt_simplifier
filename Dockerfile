# syntax=docker/dockerfile:1

FROM nginx:1.10.1-alpine
COPY src/index.html /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]  