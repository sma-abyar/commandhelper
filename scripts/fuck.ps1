if ((Get-Command "alo").CommandType -eq "Function") {
	alo @args;
	[Console]::ResetColor()
	exit
}

"First time use of commandhelper detected. "

if ((Get-Content $PROFILE -Raw -ErrorAction Ignore) -like "*commandhelper*") {
} else {
	"  - Adding commandhelper intialization to user `$PROFILE"
	$script = "`n`$env:PYTHONIOENCODING='utf-8' `niex `"`$(commandhelper --alias)`"";
	Write-Output $script | Add-Content $PROFILE
}

"  - Adding alo() function to current session..."
$env:PYTHONIOENCODING='utf-8'
iex "$($(commandhelper --alias).Replace("function alo", "function global:alo"))"

"  - Invoking alo()`n"
alo @args;
[Console]::ResetColor()
