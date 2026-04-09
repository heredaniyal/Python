distance_mi = 0 # minimum distance
is_raining=True # values of boolean in Capital letter (learning)
has_bike=True # the user has a bike or not
has_car=True 
has_ride_share_app=True

# conditional statements in action
# elif meaning else if
if distance_mi==False:
    print("False")
elif  distance_mi <=1:
    if not is_raining:
        print("True")
    else:
        print("False")
elif distance_mi > 1 and distance_mi <= 6:
    if has_bike and not is_raining:
        print("True")
    else:
        print("False")
elif distance_mi > 6:
    if has_car or has_ride_share_app:
        print("True")
    else:
        print("False")            
            


# ** end of main.py **

