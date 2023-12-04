# AoC parser for a private leaderboard

# Fetch updated JSON file
# Parse JSON

# Create list of days sorted by daily points
# Create list of times from part 1 to part 2
# Create list of total points
# Create data for graphs

import fetch
import json

data = fetch.get()

print(json.dumps(data, indent=4))