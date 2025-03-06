from PIL import Image
import streamlit as st
import requests as r
st.title("WEATHER FORECATING WEDSITE")
a=st.text_input("ENTER THE CITY NAME",value="bhopal")
city_name=a
data= r.get("https://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid=5155aa5828c4a0e920a56376dfeaa65e").json()
p=data["weather"][0]["main"]
q=data["weather"][0]["description"]
r=int(data["main"]["temp"]-273)
s=int(data["main"]["temp_max"]-273)

t=int(data["main"]["temp_min"]-273)
v=int(data["main"]["pressure"])
u=int(data["main"]["humidity"])
w=data["wind"]["speed"]
if st.button("SUBMIT"):
  st.success("SUCCESS")
  img=Image.open("i.png")
  st.image(img,width=400)

  city_name = "YOUR CITY NAME :-"

  st.markdown(f"### :blue[{city_name}] :red[{a}]")

  st.markdown(f"### :blue[{a} CITY WEATHER  IS :-] :red[{p}]")
  st.markdown(f"### :blue[{a} CITY WEATHER IS :- ] :red[{q}]")
  st.markdown(f"### :blue[{a} CITY TEMPETURE IS :-] :red[{r}C]")
  st.markdown(f"### :blue[{a} CITY  MAXIMUM TEMPETURE IS :-] :red[{s}C]")
  st.markdown(f"### :blue[{a} CITY MINIMUM TEMPETURE IS :-] :red[{t}C]")
  st.markdown(f"### :blue[{a} CITY HUMIDITY IS :-] :red[{u}%]")


  st.markdown(f"### :blue[{a} CITY PRESSURE IS :-] :red[{v}]")
  st.markdown(f"### :blue[{a}CITY WIND SPEED :-] :red[{w} KM]")
  

  


