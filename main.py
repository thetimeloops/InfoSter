import subd_slow



print(r'''

.___        _____       _________ __
|   | _____/ ____\____ /   _____//  |_  ___________
|   |/    \   __\/  _ \\_____  \\   __\/ __ \_  __ \
|   |   |  \  | (  <_> )        \|  | \  ___/|  | \/
|___|___|  /__|  \____/_______  /|__|  \___  >__|
         \/                   \/           \/

                                    with <3 from CyberImposters
                                    for more www.cyberimposters.com



'''

)

print('''

[1] SubDomain Scan without threads ( SLOW & INTENSE )
[2] SubDomain Scan with threads (Extraordinary FAST )
''')


choice = input("?>>>")

if choice=="1":


    url1 = input("URL:-> ")
    subd_slow.subdomains_slow(url1)

else:
    import subd_fast
