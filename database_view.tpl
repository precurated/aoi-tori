<h1>Database View</h1>
<table>
<tr><th>account_id</th><th>twitter name</th><th>subreddit</th></tr>
%for row in rows:
    <tr>
    %for col in row:
        <td>{{col}}</td>
    %end
    </tr>
%end
</table>