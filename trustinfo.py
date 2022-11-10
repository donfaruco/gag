"""Gag script to provide trust reference to a friend."""

import os

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

print("Name:" + trust[0])

print("contact:" + trust[1])
print("address:" + trust[2])
print(trust[3] +", " + trust[4])
