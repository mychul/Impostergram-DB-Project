#!/bin/bash
folder=/home/team2/Documents/CS179g/project
PGDATA=$folder/data
PGSOCKETS=$folder/sockets
export PGDATA
export PGSOCKETS

#Initialize folders
rm -fr $PGSOCKETS
mkdir -p $PGSOCKETS

rm -fr $PGDATA
mkdir -p $PGDATA

#Initialize DB
initdb

#Start folder
pg_ctl -o "-c unix_socket_directories=$PGSOCKETS" -D $PGDATA -l $folder/logfile start
