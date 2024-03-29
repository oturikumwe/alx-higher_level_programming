#!/bin/bash

# Script to list all databases on MySQL server

# Prompt for MySQL root password
read -s -p "Enter MySQL root password: " mysql_pass
echo ""

# MySQL command to list databases
mysql -uroot -p$mysql_pass -e "/* List all databases */ SHOW DATABASES;"
