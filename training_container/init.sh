#!/bin/sh

echo "starting cron service"
cron

echo "logging"
tail -f /var/log/cron.log
