"""
🏛️ NEXUS OIKOS — ANÁLISE DO PERFIL @nexus_oikos
Dados reais de 09 de Abril de 2026
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

class AnaliseNexusOikos:
    def __init__(self):
        self.perfil = "@nexus_oikos"
        self.data_analise = datetime.now()
        
        # Dados do perfil
        self.dados_perfil = {
            "seguidores": 552,
            "seguindo": 921,
            "curtidas_total": 2372,
            "views_semana": 7250,
            "crescimento_seguidores": 55.5,
            "crescimento_views": 477.0
        }
        
        # Dados dos vídeos
        self.videos = [
            {"titulo": "Radiação Estelar Estranha", "views": 1072, "likes": 65, "coments": 4, "compart": 2},
            {"titulo": "Não virou notícia... mas deveria", "views": 926, "likes": 55, "coments": 4, "compart": 1},
            {"titulo": "GREVE DOS CAMINHONEIROS", "views": 925, "likes": 73, "coments": 4, "compart": 2},
        ]
        
        # Origem de tráfego
        self.trafego = {
            "Para Você": 98.2,
            "Perfil pessoal": 1.2,
            "Seguindo": 0.3,
            "Pesquisar": 0.3
        }
        
        # Termos pesquisados
        self.termos = [
            ("frequência 528 hertz", 10.0),
            ("foto ia em santa catarina", 5.0),
            ("qual é o país que chove diamante", 5.0),
            ("os estres terrestres", 5.0)
        ]
    
    def calcular_dc(self, views, likes, compart):
        """Calcula D_c para cada vídeo"""
        taxa_like = likes / max(views, 1)
        dc = (views / 10000) * taxa_like * (1 + compart/max(views,1))
        return min(dc, 1.0)  # Cap em 1.0
    
    def analisar(self):
        print("\n" + "="*60)
        print(f"🏛️ NEXUS OIKOS — ANÁLISE DO {self.perfil}")
        print(f"📅 {self.data_analise.strftime('%d/%m/%Y %H:%M')}")
        print("="*60)
        
        # Perfil
        print("\n📊 MÉTRICAS DO PERFIL:")
        print(f"   👥 Seguidores: {self.dados_perfil['seguidores']}")
        print(f"   📈 Crescimento: +{self.dados_perfil['crescimento_seguidores']}%")
        print(f"   👁️ Views semana: {self.dados_perfil['views_semana']:,}")
        print(f"   🚀 Crescimento views: +{self.dados_perfil['crescimento_views']}%")
        print(f"   ❤️ Curtidas totais: {self.dados_perfil['curtidas_total']:,}")
        
        # Vídeos
        print("\n🎬 TOP VÍDEOS:")
        for v in self.videos:
            dc = self.calcular_dc(v['views'], v['likes'], v['compart'])
            engajamento = (v['likes'] / v['views']) * 100
            print(f"\n   📹 {v['titulo']}")
            print(f"      Views: {v['views']:,} | Likes: {v['likes']} ({engajamento:.2f}%)")
            print(f"      D_c: {dc:.6f}")
        
        # Tráfego
        print("\n📡 ORIGEM DO TRÁFEGO:")
        for origem, percent in self.trafego.items():
            barra = "█" * int(percent / 2)
            print(f"   {origem}: {barra} {percent}%")
        
        # Termos
        print("\n🔍 TERMOS MAIS PESQUISADOS:")
        for termo, percent in self.termos:
            print(f"   • {termo}: {percent}%")
        
        # Insights
        print("\n" + "="*60)
        print("🎯 INSIGHTS ESTRATÉGICOS:")
        print("="*60)
        print("""
1. 🔥 O ALGORITMO TE AMA: 98.2% vem do 'Para Você'
   → Continue postando, o TikTok está te empurrando

2. 📈 CRESCIMENTO EXPLOSIVO: +477% views, +55% seguidores
   → Você está num momento de inflexão

3. ⚠️ ENGAJAMENTO EM QUEDA: Novo público não interage
   → Adicione CALLS TO ACTION: "Curta se concorda!"

