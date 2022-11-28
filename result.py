import requests as r
from bs4 import BeautifulSoup as bs
import re


def get_number(roll):
    url = 'https://sresult.bise-ctg.gov.bd/s22/individual/result.php'
    data = {'roll': roll}
    res = r.post(url, data)
    sp = bs(res.text, 'html.parser')
    if sp.find('h3') != None:
        return False
    #total    
	
    nums = sp.find_all('td', class_='cap_lt')
    total = 0
    gpa = ''
    for i in nums:
        if re.search(r'GPA=\d+', str(i)) != None:
            gpa = str(i.text)[4:]
        if re.search(r'\d{3}\(.+\)', str(i)) != None:
            total += int(str(i.text)[:3])

    name = str(sp.find('td', width=True, class_='cap_lt').text)
    return {
        'name':name,
        'gpa':gpa,
        'total':total
    }

data = get_number(int(input('Enter your Roll number:')))
name = data['name']
gpa = data['gpa']
total = data['total']
print(f'\n\nDear {name},\n\nYour gpa is {gpa}\nYour total marks is {total}\n\n')
