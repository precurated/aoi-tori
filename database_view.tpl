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

{{date}}

<p align=center><a href="/">home</a> - add - modify - analyze - auth</p>