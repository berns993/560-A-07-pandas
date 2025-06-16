# https://goheels.com/sports/mens-basketball/roster

'''
roster = [ "Claude", "Brown", "Cadaeu"]
for player in roster:
    print(player)
'''

#Import Pandas as pd and create a DataFrame 
import pandas as pd

#add Last Name header (changed Dataframe from roster to player)
player = {"Last Name": ["Claude", "Brown", "Cadaeu"],
          "First name": ["Ty", "James", "Elliot"],
          "Height": [79, 82, 74],
          "Weight": [230, 215, 180]}
data = pd.DataFrame(player)

#add bmi column
data["bmi"]= (data["Weight"]/2.205)/((data["Height"]/39.37)**2)

print(data)

data.to_csv("bmi.csv")