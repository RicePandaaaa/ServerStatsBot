# ServerStatsBot
A simple bot that shows server statistics. Python3 is used as the primary and only coding language, and SQL databases are used for data storage. This is a very primitive bot and I do not intend to be showing off any cool SQL stuff so please don't judge my code too harshly ;-;

The bot currently is planning to store and visualize the following data:
 - Total member count
 - Total member count by role
 - New member count (also by role)
 - Messages per day
 - Messages per hour (graph will show 24h progression)
 
Graphs can be made on demand with .graph {data-type} and will automatically be posted every 24 hours. 

There may be server specific commands, but those will be put in a separate cog and will not be vital to server statistics related functions. As the bot is developed and tested, example graphs will be posted as image files in the Examples folder.
