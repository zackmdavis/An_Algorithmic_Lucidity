Title: Growl
Date: 2014-07-20 21:30
Status: published
Category: psychology
Tags: akrasia, cynicism, Python

Dear reader, imagine you have an idea for a work of prose that you want to have finished by Election Day for reasons which will become clear later, and you're not sure how long it should end up being, but you think maybe around twelve thousand words. When considering what you can do to ensure that this feat will actually be accomplished, it occurs to you that you could start writing now. _Or_—

_Or you could design a script to make desktop notifications about how much more writing you have to do!_ (_Maybe_ you could even put it in a cronjob so that it would nag you to write _automatically_!)

Well, I already made it for you (unless your Linux distribution doesn't use `notify-send` or you're on a Mac or something).

```python
#!/usr/bin/env python3

import argparse
import subprocess
from datetime import datetime

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("filename", help="path to file of draft")
arg_parser.add_argument("goal", type=int, help="goal wordcount")
arg_parser.add_argument("deadline", help="deadline in YYYY-MM-DD format")
args = arg_parser.parse_args()

today = datetime.today()
filename = args.filename
goal = args.goal
deadline = datetime.strptime(args.deadline, "%Y-%m-%d")

def nag_message():
    progress = int(subprocess.check_output(["wc", filename, "-w"]).split()[0])
    to_go = goal - progress
    days_remaining = (deadline - today).days
    to_go_per_day = to_go / days_remaining
    proportion = progress / goal
    return "\n".join(
        "{}: {:.2f}".format(k.replace("_", " "), v) for k, v in locals().items()
    )

subprocess.check_output(["notify-send", "writing progress", nag_message()])
```

[![My Wordcount Notification]({static}/images/wordcount_notification.png)]({static}/images/wordcount_notification.png)

_You're welcome_. Now get back to work.
