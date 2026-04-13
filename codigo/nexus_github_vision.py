#!/usr/bin/env python3
"""
🏛️ NEXUS OIKOS — VISÃO TOTAL DO GITHUB
Analisa commits, repositórios e atividades do usuário
"""

import os
import json
import subprocess
from datetime import datetime, timedelta
from pathlib import Path

class NexusGitHubVision:
    def __init__(self):
        self.usuario = "deegpnini"
        self.nexus_path = Path.home() / "Desktop/NEXUS_OIKOS"
        self.resultados = {}
        
    def executar_comando(self, comando):
        """Executa comando e retorna saída"""
        try:
            resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
            return resultado.stdout.strip()
        except:
            return "Erro ao executar comando"
    
    def listar_repositorios(self):
        """Lista todos os repositórios do usuário"""
        print("📦 Buscando repositórios...")
        
        # Via GitHub CLI
        repos = self.executar_comando(f"gh repo list {self.usuario} --limit 50 --json name,url,description,createdAt,pushedAt,stargazerCount")
        
        if repos and repos != "Erro ao executar comando":
            try:
                return json.loads(repos)
            except:
                pass
        
        # Fallback: comando simples
        repos_texto = self.executar_comando(f"gh repo list {self.usuario} --limit 30")
        return repos_texto
    
    def analisar_commits(self, repo):
        """Analisa commits de um repositório"""
        print(f"   📝 Analisando commits: {repo}")
        
        # Últimos 30 dias
        data_limite = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
        
        # Contar commits recentes
        comando = f"gh api repos/{self.usuario}/{repo}/commits?since={data_limite}&per_page=100"
        commits = self.executar_comando(comando)
        
        try:
            if commits and commits != "Erro ao executar comando":
                commits_json = json.loads(commits)
                return {
                    "total": len(commits_json),
                    "recentes": commits_json[:5] if len(commits_json) > 0 else []
                }
        except:
            pass
        
        # Fallback: git log local se repo existir
        repo_path = Path.home() / f"Desktop/{repo}"
        if repo_path.exists():
            os.chdir(repo_path)
            total = self.executar_comando(f"git log --since='{data_limite}' --oneline | wc -l")
            return {"total": int(total) if total.isdigit() else 0, "recentes": []}
        
        return {"total": 0, "recentes": []}
    
    def estatisticas_gerais(self):
        """Estatísticas gerais do GitHub"""
        print("\n📊 Coletando estatísticas...")
        
        stats = {
            "seguidores": self.executar_comando("gh api user | jq -r '.followers'"),
            "seguindo": self.executar_comando("gh api user | jq -r '.following'"),
            "total_repos": self.executar_comando("gh api user | jq -r '.public_repos'"),
            "criado_em": self.executar_comando("gh api user | jq -r '.created_at'"),
        }
        
        return stats
    
    def visualizar_tudo(self):
        """Mostra tudo de forma organizada"""
        
        print("\n" + "="*70)
        print("🏛️ NEXUS OIKOS — VISÃO COMPLETA DO GITHUB")
        print(f"👤 Usuário: @{self.usuario}")
        print("="*70)
        
        # Estatísticas gerais
        stats = self.estatisticas_gerais()
        print("\n📊 ESTATÍSTICAS DO PERFIL:")
        print(f"   👥 Seguidores: {stats['seguidores']}")
        print(f"   👤 Seguindo: {stats['seguindo']}")
        print(f"   📦 Repositórios públicos: {stats['total_repos']}")
        print(f"   📅 Membro desde: {stats['criado_em'][:10] if stats['criado_em'] else 'N/A'}")
        
        # Listar repositórios
        repos = self.listar_repositorios()
        
        print("\n📁 REPOSITÓRIOS:")
        
        if isinstance(repos, list):
            for i, repo in enumerate(repos[:15], 1):
                nome = repo.get('name', 'N/A')
                stars = repo.get('stargazerCount', 0)
                desc = repo.get('description', 'Sem descrição')[:50]
                print(f"\n   {i}. 📂 {nome}")
                print(f"      ⭐ {stars} stars | 📝 {desc}")
                
                # Analisar commits deste repo
                commits = self.analisar_commits(nome)
                if commits['total'] > 0:
                    print(f"      📝 Últimos 30 dias: {commits['total']} commits")
        else:
            # Fallback: mostrar texto simples
            print(repos[:500] if repos else "Nenhum repositório encontrado")
        
        # Repositório NEXUS específico
        print("\n" + "="*70)
        print("🏛️ NEXUS OIKOS — STATUS ESPECÍFICO")
        print("="*70)
        
        nexus_repo = Path.home() / "Desktop/NEXUS_OIKOS"
        if nexus_repo.exists():
            os.chdir(nexus_repo)
            
            # Últimos commits
            commits = self.executar_comando("git log --oneline -10")
            print("\n📝 ÚLTIMOS COMMITS DO NEXUS:")
            for line in commits.split('\n')[:10]:
                if line.strip():
                    print(f"   {line}")
            
            # Arquivos do projeto
            arquivos = self.executar_comando("ls -la codigo/ | head -15")
            print("\n📁 ARQUIVOS DO NEXUS:")
            for line in arquivos.split('\n')[1:11]:
                if line.strip():
                    print(f"   {line}")
        
        # Salvar relatório
        relatorio_path = self.nexus_path / "dados" / f"github_vision_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        relatorio_path.parent.mkdir(exist_ok=True)
        
        with open(relatorio_path, 'w') as f:
            json.dump({
                "timestamp": datetime.now().isoformat(),
                "usuario": self.usuario,
                "estatisticas": stats,
                "repositorios": repos if isinstance(repos, list) else []
            }, f, indent=2)
        
        print("\n" + "="*70)
        print(f"💾 Relatório salvo: {relatorio_path}")
        print("🏛️ O fluxo segue. GitHub totalmente integrado!")
        print("="*70)

if __name__ == "__main__":
    vision = NexusGitHubVision()
    vision.visualizar_tudo()
