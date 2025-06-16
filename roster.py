# https://goheels.com/sports/mens-basketball/roster

'''
roster = [ "Claude", "Brown", "Cadaeu"]
for player in roster:
    print(player)
'''

#Import Pandas as pd and create a DataFrame 
import pandas as pd
roster = [ "Claude", "Brown", "Cadaeu"]
#add Last Name header (changed Dataframe from roster to player)
player = {"Last Name": roster,
          "First name": ["Ty", "James", "Elliot"],
          "Height": [67, 610, 61],
          "Weight": [230, 215, 180]}
data = pd.DataFrame(player)
print(data)