from remote import Remote

#Create the remote object
remote = Remote()

#on loop update the data then display on screen and send data on serial
while True:    
    remote.update_cords()
    remote.update_data_display()
    print("x: " + str(remote.x) + " y: " + str(remote.y))