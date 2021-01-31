import shutil 

path = "/Users/Uporabnik/Desktop/FTP-Vene"

statistika = shutil.disk_usage(path) 
  
print("Informacije porabe diska:") 
print(statistika) 
