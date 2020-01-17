# import folium package 
import folium 
  
my_map3 = folium.Map(location = [ 13.845577,100.56959 ], zoom_start = 20) 
  
# Pass a string in popup parameter 
folium.Marker([13.845577,100.56959],  popup = 'ENG KU .').add_to(my_map3) 

my_map3.save(" my_map3.html ") 
