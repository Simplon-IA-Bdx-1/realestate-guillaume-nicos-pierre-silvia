#!/bin/sh

cat > /app/python/.env <<EOF
MYSQL_HOST=${MYSQL_HOST}
MYSQL_USER=${MYSQL_USER}
MYSQL_PASSWORD=${MYSQL_PASSWORD}
MYSQL_DATABASE=${MYSQL_DATABASE}
EOF

echo "Scheduled tasks:" && crontab -l
echo "starting cron service"
cron
echo "logging scheduled tasks"
tail -f /var/log/cron.log
