$eggfiles = @(Get-ChildItem -Path * -Filter *.egg)

Write-Host 'Converting .egg to .bam...'

for ($i = 0 ; $i -le $eggfiles.Length ; $i++){
    #building the array
    Write-Host 'Found you '$eggfiles[$i]
    $bamname = $eggfiles[$i] -Replace '\.egg$','.bam'
    Write-Host 'Should come out to '$eggfiles[$i]
    Write-Host '
    '
    .\egg2bam.exe $eggfiles[$i].toString() $bamname.ToString()
}