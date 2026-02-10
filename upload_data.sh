#!/bin/bash
export PATH=/usr/local/bin:/usr/bin:/bin
/usr/bin/git add .
/usr/bin/git commit -m "upload data at $(date)" 
/usr/bin/git push

