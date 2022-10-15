link = input("Link girin : ")
link = link.replace("www.","m.")
print(link)
try:
    res = requests.get(link)
    print("The status code is ", res.status_code)
    print("\n")
    soup_data = BeautifulSoup(res.text, 'html.parser')
    print(soup_data)
    print("\n")
    concl = soup_data.select("div.bo.bp")

    
    s = str(concl[0]).split(",")
    print(s[0].split('"')[3]+ " : " + s[0].split('"')[5])
except Exception as exc:
    print(exc)
