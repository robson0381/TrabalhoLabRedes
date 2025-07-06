@echo off
echo >>> Reiniciando prog3 limpo...

REM Verifica qual processo usa a porta 6001
for /f "tokens=5" %%a in ('netstat -ano ^| findstr ":6001"') do (
    echo >>> Encontrado processo na porta 6001 (PID %%a), encerrando...
    taskkill /F /PID %%a
    goto done
)

echo >>> Nenhum processo encontrado usando a porta 6001.

:done
echo >>> Agora reinicie prog3 normalmente com docker exec.
pause
