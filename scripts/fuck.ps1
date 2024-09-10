if ((Get-Command "fuck").CommandType -eq "Function") {
	fuck @args;
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

"  - Adding fuck() function to current session..."
$env:PYTHONIOENCODING='utf-8'
iex "$($(commandhelper --alias).Replace("function fuck", "function global:fuck"))"

"  - Invoking fuck()`n"
fuck @args;
[Console]::ResetColor()
