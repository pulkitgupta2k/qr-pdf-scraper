from bs4 import BeautifulSoup
from pprint import pprint
import json
from openpyxl import Workbook

def get_soup(path):
    with open(path) as f:
        html = f.read()
    return BeautifulSoup(html, 'html.parser')

data = {}

def get_page(number):
    soup = get_soup(f"data/{number}.html")
    spans = soup.find_all("span")
    spans_info = []
    for span in spans:
        spans_info.append(span.text)
    
    for i in range(len(spans_info)):
        print(str(i) + "  " + spans_info[i] )
    
    coach_info = [spans_info[1] , spans_info[3], spans_info[5]]
    title = spans_info[-3]
    year = spans_info[-4]
    START = 16


    if title.strip() == "NA LACROSSE":
        title = spans_info[-4]
        year = spans_info[-5]
    
    if title.strip() == "SUMMER INVITATIONAL":
        title = spans_info[-1]
        year = spans_info[-2]
    

    if spans_info[13].strip() == "Player E-Mail":
        START = 14

    rows = []
    
    row = [""]*10

    for i in range(START, len(spans_info)-5):
        position = int(float(spans[i]['style'].split(";")[0][6:-2]))
        
        if position <= 35:
            rows.append(row)
            row = [""]*10
            row[0] = spans_info[i]
        
        elif position <= 100:
            row[1] = spans_info[i]
        
        elif position <= 150:
            row[2] = spans_info[i]

        elif position <= 220:
            row[3] = spans_info[i]

        elif position <= 279:
            row[4] = spans_info[i]

        elif position <= 350:
            row[5] = spans_info[i]

        elif position <= 450:
            row[6] = spans_info[i]

        elif position <= 550:
            row[7] = spans_info[i]

        elif position <= 680:
            row[8] = spans_info[i]
        
        elif position <= 800:
            row[9] = spans_info[i]

    rows.append(row)
    rows = rows[1:]
    # for row in rows:
    #     print(row)

    data[number] = {
        "coach_info" : coach_info,
        "title" : title,
        "year" : year,
        "rows" : rows
    }

def create_excel():
    with open("data.json") as f:
        data = json.load(f)
    wb = Workbook()
    for key, value in data.items():
        wi = wb.create_sheet()
        wi.title = value['title'].strip() + "_" + key
        wi.append(["No.", "LastName", "FirstName", "Position", "Year", "HighSchool", "CellPhone", "Player E-Mail", "Comitted", "Noted"])
        for row in value['rows']:
            wi.append(row)
    wb.save('data.xlsx')
    


if __name__ == "__main__":
    for i in range(1, 84):
        get_page(i)
    
    with open("data.json", "w") as f:
        json.dump(data, f)

    create_excel()