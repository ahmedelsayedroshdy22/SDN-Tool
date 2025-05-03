
Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing



Write-Host "Installing Excel Module.." -ForegroundColor Yellow


Install-Module -Name ImportExcel -Scope AllUsers -Force

Import-Module ImportExcel

Write-Host "Excel Module has been Installed successfully " -ForegroundColor Yellow


$sourceDir = Get-Location

# Define the destination directory
$destinationDir = "$env:USERPROFILE"

# Get all zip files in the source directory
$zipFiles = Get-ChildItem -Path $sourceDir -Filter *.zip

# copy each zip file to the destination directory
foreach ($zipFile in $zipFiles) {
    Copy-Item -Path $zipFile.FullName -Destination $destinationDir
}

Write-Output "All zip files have been moved to $destinationDir"





if(Test-Path -Path 'C:\Util\CCD\Customers_CSV'){

Write-Host "Tool has already been installed successfully , Nothing to be done else here !" -ForegroundColor Red

}

else {

New-Item -Path 'C:\Util\CCD\Customers_CSV' -ItemType Directory -Force
New-Item -Path 'C:\Util\CCD\GiniData' -ItemType Directory -Force
New-Item -Path 'C:\Util\CCD\Credentials.txt' -ItemType File -Force -Value "nuar-username,nuar-password"


Write-Host " SDN Tool environment has been created successfully !" -ForegroundColor Green

}

cd $env:USERPROFILE

Expand-Archive -Path ".\CCD.zip" -DestinationPath "C:\Util"


Expand-Archive -Path ".\Sonus.zip" -DestinationPath "$env:USERPROFILE\OneDrive - orange.com\Documents\PowerShell\Modules\SonusModule"  

Write-Host " Sonus installed correctly into One drive --- Found One Drive Cloud ---" -ForegroundColor Yellow

Expand-Archive -Path ".\Sonus.zip" -DestinationPath "$env:USERPROFILE\Documents\PowerShell\Modules\SonusModule"

Write-Host " Sonus installed correctly into normal path " -ForegroundColor Yellow

Write-Host ">>>>>>>>  SDN Module has been imported successfully  >>>>>>>>" -ForegroundColor Green




###################################### Registering task for refereshing ##################################################

$action =New-scheduledTaskAction -Execute 'Powershell.exe' -Argument 'C:\Util\CCD\RefreshList.ps1'
$trigger=New-scheduledTaskTrigger -Weekly -WeeksInterval 2 -DaysOfWeek Monday -At 10am
Register-scheduledTask -Action $action -Trigger $trigger -TaskName "RefreshAssetListScript" -Description "Ahmed Zayed2024"

Write-Host "Registration task has been registered for refreshing the asset list"


##########################################################################################################################


################################show only ################################
$totalSteps = 20
# Loop through each step
for ($i = 0; $i -le $totalSteps; $i++) {
    $percentComplete = ($i / $totalSteps) * 100
    $loadingBar = '[' + '=' * $i + ' ' * ($totalSteps - $i) + ']'
    Write-Host "`r" -NoNewline
    Write-Host "Loading $percentComplete% $loadingBar" -ForegroundColor White -BackgroundColor Green
    Start-Sleep -Milliseconds 250
}


###########################################################################


[void][System.Windows.Forms.MessageBox]::Show(" SDN TOOL is successfully installed", 'Installtion Status')

Read-Host -Prompt "Press Enter to exit"
