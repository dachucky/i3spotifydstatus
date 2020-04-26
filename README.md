# i3spotifystatus

![screen](https://raw.githubusercontent.com/pradzio1/i3spotifystatus/master/res/scr.png)

### About:
The original author [@rpieja](https://github.com/rpieja) had this in mind when he first made this bit of code
> i3 status isn't particularly the best status generator for i3bar in terms of customization. But it's my favourite, because it works, it's easy to use, and it's bundled with i3wm so I don't have to think about installing it. Feature that lack I've been missing the most that wasn't built into i3status was notifying about author and title of currently played song in spotify client. I have found some gists written by [@csssuf](https://github.com/csssuf), and they work well, but due to format of data outputed by i3status all of the information about colors of text was lost and i3bar was showing only monochromatic text.
> i3spotifystatus is a tiny python script that parses JSON outputted by i3status, adds information about song author and title and outputs it to i3bar.

Personally I was looking for a simple solution to show the currently playing track on a dashboard I have been building at home that uses i3. After settling on spotifyd as the player, this seemed to be the best option for showing what's playing.



### What you'll need:
* DBus
* playerctl >= 2.0.1
* [spotifyd](https://github.com/Spotifyd/spotifyd)
* You'll need FontAwesome if you want to display the Spotify logo on the bar.

### How to install:

* clone repository to your prefered location
* in your i3 config file (usually placed in ~/.config/i3/) set `status_command` to `i3status | /path/to/your/pystatus.py` in `bar` section, like this:
```
bar {
    status_command i3status | ~/Documents/GitHub/i3spotifystatus/pystatus.py
}
```
If you are using i3-gaps, it will probably contain the `status_command i3status` already. You just have to add the pipe and the python script path after. 

* in `i3status.conf` file (create one if you don't have any -> read i3status doc for more information) set `output_format = "i3bar"` inside the 'general' configuration, like this:
```
general {
    ...
    output_format = "i3bar"
    ...
}
```

* Reload i3 configs (usually `Mod + Shift + R`, if you haven't changed it).

Tip: If you are not sure how this whole thing works, you can comment your config files using `#` at the beginning of each line. This way it is easy to revert the changes.

### Credits:
Script is based on sample wrapper committed to original i3status repository.

Original code forked from [@junglerobba](https://github.com/junglerobba) who forked it from [@rpieja](https://github.com/rpieja)
