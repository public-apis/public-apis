[CmdletBinding()]
param()

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
Set-Location -LiteralPath $repoRoot

$venvPython = Join-Path $repoRoot ".venv\Scripts\python.exe"
if (Test-Path -LiteralPath $venvPython) {
    $pythonExe = $venvPython
} else {
    $pythonExe = (Get-Command python -ErrorAction Stop).Source
}

$env:PYTHONUTF8 = "1"
$env:PYTHONIOENCODING = "utf-8"

function Invoke-PythonStep {
    param(
        [Parameter(Mandatory)]
        [string]$Label,
        [Parameter(Mandatory)]
        [string[]]$Arguments
    )

    Write-Host "==> $Label"
    & $script:pythonExe @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "$Label failed with exit code $LASTEXITCODE"
    }
}

Invoke-PythonStep -Label "Compile maintained Python" -Arguments @(
    "-m", "compileall", "-q", "scripts", "tests", "tools"
)
Invoke-PythonStep -Label "Ruff (E9 + F)" -Arguments @(
    "-m", "ruff", "check", "--select", "E9,F", "--target-version", "py39",
    "tests", "tools"
)
Invoke-PythonStep -Label "Pytest" -Arguments @("-m", "pytest", "tests", "-q")

Write-Host "==> Upstream validate package tests"
Push-Location -LiteralPath (Join-Path $repoRoot "scripts")
try {
    & $pythonExe -m unittest discover tests --quiet
    if ($LASTEXITCODE -ne 0) {
        throw "Upstream validate package tests failed with exit code $LASTEXITCODE"
    }
}
finally {
    Pop-Location
}

Invoke-PythonStep -Label "Check Markdown links" -Arguments @(
    "tools\check_links.py"
)

Write-Host "WINDOWS DEV CHECK GREEN"
