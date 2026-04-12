"""
🛡️ NEXUS EXPLORER — MONITOR AUTOMÁTICO
Fica vigiando novos arquivos
"""

import time
import os
import sys
from datetime import datetime

class ExplorerAutomatico:
    def __init__(self):
        self.watch_path = "../dados"
        self.processados = set()
        
    def monitorar(self):
        print(f"🛡️ Explorer ativo - monitorando: {self.watch_path}")
        print("   Aguardando novos arquivos... (Ctrl+C para parar)\n")
        
        os.makedirs(self.watch_path, exist_ok=True)
        
        try:
            while True:
                # Lista arquivos na pasta
                for arquivo in os.listdir(self.watch_path):
                    if arquivo.endswith('.csv') and arquivo not in self.processados:
                        self.processados.add(arquivo)
                        print(f"\n📄 NOVO ARQUIVO DETECTADO: {arquivo}")
                        print(f"   ⏰ {datetime.now().strftime('%H:%M:%S')}")
                        print(f"   📊 Pronto para análise NEXUS")
                
                time.sleep(5)  # Verifica a cada 5 segundos
                
        except KeyboardInterrupt:
            print("\n🛡️ Explorer encerrado")

if __name__ == "__main__":
    explorer = ExplorerAutomatico()
    explorer.monitorar()
