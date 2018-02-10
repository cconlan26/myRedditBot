# myRedditBot
Finds a recipe given a list of ingredients.
Responds to comments beginning with 'Find me a recipe with ' followed by a list of ingredients.
e.g.

"Find me a recipe with chicken and potato"



cron tab examples:
https://www.thegeekstuff.com/2009/06/15-practical-crontab-examples/

Running process indefinitely on pythonanywhere
https://www.pythonanywhere.com/

crontab -e

(minute, hour, day of month, month, day of week)
* * * * *  ./main.py

Command for finding Session ID from CRON task
ps -o pid,sess,cmd afx | egrep "( |/)cron( -f)?$"

then:
pkill -s sessionID
