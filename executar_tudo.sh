#!/bin/bash

# 🏛️ NEXUS OIKOS — EXECUTOR MESTRE
# Roda análise, depois social, e deixa explorer em background

cd ~/Desktop/NEXUS_OIKOS/codigo

echo ""
echo "════════════════════════════════════════════════════════"
echo "   🏛️ NEXUS OIKOS — EXECUTANDO ECOSSISTEMA COMPLETO"
echo "════════════════════════════════════════════════════════"
echo ""

# Passo 1: Mostrar status do NEXUS
echo "📊 STATUS DO SISTEMA:"
python3 nexus_core.py
echo ""

# Passo 2: Executar análise
echo "📈 INICIANDO ANÁLISE DE DADOS..."
python3 analise_automatica.py
echo ""

# Passo 3: Gerar conteúdo social
echo "🕊️ GERANDO CONTEÚDO PARA REDES SOCIAIS..."
python3 social_automatico.py
echo ""

# Passo 4: Iniciar explorer em background
echo "🛡️ INICIANDO MONITOR DE ARQUIVOS (background)..."
python3 explorer_automatico.py &
EXPLORER_PID=$!
echo "✅ Explorer rodando em segundo plano (PID: $EXPLORER_PID)"
echo ""

# Passo 5: Mostrar onde estão os arquivos
echo "════════════════════════════════════════════════════════"
echo "📁 ARQUIVOS GERADOS:"
echo "   📊 Dados: ~/Desktop/NEXUS_OIKOS/dados/analise_completa.csv"
echo "   📈 Gráfico: ~/Desktop/NEXUS_OIKOS/midia/analise_automatica.png"
echo "   🕊️ Social: ~/Desktop/NEXUS_OIKOS/midia/conteudo_social.json"
echo "   📝 Logs: ~/Desktop/NEXUS_OIKOS/logs/nexus.log"
echo "════════════════════════════════════════════════════════"
echo ""
echo "🏛️ O fluxo segue. Sistema operacional."
echo ""
echo "⚠️  Para parar o explorer, execute: kill $EXPLORER_PID"
echo ""

# Salva PID para matar depois
echo $EXPLORER_PID > ~/Desktop/NEXUS_OIKOS/explorer_pid.txt
