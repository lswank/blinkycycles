# Blinky Cycles 0.3.0

Blinky Cycles by Lorenzo Swank (GitHub.com/LSwank)

An xBar Plugin.

# Introduction

This is a small plugin for xBar which acts as a "Tomato" style timer. Beginning at midnight, ten minutes of planning and thirty minutes of work are repeated over and over.

# Usage

Place in your xBar plugin directory. Plug in your blink(1) device. You'll get some calming visual cues telling the people around you "I'm working, don't interact with me". If you use Yabai as a window manager, it will also make your window frame colors blink.

# Caveats

This is meant to work with the blink(1) LED device and yabai on macOS. If you do not have the blink(1) drivers installed in the same Python environment, it will fail horrifically. If you do not have yabai installed, it will be just fine.

# License

[Insert appropriate Open Source with Attribution license here.]

# (In)frequently Asked Questions

## Can I change the amount of time for each cycle?

It's open source. You can do anything you want.

## It's crashing because of blink1 or something missing.

It's open source. Feel free to remove those bits.

## It's crashing for a non blink1 related reason.

Post an issue and someone will perhaps get around to working on it. Or pull up a chair and start coding on it with me.

# Support

There is no support. GitHub issues may or may not get answered. This is just a fun personal project, and I am open sourcing it in case anyone else feels like it would be useful for them. That, and I can blog about it and share it. I've already infected two or three friends who find this to be useful in social "working" cafe visits. Maybe you will, too.