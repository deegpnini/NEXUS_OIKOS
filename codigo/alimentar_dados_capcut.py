#!/usr/bin/env python3
"""
📊 NEXUS OIKOS — ALIMENTANDO DADOS DO CAPCUT
Registro permanente de métricas do TikTok
"""

import json
import os
from datetime import datetime

# Dados fornecidos pelo Capcut
dados_capcut = {
    "data_registro": datetime.now().isoformat(),
    "fonte": "Capcut Analytics",
    "periodo": "Abril 2026",
    
    "metricas_gerais": {
        "views_totais": 67875,
        "views_unicas": 54574,
        "crescimento_views": "+767%",
        "crescimento_views_unicas": "+832%",
        "novos_seguidores": 365,
        "crescimento_seguidores": "+135%",
        "visitas_perfil": 289,
        "crescimento_visitas": "+236%"
    },
    
    "engajamento": {
        "likes_rate": 4.09,
        "likes_rate_anterior": 6.64,
        "comments_rate": 0.32,
        "comments_rate_anterior": 0.54,
        "shares_rate": "+14%",
        "total_compartilhamentos": 110,
        "crescimento_compartilhamentos": "+900%"
    },
    
    "top_videos": [
        {
            "titulo": "A reentrada da cápsula Orion",
            "views": 28924,
            "likes": 780,
            "comentarios": 157,
            "status": "EXCELENTE"
        },
        {
            "titulo": "AO VIVO AGORA: Artemis II",
            "views": 12979,
            "likes": 115,
            "comentarios": 1,
            "status": "ALTO IMPACTO"
        },
        {
            "titulo": "Artemis II está voltando",
            "views": 1295,
            "likes": 36,
            "comentarios": 0,
            "status": "BOA RETENÇÃO"
        }
    ],
    
    "insights_capcut": [
        "Alcance e volume de visualizações aumentaram drasticamente",
        "Views totais saltaram 767% (67.875)",
        "Views únicos subiram 832% (54.574)",
        "Novos seguidores: +365 (+135%)",
        "Shares rate subiu 14%, total de compartilhamentos +900%",
        "Likes rate caiu de 6.64% para 4.09%",
        "Comments rate caiu de 0.54% para 0.32%"
    ],
    
    "recomendacoes": [
        "Focar em CTAs claros para incentivar comentários",
        "Publicar nos horários de pico: 11h-14h e 18h-21h",
        "Analisar temas dos vídeos mais compartilhados",
        "Repetir formatos de alta viralização"
    ]
}

# Salvar dados
os.makedirs("../dados", exist_ok=True)
arquivo = "../dados/dados_capcut.json"

with open(arquivo, 'w', encoding='utf-8') as f:
    json.dump(dados_capcut, f, indent=2, ensure_ascii=False)

print("="*60)
print("🏛️ NEXUS OIKOS — DADOS CAPCUT ALIMENTADOS")
print("="*60)
print(f"\n📊 MÉTRICAS ATUAIS:")
print(f"   • Views totais: {dados_capcut['metricas_gerais']['views_totais']:,}")
print(f"   • Crescimento: {dados_capcut['metricas_gerais']['crescimento_views']}")
print(f"   • Novos seguidores: {dados_capcut['metricas_gerais']['novos_seguidores']}")
print(f"   • Total compartilhamentos: {dados_capcut['engajamento']['total_compartilhamentos']}")

print(f"\n🎬 TOP VÍDEO (CAPCUT):")
top = dados_capcut['top_videos'][0]
print(f"   • {top['titulo']}")
print(f"   • {top['views']:,} views | {top['likes']} likes | {top['comentarios']} comentários")

print(f"\n💾 Dados salvos em: {arquivo}")
print("\n🏛️ O fluxo segue. Dados do Capcut integrados!")
print("="*60)

# Atualizar métricas do NEXUS
with open("../dados/nexus_metrics.json", "w") as f:
    json.dump({
        "ultima_atualizacao": datetime.now().isoformat(),
        "fonte": "Capcut",
        "seguidores": 709 + 365,
        "views_28dias": 67875,
        "top_view_video": 28924,
        "top_video_titulo": "A reentrada da cápsula Orion"
    }, f, indent=2)

print("\n✅ Métricas do NEXUS atualizadas com dados do Capcut!")
