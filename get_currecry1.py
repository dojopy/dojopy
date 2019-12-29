from ip2geotools.databases.noncommercial import DbIpCity
response = DbIpCity.get('147.229.2.90', api_key='free')
print(response.country)

