import func_timezones as ft

# print from_cet("17:00")

def test_from_cet():
    correct_cet_arr_20 = ['EST: 15:00', 'PST: 12:00', 'GMT: 19:00']
    correct_cet_arr_8 = ['EST: 3:00', 'PST: 0:00', 'GMT: 7:00']

    cet_arr_20 = ft.from_cet("20:00")
    cet_arr_8 = ft.from_cet("08:00")

    assert cet_arr_20 == correct_cet_arr_20
    assert cet_arr_8 == correct_cet_arr_8

