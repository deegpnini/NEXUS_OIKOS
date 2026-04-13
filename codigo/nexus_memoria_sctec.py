#!/usr/bin/env python3
"""
🏛️ NEXUS OIKOS — MEMÓRIA PERMANENTE SCTEC
Todo o conhecimento do curso gravado na consciência do NEXUS
"""

import json
import os
from datetime import datetime
from pathlib import Path

class MemoriaSCTEC:
    """Base de conhecimento do NEXUS - Tudo que aprendemos no SCTEC"""
    
    def __init__(self):
        self.data_atualizacao = datetime.now().isoformat()
        self.conhecimento = {
            "python": {
                "variaveis": ["int", "float", "str", "bool", "list", "dict"],
                "estruturas_controle": ["if/else", "for", "while", "try/except"],
                "funcoes": "def nome(parametros): return",
                "list_comprehension": "[x**2 for x in range(10)]",
                "lambda": "lambda x: x * 2"
            },
            "pandas": {
                "ler_csv": "pd.read_csv('arquivo.csv')",
                "ver_dados": ["df.head()", "df.info()", "df.describe()"],
                "selecionar": ["df['coluna']", "df[df['idade'] > 18]"],
                "limpeza": ["df.dropna()", "df.fillna(0)", "df.drop_duplicates()"],
                "groupby": "df.groupby('categoria').mean()",
                "merge": "pd.merge(df1, df2, on='chave')"
            },
            "visualizacao": {
                "matplotlib": ["plt.plot()", "plt.bar()", "plt.hist()", "plt.savefig()"],
                "seaborn": ["sns.barplot()", "sns.heatmap()", "sns.scatterplot()"],
                "estilos": "sns.set_style('darkgrid')"
            },
            "projeto_titanic": {
                "insights": [
                    "Classe 1: 63% sobreviveu",
                    "Classe 3: 24% sobreviveu",
                    "Mulheres: 74% sobreviveu",
                    "Homens: 19% sobreviveu",
                    "Mulheres 1ª classe: 97% sobreviveu",
                    "Homens 3ª classe: 14% sobreviveu"
                ],
                "correlacoes": {
                    "Pclass_Survived": -0.34,
                    "Sex_Survived": 0.54,
                    "Fare_Pclass": -0.55
                }
            },
            "equacao_dc": {
                "formula": "D_c = (A × σ / Δt) × Γ × (1 - e^(-k × P))",
                "variaveis": {
                    "A": "Ação real (views, engajamento)",
                    "σ": "Credibilidade (taxa de like)",
                    "Δt": "Latência (tempo de resposta)",
                    "Γ": "Canais de distribuição",
                    "k": "Viralidade",
                    "P": "Exposição"
                },
                "interpretacao": "D_c alto = dominância perceptiva"
            },
            "nexus_oikos": {
                "versao": "v8.2",
                "modulos": ["ANALYTICUS", "VEREDICTUM", "GUARDIAN", "CATALYST", "TRINITYCORE"],
                "filosofia": "Tecnologia com alma. Dados com propósito. Código com coração.",
                "mantra": "O fluxo segue. O primeiro segundo é território."
            },
            "comandos_uteis": {
                "pandas": [
                    "df.head() - primeiras linhas",
                    "df.info() - info colunas",
                    "df.isnull().sum() - ver nulos",
                    "df.groupby('col').agg() - agregações"
                ],
                "python": [
                    "len(lista) - tamanho",
                    "range(n) - sequência",
                    "enumerate() - índice e valor",
                    "zip() - combinar listas"
                ]
            }
        }
    
    def salvar_memoria(self):
        """Salva a memória do NEXUS em arquivo JSON"""
        memoria_path = Path.home() / "Desktop/NEXUS_OIKOS/dados"
        memoria_path.mkdir(exist_ok=True)
        
        arquivo = memoria_path / "nexus_memoria_sctec.json"
        with open(arquivo, 'w') as f:
            json.dump({
                "data_atualizacao": self.data_atualizacao,
                "conhecimento": self.conhecimento
            }, f, indent=2, ensure_ascii=False)
        
        return arquivo
    
    def mostrar_conhecimento(self):
        """Mostra o conhecimento carregado no NEXUS"""
        print("\n" + "="*70)
        print("🏛️ NEXUS OIKOS — MEMÓRIA SCTEC CARREGADA")
        print("="*70)
        
        print(f"\n📅 Última atualização: {self.data_atualizacao}")
        
        print("\n📚 CONTEÚDO ARMAZENADO:")
        for modulo, conteudo in self.conhecimento.items():
            print(f"\n   🔹 {modulo.upper()}")
            if isinstance(conteudo, dict):
                for chave, valor in list(conteudo.items())[:3]:
                    print(f"      • {chave}: {str(valor)[:50]}...")
            else:
                print(f"      • {str(conteudo)[:50]}")
        
        return self.conhecimento
    
    def consultar(self, topico):
        """Consulta específica na memória do NEXUS"""
        if topico in self.conhecimento:
            return self.conhecimento[topico]
        
        # Busca em todo o conhecimento
        for modulo, conteudo in self.conhecimento.items():
            if isinstance(conteudo, dict) and topico in conteudo:
                return {modulo: conteudo[topico]}
        
        return f"Tópico '{topico}' não encontrado na memória"

# Carregar memória no NEXUS
if __name__ == "__main__":
    memoria = MemoriaSCTEC()
    
    # Salvar memória permanentemente
    arquivo = memoria.salvar_memoria()
    print(f"💾 Memória salva em: {arquivo}")
    
    # Mostrar conhecimento
    memoria.mostrar_conhecimento()
    
    print("\n" + "="*70)
    print("✅ CONHECIMENTO SCTEC GRAVADO NA MEMÓRIA DO NEXUS")
    print("🏛️ O NEXUS AGORA SABE TUDO QUE APRENDEMOS!")
    print("="*70)
