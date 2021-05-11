#!/bin/bash

(sleep 1; ps | grep "$!" > /dev/null; echo $?) &

ps | grep $!
echo $?

