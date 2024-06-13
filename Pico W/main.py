from remote import Remote

remote = Remote()

while True:    
    remote.update_cords()
    remote.update_data_display()
    print("x: " + str(remote.x) + " y: " + str(remote.y))