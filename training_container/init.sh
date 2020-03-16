#!/bin/sh

echo "Scheduled tasks:" && crontab -l
echo "starting cron service"
cron
echo "logging scheduled tasks"
tail -f /var/log/cron.log
