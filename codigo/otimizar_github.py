#!/usr/bin/env python3
"""
🛠️ NEXUS OIKOS — OTIMIZADOR DE REPOSITÓRIOS
"""

import subprocess
import json
from pathlib import Path

repos = [
    "NEXUS_OIKOS",
    "trinity-xai-exoplanets", 
    "trinity-quantum-memory-system",
    "TriNyTy-D7D-Nexus-GuardiaN",
    "TorreHebron"
]

def verificar_repo(repo):
    print(f"\n📦 Analisando: {repo}")
    
    # Verifica se repo existe localmente
    repo_path = Path.home() / f"Desktop/{repo}"
    
    if repo_path.exists():
        os.chdir(repo_path)
        
        # Último commit
        last_commit = subprocess.run("git log -1 --oneline", shell=True, capture_output=True, text=True).stdout.strip()
        print(f"   📝 Último commit: {last_commit[:50]}")
        
        # Verifica remote
        remote = subprocess.run("git remote -v", shell=True, capture_output=True, text=True).stdout.strip()
        if remote:
            print(f"   🔗 Remote configurado")
        else:
            print(f"   ❌ Sem remote - precisa configurar")
    else:
        print(f"   ⚠️ Repositório não encontrado localmente")
        print(f"   🔧 Clone com: gh repo clone deegpnini/{repo}")

if __name__ == "__main__":
    print("🏛️ OTIMIZADOR NEXUS")
    for repo in repos:
        verificar_repo(repo)
