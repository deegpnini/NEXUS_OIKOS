"""
📊 NEXUS OIKOS — ANÁLISE AUTOMÁTICA
Executa tudo sozinho, só precisa rodar
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from nexus_core import NEXUS_OIKOS

class AnaliseAutomatica:
    def __init__(self):
        self.nexus = NEXUS_OIKOS()
        print("🏛️ Iniciando análise automática...")
    
    def executar(self):
        print("\n📊 Gerando dados de teste...")
        
        # Cria dados sintéticos
        np.random.seed(42)
        df = pd.DataFrame({
            'timestamp': pd.date_range(start='2026-01-01', periods=10000, freq='H'),
            'engajamento': np.random.exponential(100, 10000),
            'velocidade': np.random.gamma(2, 1, 10000),
            'credibilidade': np.random.beta(2, 5, 10000),
            'viralidade': np.random.beta(1.5, 3, 10000)
        })
        
        # Calcula D_c simplificado
        df['d_c'] = (df['engajamento'] * df['credibilidade'] / df['velocidade'].clip(lower=0.1)) * df['viralidade']
        df['d_c'] = df['d_c'].clip(upper=1)
        
        print(f"✅ {len(df):,} registros analisados")
        print(f"📈 D_c médio: {df['d_c'].mean():.4f}")
        print(f"🔥 D_c máximo: {df['d_c'].max():.4f}")
        
        # Gera gráfico simples
        plt.figure(figsize=(10, 4))
        plt.plot(df['timestamp'][:500], df['d_c'][:500], alpha=0.7, linewidth=0.5, color='teal')
        plt.title('Evolução do D_c - NEXUS OIKOS')
        plt.xlabel('Tempo')
        plt.ylabel('D_c')
        plt.grid(True, alpha=0.3)
        plt.savefig('../midia/analise_automatica.png', dpi=100)
        plt.close()
        
        print("✅ Gráfico salvo em ../midia/analise_automatica.png")
        
        # Salva dados
        df.to_csv('../dados/analise_completa.csv', index=False)
        print("✅ Dados salvos em ../dados/analise_completa.csv")
        
        return df

if __name__ == "__main__":
    analise = AnaliseAutomatica()
    resultados = analise.executar()
    print(f"\n{analise.nexus.mensagem_maestro()}")
