FROM nginx:1.19.2-alpine

LABEL maintainer="raulvalverdesanchez@gmail.com"

# Copying custom conf files to proper directory
COPY default.conf /etc/nginx/conf.d/

# Redirecting nginx logs to the standard output
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

# To solve nginx: [emerg] open() "/run/nginx/nginx.pid" failed (2: No such file or directory) described in https://github.com/gliderlabs/docker-alpine/issues/185
RUN mkdir -p /run/nginx

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
