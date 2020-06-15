''' Question: Write a Python program to valid a IP address.

Solution: '''

ip_address = input('Enter an IP-Address: ')
octets = ip_address.split('.')

#validating the ip_address
if len(octets) == 4:
    flag = 0
    for octet in octets:
        int_octet = int(octet)
        if int_octet>=0 and int_octet<=255:
            continue
        else:
            flag = 1
            break
    if flag == 0:
        print("{} is a valid IP Address....".format(ip_address))
    else:
        print("{} is not a valid IP Address...".format(ip_address))
else:
    print("{} is not a valid IP Address...".format(ip_address))
