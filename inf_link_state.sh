#!/bin/bash


INF=$1
PATH_TO_FILE='/tmp/link_state_log.log'

function inf_link_state() {
local interface=$1
echo -e `date` `ip link show ${interface} | grep ${interface}: | awk '{print $2 $9}'`"\n"
}

while true
do
inf_link_state $INF >> $PATH_TO_FILE
sleep 1
done

