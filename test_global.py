import time
# import os
# import sys

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import functions.est_date as est_date
import functions.wknd_upcom as wknd_upcom

test = True
hints_enabled = False

def multi_time(test, hints_enabled):
    meta_date = est_date.get_now(test, hints_enabled)
    time_ref = []
    for i in range(1000000):
        time_start_a = time.time()
        # d3wknd_start, d3wknd_end = wknd_upcom.main(test, hints_enabled, meta_date[1])
        d3wknd_start, d3wknd_end = wknd_upcom.main(test, hints_enabled, meta_date[1])
        time_end_a = time.time()
        time_ref.append((time_end_a-time_start_a))

    time_cal = []
    for i in range(1000000):
        time_start_b = time.time()
        d3wknd_start, d3wknd_end = wknd_upcom.main_b(test, hints_enabled)
        time_end_b = time.time()
        time_cal.append((time_end_b-time_start_b))

    time_ref_calc = 0
    for i in range(len(time_ref)):
        time_ref_calc += time_ref[i]
    print(f"average time elapsed for referenced time: {time_ref_calc/len(time_cal)}")

    time_cal_calc = 0
    for i in range(len(time_cal)):
        time_cal_calc += time_cal[i]
    print(f"average time elapsed for calling time: {time_cal_calc/len(time_cal)}")

multi_time(test, hints_enabled)