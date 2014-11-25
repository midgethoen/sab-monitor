#! /usr/bin/python
import Image,ImageDraw
import datetime, MySQLdb
from cStringIO import StringIO

def index():
    img = Image.open("/var/www/clients/client0/web4/web/sabspeedgraph_template.png")
    draw = ImageDraw.Draw(img)
    
    vannacht = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d 00:00:00")
    eergister = (datetime.datetime.now() - datetime.timedelta(days=0)).strftime("%Y-%m-%d 00:00:00")
    
    db = MySQLdb.connect(host='localhost',user='c1midgethoen',passwd='12478786',db='c1sabstats')
    c=db.cursor()
    c.execute("SELECT * FROM sabspeed WHERE time <= %s AND time >= %s ORDER BY time ASC LIMIT 288",(vannacht, eergister))
    
    
    
    top = 124
    left = 20
    result = c.fetchall()
    cnt = 0
    for row in result:
      cnt = cnt + 1
      print row[1]
      if row[1] != 0:
        y = top - row[1] / 10
        x = left + cnt
        draw.line((x, top, x, y), fill="#fdb700")
        
    
    file = StringIO()
    img.save(file,"PNG")
    return file.getvalue()
    