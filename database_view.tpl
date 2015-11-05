%import datetime
%import time

<link rel="stylesheet" type="text/css" href="style.css">

<h1>{{title}}</h1>
<table border="1">
<tr>
%for column in columns:
	<th>{{column}}</th>
%end
</tr>

%for row in rows:
    <tr>
    %for col in row:
        <td>{{col}}</td>
    %end
    </tr>
%end
</table>

<p align=center>
	<a href=/>Tweets</a> -
	<a href=accounts>Accounts</a> -
	<a href=groups>Groups</a> -
	<a href=rules>Rules</a> -
	<a href=apps>Apps</a>
</p>

%time = datetime.datetime.now().strftime('%Y %b %d %A %H:%M:%S')

<p align=right>{{time}} </p>
