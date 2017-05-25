def from_est(time):
    time_arr = []
    cet = 5
    pst = 3
    gmt = 4

    hour = int(time[0:2])
    cet_hour = hour + cet
    pst_hour = hour - pst
    gmt_hour = hour + gmt

    if cet_hour > 24:
        cet_hour -= 24
        cet_hour = "0" + str(cet_hour)
    if pst_hour < 0:
        pst_hour += 24
    if gmt_hour > 24:
        gmt_hour -= 24
        gmt_hour = "0" + str(gmt_hour)

    time_arr.append("CET: " + str(cet_hour) + ":" + time[3:5])
    time_arr.append("PST: " + str(pst_hour) + ":" + time[3:5])
    time_arr.append("GMT: " + str(gmt_hour) + ":" + time[3:5])

    return time_arr

def from_cet(time): # => [est, pst]
    time_arr = []
    est = 5
    pst = 8
    gmt = 1

    hour = int(time[0:2])
    est_hour = hour - est
    pst_hour = hour - pst
    gmt_hour = hour - gmt

    if est_hour < 0:
        est_hour += 24
    if pst_hour < 0:
        pst_hour += 24
    if gmt_hour < 0:
        gmt_hour += 24

    time_arr.append("EST: " + str(est_hour) + ":" + time[3:5])
    time_arr.append("PST: " + str(pst_hour) + ":" + time[3:5])
    time_arr.append("GMT: " + str(gmt_hour) + ":" + time[3:5])

    return time_arr

def timezones():
    time = raw_input("enter time (eg: 3:00, 14:00): ")
    zone = raw_input("enter timezone (GMT, EST, PST, or CET only): ")
    zone.lower()

    if len(time) < 5:
        time = "0" + time

    if zone == "est":
        time = from_est(time)
    # elif zone == "gmt":
    #     time = from_gmt(time)
    # elif zone == "pst":
    #     time = from_pst(time)
    elif zone == "cet":
        time = from_cet(time)

    for t in time:
        print t

def main():
    timezones()

main()
