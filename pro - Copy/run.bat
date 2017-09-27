@echo off
setlocal
set "lock=%temp%\wait%random%.lock"
start "" 9>"%lock%1" python player1.py
start "" 9>"%lock%2" python player2.py

1>nul 2>nul ping /n 2 ::1
for %%N in (1 2) do (
  (call ) 9>"%lock%%%N" || goto :Wait
) 2>nul

del "%lock%*"
echo Done - ready to continue processing