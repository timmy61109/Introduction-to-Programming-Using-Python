"""Yout life in weeks."""

OLD_YEAR = 20
OLD_WEEK = 26

for week in range(0, 53):
    if week < 1:
        WEEK_STR = "|" + format('|', ">33s")
    else:
        WEEK_STR += format(week, "32d") + "|"

print(WEEK_STR)

for week in range(0, 53):
    if week < 1:
        WEEK_STR = "|" + format(':---:|', ">33s")
    else:
        WEEK_STR += format(':---:|', ">33s")

print(WEEK_STR)
WEEK_STR = ""

for year in range(1, 101):
    for week in range(0, 53):
        if week < 1:
            WEEK_STR += "|" + format(year, "33d") + '|'
        else:
            if OLD_YEAR > year:
                WEEK_STR += format('<font color="#FF0000">■</font> |', ">32s")
            elif OLD_YEAR == year:
                if OLD_WEEK >= week:
                    WEEK_STR += format(
                        '<font color="#FF0000">■</font> |', ">32s")
                else:
                    WEEK_STR += format('□|', ">33s")
            else:
                WEEK_STR += format('□|', ">33s")
    WEEK_STR += '\n'

print(WEEK_STR)
