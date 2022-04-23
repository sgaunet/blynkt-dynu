# blynkt-dynu

Just some scripts to update a dynu.net dynamic dns and blink led of a blink pimoroni.
The code worked, is not beautiful... developped quickly for a friend.

I don't use it anymore.

You need to create an account on dynu.net to use it.

## bash version

One script to update the dynamic dns without blink leds.

## python version

The script blink leds also (worked on a raspberry py with pimoroni LEDS).

There is a dyndns.service file to setup a systemd.

Setup is easy :

```
mkdir /opt/dyndns
cp maj-dns.py /opt/dyndns/

cp dydns.service /...
systemctl enable dyndns
systemctl start dyndns
```