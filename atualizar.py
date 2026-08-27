import json
import datetime

# Exemplo de dados simulados ou buscados de APIs externas
dados = {
    "status": "online",
    "youtube": {
        "canal": "Seu Canal",
        "inscritos": "1.2k",
        "ultimo_video": f"Atualizado em: {datetime.datetime.now().strftime('%d/%m/%Y às %H:%M')}"
    },
    "tiktok": {
        "perfil": "@seuusuario",
        "seguidores": "5.4k",
        "ultimo_video": "Novo desafio postado hoje"
    }
}

# Reescreve o arquivo Opa.json com os novos valores
with open('Opa.json', 'w', encoding='utf-8') as f:
    json.dump(dados, f, ensure_ascii=False, indent=4)
  
