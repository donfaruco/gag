"""Gag script to provide trust reference to a friend."""

def mytrust(city):
    office = "Law offices of Savin & Bursk"
    phone = "818-368-8646"
    address = "10663 Yarmouth Ave"
    zip = "91344"

    if city != "Granada Hills":
        return "incorrect city, please enter Granada Hills"
    else:
        return office, phone, address, city, zip

trust = mytrust("Granada Hills")

print(trust)
