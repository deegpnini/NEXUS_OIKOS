# NEXUS OIKOS / ARCTURUS

"Onde a duvida vira investigacao."

## Sobre o Projeto

Este repositorio contem o ecossistema ARCTURUS, desenvolvido como parte do projeto NEXUS OIKOS.
O sistema integra analise sismica, monitoramento climatico, processamento de imagens SAR
e um pipeline automatizado de videos para redes sociais.

## Estrutura

```
notebooks/
├── SISMICOS/      # Analise sismica com dados USGS
├── CLIMATICOS/    # Dados climaticos (INMET/Open-Meteo)
├── NEXUS_OIKOS/   # Pipeline de producao de videos
├── VISUAL/        # Analise SAR (Sentinel-1)
└── UTILITARIOS/   # Scripts de apoio e testes
```

## Modulos

| Modulo | Descricao | Status |
|--------|-----------|--------|
| RICHTER | Predicao sismica com CatBoost | Producao |
| CLIMATIK | Coleta de dados climaticos (GFS + OWM) | Producao |
| VISUAL | Analise SAR com Sentinel-1 | Producao |
| NEXUS OIKOS | Pipeline de videos para TikTok/X | Producao |

## Tecnologias

- Python 3.12+
- Google Earth Engine
- Edge-TTS (voz neural)
- Whisper (OpenAI)
- MoviePy
- Scikit-learn / CatBoost

## Ultima Atualizacao

04/08/2026 14:19:43

---
NEXUS OIKOS — Tecnologia com alma, dados com proposito.