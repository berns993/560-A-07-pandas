# https://goheels.com/sports/mens-basketball/roster

'''
roster = [ "Claude", "Brown", "Cadaeu"]
for player in roster:
    print(player)
'''

#Import Pandas as pd and create a DataFrame 
import pandas as pd
roster = [ "Claude", "Brown", "Cadaeu"]
data = pd.DataFrame(roster)
print(data)