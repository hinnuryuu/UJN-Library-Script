from libapi import *
from libapi.utils import *

username = "username"
password = "password"
p = libapi(username, password)
library_information = p.filters()
for room_num in range(41):
    room_id = library_information['data']['rooms'][room_num][0]
    limitation = limit_seat_number(room_id)
    for seat_num in range(int(limitation[0]), int(limitation[1]) + 1):
        with open("seat_id_database.csv", "a", encoding="utf-8-sig") as f:
            data = "{},{},{},{},{},{}\n" \
                .format(library_information['data']['rooms'][room_num][1],
                        "东校区" if library_information['data']['rooms'][room_num][2] == 1 else "西校区",
                        library_information['data']['rooms'][room_num][3],
                        seat_num, room_id,
                        p.getSeatIDbyNum(str(room_id), str(seat_num))
                        )
            f.write(data)
