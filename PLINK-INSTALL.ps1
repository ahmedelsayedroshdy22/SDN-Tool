$url = "https://the.earth.li/~sgtatham/putty/latest/w64/plink.exe"
$destination = "C:\Program Files (x86)\PuTTY\plink.exe"
if (-not (Test-Path "C:\Program Files (x86)\PuTTY")) {
    New-Item -ItemType Directory -Path "C:\Program Files (x86)\PuTTY"
}
Invoke-WebRequest -Uri $url -OutFile $destination
[System.Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\Program Files (x86)\PuTTY\", [System.EnvironmentVariableTarget]::Machine)