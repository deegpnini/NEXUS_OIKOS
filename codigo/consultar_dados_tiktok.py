#!/usr/bin/env python3
"""
📊 NEXUS OIKOS — CONSULTOR DE DADOS TIKTOK
Exibe relatório completo atualizado
"""

import json
import os
from datetime import datetime

def mostrar_dados():
    dados_path = "../dados/dados_tiktok_completo.json"
    
    if not os.path.exists(dados_path):
        print("❌ Arquivo de dados não encontrado!")
        return
    
    with open(dados_path, 'r') as f:
        dados = json.load(f)
    
    print("\n" + "="*60)
    print("🏛️ NEXUS OIKOS — RELATÓRIO TIKTOK ATUALIZADO")
    print(f"📅 {dados['data_atualizacao']} | Período: {dados['periodo']}")
    print("="*60)
    
    # Métricas de crescimento
    print("\n📈 MÉTRICAS DE CRESCIMENTO:")
    metricas = dados['metricas_crescimento']
    for key, value in metricas.items():
        nome = key.replace('_', ' ').title()
        print(f"   • {nome}: {value['antes']:,} → {value['depois']:,} ({value['crescimento']})")
    
    # Alertas críticos
    print("\n⚠️ ALERTAS CRÍTICOS:")
    alertas = dados['alertas_criticos']
    print(f"   • Taxa de curtidas: {alertas['taxa_curtidas']['antes']}% → {alertas['taxa_curtidas']['depois']}% ({alertas['taxa_curtidas']['variacao']})")
    print(f"   • Retenção média: {alertas['retencao_media']['antes']} → {alertas['retencao_media']['depois']} {alertas['retencao_media']['status']}")
    print(f"   • Ponto de abandono: {alertas['ponto_abandono']['antes']} → {alertas['ponto_abandono']['depois']} {alertas['ponto_abandono']['status']}")
    
    # Vídeos destaque
    print("\n🎬 VÍDEOS DE DESTAQUE:")
    for video in dados['videos_destaque']:
        print(f"   • {video['titulo'][:40]}...")
        print(f"     {video['views']:,} views | {video['likes']} likes | {video['status']}")
    
    # Diagnóstico
    print("\n🔍 DIAGNÓSTICO:")
    diag = dados['diagnostico']
    print(f"   • Shadowban: {diag['shadowban']}")
    print(f"   • Causa: {diag['causa_provavel']}")
    print(f"   • Retenção 3s: {diag['retencao_3s']}")
    
    # Plano de recuperação
    print("\n🔄 PLANO DE RECUPERAÇÃO:")
    fase1 = dados['plano_recuperacao']['fase_1_cool_down']
    print(f"   • Fase 1 (Cool Down): {fase1['status']} - {fase1['duracao']}")
    
    # Hook aprovado
    print("\n🎯 HOOK APROVADO PARA O RETORNO:")
    print(f"   {dados['hook_aprovado']['texto']}")
    
    print("\n" + "="*60)
    print("🏛️ O fluxo segue. Dados atualizados com sucesso!")
    print("="*60)

if __name__ == "__main__":
    mostrar_dados()
