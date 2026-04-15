#!/usr/bin/env python3
"""
🏛️ NEXUS OIKOS — MENU INTERATIVO DENTRO DO VS CODE
Executa todas as funções do sistema
"""

import os
import subprocess
import json
import sys
from datetime import datetime

# Cores para terminal
class Cores:
    VERMELHO = '\033[0;31m'
    VERDE = '\033[0;32m'
    AMARELO = '\033[1;33m'
    AZUL = '\033[0;34m'
    ROXO = '\033[0;35m'
    CIANO = '\033[0;36m'
    BRANCO = '\033[1;37m'
    NC = '\033[0m'

def limpar_tela():
    os.system('clear')

def cabecalho():
    print(Cores.ROXO + "╔══════════════════════════════════════════════════════════════════╗")
    print("║     🏛️ NEXUS OIKOS — MODO INTERATIVO (VS CODE)                       ║")
    print("╚══════════════════════════════════════════════════════════════════╝" + Cores.NC)
    print()

def menu_vscode():
    print(Cores.AMARELO + "════════════════════════════════════════════════════════════════" + Cores.NC)
    print(Cores.BRANCO + "🎮 PAINEL DE CONTROLE — NEXUS OIKOS" + Cores.NC)
    print(Cores.AMARELO + "════════════════════════════════════════════════════════════════" + Cores.NC)
    print()
    print(f" {Cores.VERDE}1{Cores.NC} 📊 Analisar Dados do TikTok")
    print(f" {Cores.VERDE}2{Cores.NC} 🚀 Rodar NEXUS CORE ML")
    print(f" {Cores.VERDE}3{Cores.NC} 🧠 Ver Memória Longitudinal")
    print(f" {Cores.VERDE}4{Cores.NC} 📹 Calcular D_c de um vídeo")
    print(f" {Cores.VERDE}5{Cores.NC} 💾 Sincronizar GitHub")
    print(f" {Cores.VERDE}6{Cores.NC} 🌡️  Ver temperatura do sistema")
    print(f" {Cores.VERDE}7{Cores.NC} 📈 Ver relatório completo do TikTok")
    print(f" {Cores.VERDE}8{Cores.NC} 🧹 Limpar cache e otimizar")
    print(f" {Cores.VERDE}9{Cores.NC} 🔄 Status do Shadowban")
    print(f" {Cores.VERDE}0{Cores.NC} ❌ Voltar ao menu principal")
    print()
    print(Cores.AMARELO + "════════════════════════════════════════════════════════════════" + Cores.NC)

def analisar_tiktok():
    print(Cores.CIANO + "\n📊 ANALISANDO DADOS DO TIKTOK..." + Cores.NC)
    dados_path = "../dados/dados_tiktok_completo.json"
    if os.path.exists(dados_path):
        with open(dados_path, 'r') as f:
            dados = json.load(f)
        print(f"\n   📈 Views totais: {dados['metricas_crescimento']['visualizacoes_totais']['depois']:,}")
        print(f"   👥 Seguidores: +{dados['metricas_crescimento']['seguidores_liquidos']['crescimento']}")
        print(f"   ⚠️ Taxa de curtidas: {dados['alertas_criticos']['taxa_curtidas']['depois']}%")
    else:
        print("   ❌ Arquivo de dados não encontrado")
    print("\n" + Cores.CIANO + "   ✅ Análise concluída!" + Cores.NC)

def rodar_nexus_core():
    print(Cores.CIANO + "\n🚀 RODANDO NEXUS CORE ML..." + Cores.NC)
    if os.path.exists("nexus_core_ml.py"):
        subprocess.run(["python3", "nexus_core_ml.py"])
    else:
        print("   ❌ nexus_core_ml.py não encontrado")

def ver_memoria():
    print(Cores.CIANO + "\n🧠 MEMÓRIA LONGITUDINAL..." + Cores.NC)
    memoria_path = "../memoria/nexus_memoria_completa.json"
    if os.path.exists(memoria_path):
        with open(memoria_path, 'r') as f:
            memoria = json.load(f)
        print(f"\n   👤 Maestro: {memoria['identidade']['maestro']}")
        print(f"   🎓 Cursos concluídos: {len(memoria['sctec_jornada']['concluidos'])}")
        print(f"   🤖 Agentes: {list(memoria['agentes_trinity'].keys())}")
    else:
        print("   ❌ Memória não encontrada")

