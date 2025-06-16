# https://goheels.com/sports/mens-basketball/roster

'''
roster = [ "Claude", "Brown", "Cadaeu"]
for player in roster:
    print(player)
'''

#Import Pandas as pd and create a DataFrame 
import pandas as pd

#add Last Name header (changed Dataframe from roster to player)
player = {"Last Name": ["Claude", "Brown", "Cadaeu", "Davis", "Tyson", "Davis", "Trimble", "Powell", "Jackson", "Washington"],
          "First name": ["Ty", "James", "Elliot", "RJ", "Cade", "Elijah", "Seth", "Drake", "Ian", "Jalen"],
          "Height": [79, 82, 74, 72, 77, 75, 75, 78, 76, 82],
          "Weight": [230, 215, 180, 180, 200, 215, 195, 195, 190, 235]}
data = pd.DataFrame(player)

#add bmi column
data["bmi"]= (data["Weight"]/2.205)/((data["Height"]/39.37)**2)

# Round the bmi column to 2 decimal points
data["bmi"] = data["bmi"].round(2)

print(data)

data.to_csv("bmi.csv")