# import folium package 
import folium 
  
my_map4 = folium.Map(location = [13.845577,100.56959], zoom_start = 20) 
  
folium.Marker([13.845577,100.56959], popup = 'KU ENG').add_to(my_map4) 
  
folium.Marker([13.848796,100.56706], popup = 'newbar').add_to(my_map4) 
  
# Add a line to the map by using line method . 
# it connect both coordiates by the line 
# line_opacity implies intensity of the line 
  
folium.PolyLine(locations = [(13.845577,100.56959), (13.848796,100.56706)], line_opacity = 0.5).add_to(my_map4) 
  
my_map4.save("my_map4.html") 
