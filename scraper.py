import requests 
from bs4 import BeautifulSoup
from csv import writer

# Request to get sampleblog html
urlBlog = "http://codedemos.com/sampleblog/"
response = requests.get(urlBlog)

soup = BeautifulSoup(response.text ,'html.parser')
posts = soup.find_all(class_='post-preview')

# open posts.csv file in write mode
# newline='' otherwise windows automatically adds an extra newline on "writerow"
with open('posts.csv','w', newline='') as csv_file:
    csv_writer = writer(csv_file)
    # add headers
    csv_writer.writerow(["Title", "Link", "Date"])
    
    for post in posts:
        title = post.find(class_='post-title').get_text().replace('\n', '').strip()
        link = urlBlog + post.find('a').get('href')
        date = post.select('.post-date')[0].get_text()
        # write post data to csv file
        csv_writer.writerow([title, link, date])
