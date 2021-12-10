from website.models import Link
from website import db

f = open('data.txt', 'r')
lines = f.readlines()
for line in lines:
    t = line.split('\t')
    link = Link(link=t[0], url=t[1], title=t[2], name=t[3], desc=t[4], image=t[5], clicks=0)
    db.session.add(link)
    db.session.commit()
f.close()
# return f"{self.link}\t{self.url}\t{self.title}\t{self.name}\t{self.desc}\t{self.image}\t"