4. 🎯 NICHO DESCOBERTO: Frequência 528Hz é seu termo mais buscado
   → Faça uma série sobre sons e frequências

5. 🕐 HORÁRIO OURO: Teste postagens entre 18h-20h
   → É quando o brasileiro está mais ativo

6. 📹 SEU FORMATO VIRAL: Temas misteriosos e atuais
   → "O que não virou notícia" pode ser sua série principal
""")
        
        # Recomendações
        print("\n" + "="*60)
        print("🚀 RECOMENDAÇÕES NEXUS:")
        print("="*60)
        print("""
✅ FAZER AMANHÃ:
   • Criar vídeo sobre "Frequência 528Hz - O que a ciência diz?"
   • Adicionar legenda: "Comente sua experiência com essa frequência"
   • Postar às 18:30

✅ FAZER ESTA SEMANA:
   • Série "O que não virou notícia #2"
   • Vídeo respondendo comentários (engaja a comunidade)
   • Stories com bastidores

✅ FAZER NO PRÓXIMO MÊS:
   • Live sobre "Ciência e Consciência"
   • Parceria com outro criador do nicho
   • Playlist "Mistérios do Cosmos"
""")
        
        # Gerar gráfico
        self.gerar_grafico()
        
        return True
    
    def gerar_grafico(self):
        """Gera visualização dos dados"""
        
        fig, axes = plt.subplots(2, 2, figsize=(12, 10))
        fig.suptitle(f'NEXUS OIKOS — Análise do {self.perfil}', fontsize=14, fontweight='bold')
        
        # Gráfico 1: Views vs Likes
        titulos = [v['titulo'][:20] for v in self.videos]
        views = [v['views'] for v in self.videos]
        likes = [v['likes'] for v in self.videos]
        
        x = np.arange(len(titulos))
        width = 0.35
        axes[0,0].bar(x - width/2, views, width, label='Views', color='teal')
        axes[0,0].bar(x + width/2, likes, width, label='Likes', color='orange')
        axes[0,0].set_xlabel('Vídeos')
        axes[0,0].set_ylabel('Quantidade')
        axes[0,0].set_title('Views vs Likes')
        axes[0,0].set_xticks(x)
        axes[0,0].set_xticklabels(titulos, rotation=45, ha='right')
        axes[0,0].legend()
        
        # Gráfico 2: Origem do tráfego
        origens = list(self.trafego.keys())
        percentuais = list(self.trafego.values())
        axes[0,1].pie(percentuais, labels=origens, autopct='%1.1f%%', startangle=90)
        axes[0,1].set_title('Origem do Tráfego')
        
        # Gráfico 3: Taxa de engajamento
        engajamento = [(v['likes']/v['views'])*100 for v in self.videos]
        axes[1,0].bar(titulos, engajamento, color='coral')
        axes[1,0].axhline(y=sum(engajamento)/len(engajamento), color='red', linestyle='--', label=f'Média: {sum(engajamento)/len(engajamento):.2f}%')
        axes[1,0].set_ylabel('Taxa de Engajamento (%)')
        axes[1,0].set_title('Engajamento por Vídeo')
        axes[1,0].set_xticklabels(titulos, rotation=45, ha='right')
        axes[1,0].legend()
        
        # Gráfico 4: D_c dos vídeos
        dc_values = [self.calcular_dc(v['views'], v['likes'], v['compart']) for v in self.videos]
        axes[1,1].bar(titulos, dc_values, color='purple')
        axes[1,1].set_ylabel('D_c (Dominância Perceptiva)')
        axes[1,1].set_title('D_c por Vídeo')
        axes[1,1].set_xticklabels(titulos, rotation=45, ha='right')
        axes[1,1].axhline(y=sum(dc_values)/len(dc_values), color='red', linestyle='--', label=f'Média: {sum(dc_values)/len(dc_values):.4f}')
        axes[1,1].legend()
        
        plt.tight_layout()
        plt.savefig('../midia/analise_nexus_oikos.png', dpi=150)
        print("\n✅ Gráfico salvo em: ../midia/analise_nexus_oikos.png")
        plt.close()

if __name__ == "__main__":
    analise = AnaliseNexusOikos()
    analise.analisar()