def calcular_dc():
    print(Cores.CIANO + "\n📹 CALCULANDO D_c DE UM VÍDEO..." + Cores.NC)
    try:
        views = int(input("   📊 Views do vídeo: "))
        likes = int(input("   ❤️ Likes: "))
        comentarios = int(input("   💬 Comentários: "))
        compart = int(input("   🔄 Compartilhamentos: "))
        
        # Fórmula D_c simplificada
        taxa_like = likes / max(views, 1)
        engajamento = taxa_like
        d_c = (views / 10000) * engajamento * 1.2
        
        print(f"\n   📊 RESULTADO:")
        print(f"   D_c: {d_c:.4f}")
        if d_c >= 0.7:
            print("   🔥 Classificação: VIRAL!")
        elif d_c >= 0.4:
            print("   📈 Classificação: PROMISSOR")
        elif d_c >= 0.2:
            print("   📊 Classificação: MÉDIO")
        else:
            print("   ⚠️ Classificação: BAIXO - Precisa melhorar")
    except:
        print("   ❌ Erro nos dados")

def sincronizar_github():
    print(Cores.CIANO + "\n💾 SINCRONIZANDO COM GITHUB..." + Cores.NC)
    os.chdir("..")
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", f"Update via NEXUS {datetime.now().strftime('%Y%m%d_%H%M%S')}"])
    subprocess.run(["git", "push"])
    os.chdir("codigo")
    print("   ✅ Sincronizado!")

def ver_temperatura():
    print(Cores.CIANO + "\n🌡️ TEMPERATURA DO SISTEMA..." + Cores.NC)
    subprocess.run(["sensors"])

def relatorio_completo():
    print(Cores.CIANO + "\n📈 RELATÓRIO COMPLETO DO TIKTOK..." + Cores.NC)
    if os.path.exists("consultar_dados_tiktok.py"):
        subprocess.run(["python3", "consultar_dados_tiktok.py"])
    else:
        print("   ❌ Script não encontrado")

def limpar_sistema():
    print(Cores.CIANO + "\n🧹 LIMPANDO CACHE E OTIMIZANDO..." + Cores.NC)
    subprocess.run(["sudo", "apt", "clean"])
    subprocess.run(["rm", "-rf", "~/.cache/thumbnails/*"])
    print("   ✅ Limpeza concluída")

def status_shadowban():
    print(Cores.CIANO + "\n🔄 STATUS DO SHADOWBAN/RECUPERAÇÃO..." + Cores.NC)
    print("""
   📋 STATUS ATUAL:
   • Shadowban: ⚠️ POSSÍVEL
   • Pausa nas postagens: EM ANDAMENTO (48-72h)
   • Retenção: 🔴 CRÍTICA (abandono em 1s)
   
   🎯 RECOMENDAÇÃO:
   • Aguardar fim da pausa
   • Postar 1 vídeo CURTO com hook forte
   • Responder comentários nos primeiros 30min
   • Monitorar % For You Page
   
   ✅ HOOK APROVADO:
   'A Lua tem bilhões de toneladas de água...
   Só que tem um problema: ninguém é dono disso.
   Comenta: SABIA ou NÃO SABIA.'
    """)

def main():
    while True:
        limpar_tela()
        cabecalho()
        menu_vscode()
        
        opcao = input(f"{Cores.CIANO}👉 Digite a opção [0-9]: {Cores.NC}")
        
        if opcao == "1":
            analisar_tiktok()
        elif opcao == "2":
            rodar_nexus_core()
        elif opcao == "3":
            ver_memoria()
        elif opcao == "4":
            calcular_dc()
        elif opcao == "5":
            sincronizar_github()
        elif opcao == "6":
            ver_temperatura()
        elif opcao == "7":
            relatorio_completo()
        elif opcao == "8":
            limpar_sistema()
        elif opcao == "9":
            status_shadowban()
        elif opcao == "0":
            print(f"\n{Cores.VERDE}🏛️ Voltando ao menu principal...{Cores.NC}")
            break
        else:
            print(f"\n{Cores.VERMELHO}❌ Opção inválida!{Cores.NC}")
        
        print(f"\n{Cores.AMARELO}Pressione ENTER para continuar...{Cores.NC}")
        input()

if __name__ == "__main__":
    main()
