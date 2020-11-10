#!/bin/bash
folder=/home/team2/Documents/CS179g/project
PGDATA=$folder/data
PGSOCKETS=$folder/sockets
export PGDATA
export PGSOCKETS

#root=$(realpath $(dirname "$0"))
#echo $root
#root=$(dirname $root)
#echo $root
dbname=impostergram_db
echo "creating db named ... $dbname"
createdb -h localhost $dbname
pg_ctl status

echo "Copying csv files ... "
sleep 1
cp /home/team2/Documents/CS179g/Backup/*.csv $folder/data/

echo "Initializing tables .. "
psql -h localhost $dbname < $folder/sql/create.sql
