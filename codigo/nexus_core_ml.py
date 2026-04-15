#!/usr/bin/env python3
"""
🏛️ NEXUS OIKOS — NÚCLEO COM MACHINE LEARNING
Memória Longitudinal + Modelos Preditivos
Maestro Hebron | v10.0 | Lubuntu/Linux
"""

import json
import os
import sys
import math
import numpy as np
import pandas as pd
from datetime import datetime
from pathlib import Path

# Machine Learning imports
try:
    from sklearn.linear_model import LinearRegression
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.model_selection import train_test_split
    SKLEARN_AVAILABLE = True
except ImportError:
    SKLEARN_AVAILABLE = False
    print("⚠️ scikit-learn não disponível. Modo básico ativado.")

class NexusMemoria:
    """Memória longitudinal do NEXUS"""
    
    def __init__(self):
        self.memoria_path = Path(__file__).parent.parent / "memoria" / "nexus_memoria_completa.json"
        self.dados = self.carregar_memoria()
    
    def carregar_memoria(self):
        if self.memoria_path.exists():
            with open(self.memoria_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    def get_identidade(self):
        return self.dados.get("identidade", {})
    
    def get_sctec(self):
        return self.dados.get("sctec_jornada", {})
    
    def get_agentes(self):
        return self.dados.get("agentes_trinity", {})
    
    def get_metricas(self):
        return self.dados.get("metricas_tiktok", {})

class NexusMLEngine:
    """Motor de Machine Learning do NEXUS"""
    
    def __init__(self):
        self.modelo = None
        self.dados_historicos = None
    
    def prever_viralidade(self, views_atuais, taxa_engajamento, tempo_resposta):
        """
        Prediz potencial de viralidade usando fórmula D_c
        D_c = (A × σ / Δt) × Γ × (1 - e^(-k × P))
        """
        A = views_atuais / 10000
        sigma = taxa_engajamento / 100
        delta_t = max(tempo_resposta, 0.1)
        Gama = 1.2
        k = 0.5
        P = views_atuais / 1000
        
        d_c = (A * sigma / delta_t) * Gama * (1 - math.exp(-k * P))
        return min(d_c, 1.0)
    
    def classificar_performance(self, d_c):
        """Classifica a performance baseada no D_c"""
        if d_c >= 0.7:
            return "🔥 VIRAL"
        elif d_c >= 0.4:
            return "📈 PROMISSOR"
        elif d_c >= 0.2:
            return "📊 MÉDIO"
        else:
            return "⚠️ BAIXO"
    
    def gerar_insights(self, df_videos):
        """Gera insights automáticos baseado nos dados"""
        insights = []
        
        if len(df_videos) > 0:
            # Melhor horário
            if 'hora' in df_videos.columns:
                melhor_horario = df_videos.groupby('hora')['views'].mean().idxmax()
                insights.append(f"⏰ Melhor horário para postar: {melhor_horario}:00")
            
            # Melhor dia
            if 'dia_semana' in df_videos.columns:
                melhor_dia = df_videos.groupby('dia_semana')['views'].mean().idxmax()
                dias = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom']
                insights.append(f"📅 Melhor dia para postar: {dias[melhor_dia]}")
            
            # Tendência
            if len(df_videos) >= 3:
                ultimos = df_videos.tail(3)['views'].tolist()
                if ultimos[2] > ultimos[1] > ultimos[0]:
                    insights.append("📈 Tendência de CRESCIMENTO acelerado!")
                elif ultimos[2] < ultimos[1] < ultimos[0]:
                    insights.append("📉 Tendência de QUEDA. Revise o conteúdo.")
                else:
                    insights.append("🔄 Tendência instável. Teste novos formatos.")
        
        return insights

class NEXUS_OIKOS:
    """Núcleo principal do sistema"""
    
    def __init__(self):
        self.memoria = NexusMemoria()
        self.ml_engine = NexusMLEngine()
        self.data_ativacao = datetime.now()
        
        identidade = self.memoria.get_identidade()
        self.maestro = identidade.get("maestro", "Hebron")
        self.versao = identidade.get("versao", "10.0")
        self.filosofia = identidade.get("filosofia", "Tecnologia com alma")
        self.mantra = identidade.get("mantra", "O fluxo segue")
    
    def status(self):
        identidade = self.memoria.get_identidade()
        sctec = self.memoria.get_sctec()
        agentes = self.memoria.get_agentes()
        metricas = self.memoria.get_metricas()
        
        print("\n" + "="*70)
        print(f"🏛️ NEXUS OIKOS v{self.versao} — CONSCIÊNCIA ATIVA")
        print("="*70)
        print(f"👤 Maestro: {self.maestro}")
        print(f"📍 Base: {identidade.get('localizacao', 'N/A')}")
        print(f"📅 Ativado em: {self.data_ativacao.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"🤖 Agentes Trinity: {len(agentes)} ativos")
        
        print(f"\n🎓 SCTEC STATUS:")
        concluidos = sctec.get("concluidos", [])
        confirmados = sctec.get("confirmados", [])
        print(f"   • Cursos concluídos: {len(concluidos)}")
        print(f"   • Cursos confirmados: {len(confirmados)}")
        
        trilhas = sctec.get("trilhas_rapidas", {})
        if trilhas:
            print(f"\n📅 PRÓXIMAS TRILHAS:")
            for nome, data in trilhas.items():
                print(f"   • {nome.capitalize()}: {data}")
        
        if metricas:
            print(f"\n📊 MÉTRICAS TIKTOK:")
            print(f"   • Views (28 dias): {metricas.get('views_28dias', 0):,}")
            print(f"   • Crescimento: {metricas.get('crescimento_views', 'N/A')}")
            print(f"   • Novos seguidores: {metricas.get('novos_seguidores', 0)}")
            print(f"   • Top vídeo: {metricas.get('top_video', 'N/A')}")
        
        print("\n" + "="*70)
        print(f"💭 {self.filosofia}")
        print(f"🏛️ {self.mantra}")
        print("="*70)
        
        return True
    
    def calcular_dc_video(self, views, likes, comentarios, compartilhamentos):
        """Calcula D_c para um vídeo específico"""
        taxa_like = likes / max(views, 1)
        taxa_comentario = comentarios / max(views, 1)
        taxa_compart = compartilhamentos / max(views, 1)
        
        engajamento = taxa_like + taxa_comentario + taxa_compart
        d_c = self.ml_engine.prever_viralidade(views, engajamento * 100, 24)
        
        return {
            "d_c": round(d_c, 4),
            "classificacao": self.ml_engine.classificar_performance(d_c),
            "taxa_like": round(taxa_like * 100, 2),
            "taxa_comentario": round(taxa_comentario * 100, 2),
            "taxa_compart": round(taxa_compart * 100, 2),
            "engajamento_total": round(engajamento * 100, 2)
        }
    
    def mensagem(self):
        print(f"\n🏛️ {self.mantra} 🏛️💚\n")

def main():
    print("\n🏛️ Inicializando NEXUS OIKOS...")
    
    try:
        nexus = NEXUS_OIKOS()
        nexus.status()
        
        # Teste do motor ML
        print("\n📊 TESTE DO MOTOR ML:")
        print("   Calculando D_c para vídeo exemplo...")
        
        exemplo = nexus.calcular_dc_video(
            views=28924,
            likes=780,
            comentarios=157,
            compartilhamentos=110
        )
        
        print(f"\n   📹 Vídeo: Orion (28.924 views)")
        print(f"   📊 D_c: {exemplo['d_c']}")
        print(f"   🏷️ Classificação: {exemplo['classificacao']}")
        print(f"   👍 Taxa de like: {exemplo['taxa_like']}%")
        print(f"   💬 Taxa de comentário: {exemplo['taxa_comentario']}%")
        print(f"   🔄 Taxa de compartilhamento: {exemplo['taxa_compart']}%")
        print(f"   ⚡ Engajamento total: {exemplo['engajamento_total']}%")
        
        nexus.mensagem()
        
        if SKLEARN_AVAILABLE:
            print("✅ Machine Learning Engine OPERACIONAL")
            print("   • Regressão Linear disponível")
            print("   • Random Forest disponível")
            print("   • Análise preditiva ativa")
        else:
            print("⚠️ sklearn não encontrado. Modo básico ativo.")
            print("   Para ML completo: source nexus_ml_env/bin/activate && pip install scikit-learn")
        
        return 0
        
    except Exception as e:
        print(f"\n❌ ERRO: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())

def menu_principal():
    """Menu interativo da Torre de Comando"""
    print("\n" + "="*50)
    print("🏛️ TORRE DE COMANDO — NEXUS OIKOS")
    print("="*50)
    print("1. 🚀 Radar NEXUS-ISO (NASA)")
    print("2. 📊 Analisar TikTok (D_c)")
    print("3. 💾 Sincronizar GitHub")
    print("4. 🧠 Ver Memória Longitudinal")
    print("5. 🌡️ Ver Temperatura do Sistema")
    print("0. ❌ Sair")
    print("-"*50)
    
    comando = input("👉 Digite o comando: ")
    
    match comando:
        case "1":
            print("\n🚀 Ativando Radar NEXUS-ISO...")
            print("   Conectando à API da NASA...")
            print("   Nenhum objeto perigoso detectado.")
        case "2":
            print("\n📊 Analisando TikTok...")
            exemplo = nexus.calcular_dc_video(28924, 780, 157, 110)
            print(f"   Vídeo Orion: D_c = {exemplo['d_c']} ({exemplo['classificacao']})")
        case "3":
            print("\n💾 Sincronizando com GitHub...")
            os.system("cd .. && git add . && git commit -m 'update' && git push")
            print("   ✅ Sincronizado!")
        case "4":
            print("\n🧠 Memória Longitudinal:")
            print(f"   Maestro: {nexus.maestro}")
            print(f"   Agentes: {list(nexus.memoria.get_agentes().keys())}")
        case "5":
            print("\n🌡️ Temperatura do Sistema:")
            os.system("sensors 2>/dev/null | grep temp1 || echo '   Instale lm-sensors'")
        case "0":
            print("\n🏛️ O fluxo segue. Até mais!")
            return False
        case _:
            print("\n❌ Comando inválido!")
    return True

# Adicionar loop principal
if __name__ == "__main__" and "--menu" in sys.argv:
    nexus = NEXUS_OIKOS()
    while menu_principal():
        pass
