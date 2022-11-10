"""Gag script to provide trust reference to a friend."""

import webbrowser
import sys


city = sys.argv[1]
url = "https://savinbursklaw.com/"
directions = "https://www.google.com/maps/dir/Woodley+Ave+%26+Rinaldi+St,+Los+Angeles,+CA+91344/10663+Yarmouth+Ave,+Granada+Hills,+CA+91344/@34.2718048,-118.5208106,14z/data=!3m1!4b1!4m13!4m12!1m5!1m1!1s0x80c2900992118cb1:0x33e7de3cd8afaf17!2m2!1d-118.4846721!2d34.27918!1m5!1m1!1s0x80c29add568c4543:0x98e7417a1b27d322!2m2!1d-118.5219299!2d34.2641603"

def mytrust(city):
    data = """
    Name: Law offices of Savin & Bursk
    Phone: 818-368-8646
    Address = 10663 Yarmouth Ave.
    Granada Hills, CA. 91344
    """

    if city != "Granada Hills":
        return "incorrect city, please enter Granada Hills"
        exit()
    else:
        return data

trust = mytrust(city)

print(trust)

webbrowser.open_new(url)
webbrowser.open_new(directions)

