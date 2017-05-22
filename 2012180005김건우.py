import http.client
conn = http.client.HTTPConnection("apis.data.go.kr")
conn.request("GET",
             """1430000/StdPatStsInfoService/getRealtimeStatisticsInfo?serviceKey=
             RfXMKfQ7poleOdmbgzrOPTeccpDIkYlwmQCxZNI3mNo3OBYPX22pBUNLBx%2F%2BB7KLw21aM43w5YSxW9yAYnuMfQ%3D%3D
             &numOfRows=10&pageSize=10&pageNo=1&startPage=1&resultType=xml&workverymn=201612&stdorgancd=ETSI&
             countryclass=%EA%B8%B0%EC%97%85&dtltech1=3GPP&dtltech2=LTE&declarer_adjust=Apple&
             declarercountry_adjust=%EB%AF%B8%EA%B5%AD&club2050yn=N&oecdyn=N&comptype=%EB%AF%B8%EA%B5%AD""")
req = conn.getresponse()
print(req.status,req.reason)
cLen = req.getgeader("Content-Length")
req.read(cLen)
