import os
import glob
import pandas as pd
import  plotly.express as px
import calendar



Data_file_path = r"C:\Users\Mary\FINAL PROJECT\World Data Fires"

file_list = glob.glob(Data_file_path + "/*.csv")

usecols = ["latitude", "longitude", "brightness", "acq_date"]


list_df = []
for file in file_list[:]:
    in_df = pd.read_csv(file, usecols = usecols)
    in_df.insert(0, "Country", [os.path.split(file)[-1].split("_")[-1].replace(".csv", "")] * len(in_df.index), True)
    list_df.append(in_df)
    
df = pd.concat(list_df)

# user_input = input ("Give any date and month in 2023 ?")
# created user input for the day month and year 
year = input ("enter year between 2020-2023: ")

valid_years = ["2020", "2021", "2022", "2023"]
while year not in valid_years:
    print(f"the value {year} is not a valid year")
    year = input ("enter year between 2020-2023: ")


month = input ("enter month between 1-12: ")
while int(month) not in range (1,13):
    print(f"the value {month} is not a valid month")
    month = input ("enter month between 1,12: ")

month = month.zfill(2)

last_day = calendar.monthrange(int(year), int(month))[1]
day = input (f"enter day between 1, {last_day}: ")

while int(day) not in range (1,last_day + 1):
    print(f"the value {day} is not a valid day")
    day = input (f"enter day between 1, {last_day}: ")


day = day.zfill(2)


tgt_date = f"{year}-{month}-{day}"


df = df[df.acq_date == tgt_date ]  
# visualize panda DataFrame using px. scatter-geo
fig = px.scatter_geo(df, lon=df.longitude, lat=df.latitude, color = df.brightness, hover_data=["Country", "longitude", "latitude", "brightness"])

hover_template = "<br>".join([
        "Country: %{customdata[0]}",
        "Lon: %{customdata[1]}",
        "Lat: %{customdata[2]}",
        "Brightness: %{customdata[3]}",
    ])

fig.update_traces(hovertemplate = hover_template)

fig.update_layout(

    title_text= f'Global Fires - {tgt_date}', 
    title_font_color = "red", 
    title_font_size = 40,
    font_weight = "bold",
    font_color = "green",
    title_x  = 0.5, 
    font_size = 20
)

fig.show()


