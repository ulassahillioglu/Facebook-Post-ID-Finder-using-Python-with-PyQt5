input_link = input("Enter the link : ")
link = str(input_link).replace("www","m")
res = rq.get(link)
soup_data = bs(res.text, 'html.parser')
concl = soup_data.find_all('div',{'class' : 'bo bp'})

s = str(concl[0]).split(",")
global final_result
final_result = s[1]
print(final_result)
