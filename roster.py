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
player = {"Last Name": roster}
data = pd.DataFrame(player)
print(data)