def check_speed(speed):
    if (speed<70):
        print('70')
    elif speed>70:
        exceeded_speed=speed-70
        print("exceeded speed is ",exceeded_speed)
    points_accumulated=0
    i=0
    while i<=exceeded_speed:
        if i!=0 and i%5==0:
            points_accumulated+=1
        i=i+1
        if points_accumulated>12:
            print("license suspended")
    print('total points accumulated',points_accumulated)

check_speed(90)