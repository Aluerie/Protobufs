./venv/Scripts/Activate.ps1
Set-Location -Path "dota2"
Get-ChildItem "." -Filter *.proto |
Foreach-Object {
    $relative_name = '{0}{1}' -f $_.BaseName, $_.Extension
    ../protoc.exe -I . --python_betterproto_out=py_mirrors $relative_name
}
Set-Location -Path ".."
