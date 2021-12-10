from website.models import Link

f = open('data.txt', 'w')
links = Link.query.all()
for link in links:
    temp = str(link)
    f.write(f'{temp}\n')
f.close()