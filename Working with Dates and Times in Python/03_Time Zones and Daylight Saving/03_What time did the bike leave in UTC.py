"""
What time did the bike leave in UTC?
Having set the timezone for the first ten rides that W20529 took, let's see what time the bike left in UTC. We've already loaded the results of the previous exercise into memory.

Instructions
100 XP
Within the for loop, set dt to be the trip['start'] but moved to UTC. Use timezone.utc as a convenient shortcut for UTC."""
# Loop over the trips
for trip in onebike_datetimes[:10]:
  # Pull out the start and set it to UTC
  dt = trip['start'].astimezone(timezone.utc)
  
  # Print the start time in UTC
  print('Original:', trip['start'], '| UTC:', dt.isoformat())