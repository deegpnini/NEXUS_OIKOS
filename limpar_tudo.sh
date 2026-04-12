#!/bin/bash

# 🧹 Limpa todos os arquivos gerados

echo "🧹 Limpando arquivos gerados pelo NEXUS..."

cd ~/Desktop/NEXUS_OIKOS

# Mata explorer se estiver rodando
if [ -f explorer_pid.txt ]; then
    PID=$(cat explorer_pid.txt)
    kill $PID 2>/dev/null
    echo "✅ Explorer finalizado"
fi

# Limpa pastas
rm -rf dados/*.csv
rm -rf midia/*.png
rm -rf midia/*.json
rm -rf logs/*.log
rm -rf backup/*

echo "✅ Limpeza concluída"
echo "🏛️ Pronto para começar de novo"
