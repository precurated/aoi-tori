<link rel="stylesheet" type="text/css" href="style.css">

<h1>Database View</h1>
<table border="1">
<tr><th>account_id</th><th>twitter name</th><th>subreddit</th></tr>
%for row in rows:
    <tr>
    %for col in row:
        <td>{{col}}</td>
    %end
    </tr>
%end
</table>