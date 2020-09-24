from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as p
import whois
import urllib.parse
import csv
#функция по форматированию csv файла
def ooo():
    df = p.read_csv('result.csv', delimiter=';')
    for i in range(0,len(df['Emails:'])):
        if df['Emails:'][i][3]=='\'':
            print(''.join(df['Emails:'][i].replace('[', '').replace(']', '').replace(',', '').replace('\'', '').replace(' ', '')))
            df['Emails:'][i]=''.join(df['Emails:'][i].replace('[', '').replace(']', '').replace(',', '').replace('\'', '').replace(' ', ''))
        else:
            print(''.join(df['Emails:'][i].replace('[', '').replace(']', '').replace(',', '').replace('\'', '')))
            df['Emails:'][i] = ''.join(df['Emails:'][i].replace('[', '').replace(']', '').replace(',', '').replace('\'', '').replace(' ', ','))
    df.to_csv('result.csv', sep=';', index=False)
i=open("result.csv","w",newline="")#открывает файл на запись
writer=csv.writer(i,delimiter=";")#записывает с ограничителем ;
writer.writerow(["Company:","Site:","Emails:"])#запись заголовка
with open(r"r.txt", "r") as f:#открытие файла на чтение
        for line in f:
                try:
                    query = urllib.parse.quote(line)  # encoding name company of parameter to url
                    SiteCompany = BeautifulSoup(urlopen("https://www.whois.com/whois/" + query), "lxml").find("div",class_="df-value")#парсит домен
                    writer.writerow([line.strip(), SiteCompany.get_text(),[j for j in whois.whois(SiteCompany.get_text()).emails]])#запись результа
                    print("Name: {}\nSite: {}\n".format(line.strip(),SiteCompany.get_text()))#вывод для наглядности процесса
                except AttributeError:#исключение при котором сайт не находит домен
                    print("company does not exist\n")
                    continue
i.close()
ooo()
print('ＰＲＯＧＲＡＭ＿ＫＩＬＬ')


