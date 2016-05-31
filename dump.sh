#!/bin/bash

dump_specific_table(){
        rm -r ./dump/$1
        mongodump --db $1 --out ./dump
        cd dump
        for dir in */
        do
                base=$(basename "$dir")
                if [ "$base" == "$1" ]; then
                        tar -czf "${base}.tar.gz" "$dir"
                fi
        done
}

dump_all(){
        rm -r dump
        mongodump --out ./dump
        cd dump
        for dir in */
        do
                base=$(basename "$dir")
                tar -czf "${base}.tar.gz" "$dir"
        done
}

if [ "$#" -ge 1 ]; then
        dump_specific_table $1

else
        dump_all
fi
