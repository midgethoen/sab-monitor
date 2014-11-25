#! /usr/bin/python
def index():
 import urllib2
 import os
 from mod_python import psp 
 #retrieve current speed from SABnzbd
 url = 'http://192.168.2.10:8888/sabnzbd/api?ma_password=zandzak&mode=qstatus&apikey=a9b169c655bce472423068df3acc0dd2&ma_username=midgethoen&output=json'
 try:
  res = urllib2.urlopen(url)
  img = "green.png"
 except:
  img = "red.png"
 html1 = """
	<html>
<head>
<title>SABMonitor</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
</head>
<body bgcolor="#FFFFFF" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
<!-- Save for Web Slices (sabspeedgraph.psd) -->
<table id="Table_01" width="540" height="170" border="0" cellpadding="0" cellspacing="0">
	<tr>
		<td colspan="5">
			<img src="images/sabspeedgraph_01.png" width="540" height="14" alt=""></td>
	</tr>
	<tr>
		<td colspan="3"><a href="http://sabnzbd.midgethoen.nl"><img src="images/sabspeedgraph_02.png" alt="" width="177" height="120" border="0"></a></td>
		<td rowspan="2">
			<img src="sabgraph.py" width="333" height="141" alt=""></td>
		<td rowspan="3">
			<img src="images/sabspeedgraph_04.png" width="30" height="156" alt=""></td>
	</tr>
	<tr>
		<td rowspan="2">
			<img src="/images/sabspeedgraph_05.png" width="111" height="36" alt=""></td>
		<td><img src='"""

			
 html2 =	"""' width='22' height='21' alt=''><td rowspan="2">
			<img src="images/sabspeedgraph_07.png" width="44" height="36" alt=""></td>
	</tr>
	<tr>
		<td>
			<img src="images/sabspeedgraph_08.png" width="22" height="15" alt=""></td>
		<td>
			<img src="images/sabspeedgraph_09.png" width="333" height="15" alt=""></td>
	</tr>
</table>
<!-- End Save for Web Slices -->
</body>
</html>"""
 return html1 + img + html2