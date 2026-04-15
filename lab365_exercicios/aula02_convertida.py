"""
🏛️ AULA 02 SCTEC — CONVERTIDA PARA PYTHON
Lógica de Programação aplicada ao NEXUS
"""

print("="*50)
print("🏛️ AULA 02 — CÓDIGOS CONVERTIDOS")
print("="*50)

# 1. FILTRO DE VERDADE (if/else)
print("\n1. FILTRO DE VERDADE (if/else):")

def validar_objeto_espacial(tamanho):
    if type(tamanho) is not float:
        return "⚠️ Erro: Formato inválido"
    elif tamanho > 100.0:
        return "🚨 ALERTA: Objeto Massivo Detectado!"
    else:
        return "✅ Objeto Monitorado"

print(f"   Asteroide 50m: {validar_objeto_espacial(50.0)}")
print(f"   Asteroide 150m: {validar_objeto_espacial(150.0)}")

# 2. ROTEADOR DE AÇÕES (match/case)
print("\n2. ROTEADOR DE AÇÕES (match/case):")

def menu_nexus(comando):
    match comando:
        case "1":
            return "🚀 Ativando Radar NEXUS-ISO"
        case "2":
            return "📊 Calculando D_c do TikTok"
        case "3":
            return "💾 Sincronizando com GitHub"
        case _:
            return "❌ Comando não reconhecido"

print(f"   Comando 1: {menu_nexus('1')}")
print(f"   Comando 2: {menu_nexus('2')}")
print(f"   Comando X: {menu_nexus('X')}")

# 3. MOTOR DE AUTOMATIZAÇÃO (while)
print("\n3. MOTOR DE AUTOMATIZAÇÃO (while):")

def processar_videos(lista_videos):
    i = 0
    print("   Processando vídeos...")
    while i < len(lista_videos):
        print(f"   • Vídeo {i+1}: {lista_videos[i]['nome']} - {lista_videos[i]['views']} views")
        i += 1
    print("   ✅ Processamento concluído!")

videos_teste = [
    {"nome": "Orion Reentrada", "views": 28924},
    {"nome": "Artemis Ao Vivo", "views": 12979},
    {"nome": "Cápsula Voltando", "views": 1295}
]
processar_videos(videos_teste)

print("\n" + "="*50)
print("🏛️ Códigos convertidos com sucesso!")
