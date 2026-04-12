"""
🕊️ NEXUS SOCIAL — CONTEÚDO PRONTO PARA VIRALIZAR
"""

import json
import random
from datetime import datetime

class SocialAutomatico:
    def __init__(self):
        self.hashtags = "#NexusOikos #TrinityCore #IA #Tecnologia #Inovação #OPrimeiroSegundo"
        
    def gerar_conteudo(self, d_c=0.068):
        posts = {
            "tiktok": f"🏛️ D_c calculado: {d_c}\nO primeiro segundo é território!\n#NexusOikos",
            
            "instagram": f"📊 Análise NEXUS OIKOS\nD_c = {d_c}\n\nTecnologia com alma. Dados com propósito.\n\n{self.hashtags}",
            
            "twitter": f"D_c = {d_c}\nO fluxo segue. 🏛️💚\n#NexusOikos"
        }
        
        # Salva conteúdo
        with open('../midia/conteudo_social.json', 'w') as f:
            json.dump(posts, f, indent=2)
        
        print("\n🕊️ CONTEÚDO GERADO PARA REDES SOCIAIS:")
        print("="*50)
        for plataforma, texto in posts.items():
            print(f"\n📱 {plataforma.upper()}:")
            print(f"   {texto[:100]}...")
        
        print(f"\n💾 Conteúdo salvo em ../midia/conteudo_social.json")
        return posts

if __name__ == "__main__":
    social = SocialAutomatico()
    social.gerar_conteudo(0.068)
    print("\n🏛️ Pronto para postar. O fluxo segue.")
