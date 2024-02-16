def eto_command(command):
    eto, year_str = command.split()
    year = int(year_str)
    number_of_eto = (year + 8) % 12
    eto_tuple = ("子", "丑", "寅", "卯", "辰", "巳",
                 "午", "未", "申", "酉", "戌", "亥")
    eto_name = eto_tuple[number_of_eto]
    response = f"{year}年は{eto_name}年です。"
    return response
