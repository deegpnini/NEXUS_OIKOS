#!/usr/bin/env python3
"""
🛡️ NEXUS SENTINEL — Monitor e Protetor do Sistema
Hardware Raiz — Vigilância Contínua
"""

import os
import sys
import json
import time
import platform
import subprocess
from datetime import datetime
from pathlib import Path

try:
    import psutil
except ImportError:
    print("⚠️ psutil não instalado. Instalando...")
    subprocess.run([sys.executable, "-m", "pip", "install", "psutil", "--quiet"])
    import psutil

class NexusSentinel:
    def __init__(self):
        self.nexus_path = Path.home() / "Desktop/NEXUS_OIKOS"
        self.log_path = self.nexus_path / "logs"
        self.log_path.mkdir(exist_ok=True)
        
        self.os_info = platform.uname()
        self.boot_time = datetime.now()
        
    def health_check(self):
        """Verifica saúde do sistema"""
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory()
        disco = psutil.disk_usage('/')
        
        status = {
            "timestamp": datetime.now().isoformat(),
            "cpu_percent": cpu,
            "ram_percent": ram.percent,
            "ram_used_gb": ram.used / (1024**3),
            "disk_percent": disco.percent,
            "disk_free_gb": disco.free / (1024**3),
            "temperatura": self._get_temperature()
        }
        
        # Alertas
        alertas = []
        if cpu > 80:
            alertas.append(f"⚠️ CPU alta: {cpu}%")
        if ram.percent > 90:
            alertas.append(f"⚠️ RAM crítica: {ram.percent}%")
        if disco.percent > 90:
            alertas.append(f"⚠️ Disco quase cheio: {disco.percent}%")
        
        return status, alertas
    
    def _get_temperature(self):
        """Tenta obter temperatura do sistema"""
        try:
            with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
                return float(f.read()) / 1000
        except:
            return None
    
    def create_file(self, nome, extensao, conteudo=""):
        """Cria arquivo em qualquer formato"""
        filename = f"{nome}.{extensao}"
        filepath = self.nexus_path / "codigo" / filename
        
        with open(filepath, "w") as f:
            f.write(conteudo)
        
        print(f"✅ Arquivo criado: {filename}")
        return str(filepath)
    
    def create_json(self, nome, dados):
        """Cria arquivo JSON"""
        return self.create_file(nome, "json", json.dumps(dados, indent=2))
    
    def create_markdown(self, nome, conteudo):
        """Cria arquivo Markdown"""
        return self.create_file(nome, "md", conteudo)
    
    def log_evento(self, evento, detalhes=""):
        """Registra evento no log"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "evento": evento,
            "detalhes": detalhes
        }
        
        log_file = self.log_path / f"{datetime.now().strftime('%Y%m%d')}_eventos.json"
        
        if log_file.exists():
            with open(log_file, 'r') as f:
                logs = json.load(f)
        else:
            logs = []
        
        logs.append(log_entry)
        
        with open(log_file, 'w') as f:
            json.dump(logs, f, indent=2)
        
        return log_entry
    
    def monitorar_processos(self, nome_processo=None):
        """Monitora processos em execução"""
        processos = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            try:
                info = proc.info
                if nome_processo and nome_processo.lower() in info['name'].lower():
                    processos.append(info)
                elif not nome_processo:
                    processos.append(info)
            except:
                pass
        
        return processos
    
    def status_completo(self):
        """Retorna status completo do sistema"""
        status, alertas = self.health_check()
        
        print("\n" + "="*60)
        print("🛡️ NEXUS SENTINEL — STATUS DO SISTEMA")
        print("="*60)
        print(f"📅 Timestamp: {status['timestamp']}")
        print(f"💻 Sistema: {self.os_info.system} {self.os_info.release}")
        print(f"🔧 CPU: {status['cpu_percent']}%")
        print(f"🧠 RAM: {status['ram_percent']}% ({status['ram_used_gb']:.1f} GB usado)")
        print(f"💾 Disco: {status['disk_percent']}% ({status['disk_free_gb']:.1f} GB livre)")
        if status['temperatura']:
            print(f"🌡️ Temperatura: {status['temperatura']:.1f}°C")
        
        if alertas:
            print("\n⚠️ ALERTAS:")
            for alerta in alertas:
                print(f"   {alerta}")
        else:
            print("\n✅ SISTEMA SAUDÁVEL — Sem alertas")
        
        print("="*60)
        return status

def main():
    sentinel = NexusSentinel()
    
    if len(sys.argv) > 1:
        comando = sys.argv[1]
        
        if comando == "health":
            sentinel.status_completo()
        elif comando == "processos":
            processos = sentinel.monitorar_processos()
            print(f"\n📊 Processos em execução: {len(processos)}")
        elif comando == "log":
            sentinel.log_evento("consulta_manual", "Status verificado via terminal")
            print("✅ Evento registrado")
        else:
            print(f"❌ Comando desconhecido: {comando}")
    else:
        sentinel.status_completo()

if __name__ == "__main__":
    main()
