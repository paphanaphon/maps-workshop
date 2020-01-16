# import folium package 
import folium 
  
my_map2 = folium.Map(location = [13.845764,100.570189],
                                 zoom_start=20)
# CircleMarker with radius 
folium.CircleMarker(location =[13.845764,100.570189],
                          radius = 50, popup = 'ENG KU. ').add_to(my_map2) 
  
# save as html 
my_map2.save(" my_map2.html ") 


                

