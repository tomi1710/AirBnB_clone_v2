#!/usr/bin/env bash
# Sets up my web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx
mkdir -p /data/web_static/releases/test /data/web_static/shared
echo -e "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "38i\ location /hbnb_static/ {\n\talias /data/web_static/current/;\n}" /etc/nginx/sites-available/default
sudo service nginx restart
exit 0
