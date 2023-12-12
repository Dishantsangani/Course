import geo

ip = geo.IP()
print(ip)

country = geo.getcountry(ip,'plain')
print(country)

country = geo.getcountry(ip,'json')
print(country)

geodata = geo.getgeoData(ip)
print(geodata)

ptrData = geo.getPTR(ip)
print(ptrData)

geo.showIpdetails('216.239.32.0')
geo.showCountryDetails('216.239.32.0')


