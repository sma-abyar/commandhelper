@set PYTHONIOENCODING=utf-8
@powershell -noprofile -c "cmd /c \"$(commandhelper %* $(doskey /history)[-2])\"; [Console]::ResetColor();"
