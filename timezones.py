import func_timezones as ft

def timezones():
    time = raw_input("enter time (eg: 3:00, 14:00): ")
    zone = raw_input("enter timezone (GMT, EST, PST, or CET only): ")
    zone.lower()

    if len(time) < 5:
        time = "0" + time

    if zone == "est":
        time = ft.from_est(time)
    # elif zone == "gmt":
    #     time = from_gmt(time)
    # elif zone == "pst":
    #     time = from_pst(time)
    elif zone == "cet":
        time = ft.from_cet(time)

    for t in time:
        print t

def main():
    timezones()

main()
