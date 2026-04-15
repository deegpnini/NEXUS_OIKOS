"""
📊 NEXUS OIKOS — PROCESSADOR EM LOTE
Analisa todos os vídeos do histórico de uma vez
"""

import json
import sys
from nexus_core_ml import NEXUS_OIKOS

def processar_historico():
    nexus = NEXUS_OIKOS()
    
    # Dados reais dos seus vídeos
    videos = [
        {"nome": "Reentrada da Orion", "views": 28924, "likes": 780, "coments": 157, "compart": 110},
        {"nome": "Artemis Ao Vivo", "views": 12979, "likes": 115, "coments": 1, "compart": 0},
        {"nome": "Artemis Voltando", "views": 1295, "likes": 36, "coments": 0, "compart": 0},
    ]
    
    print("\n" + "="*50)
    print("🏛️ NEXUS OIKOS — ANALISANDO HISTÓRICO")
    print("="*50)
    
    i = 0
    total_dc = 0
    
    while i < len(videos):
        v = videos[i]
        resultado = nexus.calcular_dc_video(v["views"], v["likes"], v["coments"], v["compart"])
        total_dc += resultado["d_c"]
        
        print(f"\n📹 {i+1}. {v['nome']}")
        print(f"   Views: {v['views']:,}")
        print(f"   D_c: {resultado['d_c']}")
        print(f"   Classificação: {resultado['classificacao']}")
        
        i += 1
    
    print("\n" + "="*50)
    print(f"📊 RESUMO:")
    print(f"   Total de vídeos: {len(videos)}")
    print(f"   D_c médio: {total_dc/len(videos):.4f}")
    print("="*50)
    print("🏛️ O fluxo segue!")

if __name__ == "__main__":
    processar_historico()
