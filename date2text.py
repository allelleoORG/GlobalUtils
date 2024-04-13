def date2text(date: str = "31.01.2023"):
    return (
        date.split(".")[0]
        + " "
        + [
            "Января",
            "Февраля",
            "Марта",
            "Апреля",
            "Мая",
            "Июня",
            "Июля",
            "Августа",
            "Сентября",
            "Октября",
            "Ноября",
            "Декабря",
        ][int(date.split(".")[1]) - 1]
        + " "
        + date.split(".")[2]
    ).lower()


if __name__ == "__main__":
    print(date2text())
