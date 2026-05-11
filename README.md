📄 README.md
Markdown
# 📂 Blip-Folder-Map

Uma utilitária leve e sem dependências em Python para gerar mapas organizados de diretórios em formato Markdown. Esta ferramenta faz parte do **Ecossistema Jetblip (v5)**.

## 🚀 Visão Geral

O `Blip-Folder-Map` foi criado para programadores que precisam de documentar arquiteturas de projetos, mapear estruturas legadas ou partilhar uma visão limpa do conteúdo de um repositório. O script gera um ficheiro `.md` ordenado com todas as pastas dentro de um caminho alvo, guardando-os numa pasta `maps/` local.

## ✨ Funcionalidades

- **Zero Dependências**: Utiliza apenas bibliotecas padrão do Python (`os`, `datetime`, `argparse`).
- **Mapeamento Inteligente**: Ignora automaticamente pastas ocultas (como `.git`) e ficheiros, focando-se apenas na estrutura de diretórios.
- **Timestamping**: Gera nomes de ficheiros únicos (ex: `folders-2026-05-11-16-37.md`).
- **Auto-Organização**: Cria automaticamente uma pasta `maps/` para manter a raiz do teu repositório limpa.

## 🛠️ Instalação

1. **Clonar o repositório**:
   ```bash
   git clone [https://github.com/jeremytrindade/blip-folder-map.git](https://github.com/jeremytrindade/blip-folder-map.git)
   cd blip-folder-map
Garantir que o Python está instalado:
Recomendado Python 3.6+.

📖 Como Usar
1. Chamada Direta (Caminho Absoluto)
Esta é a melhor forma se estiveres num terminal qualquer e não quiseres navegar até à pasta do script. Basta indicares o caminho completo do ficheiro .py e o --path do que queres mapear.

No PowerShell:

PowerShell
python "D:\jetblip\github\blip-folder-names\map_folders.py" --path "D:\jetblip\github"
2. Chamada por Alias (A forma "Pro")
Se queres que isto seja um comando permanente que possas usar como se fosse um programa do Windows, podes criar um alias no teu perfil do PowerShell:

No PowerShell:

PowerShell
# Cria o comando 'blip-map'
function blip-map { python "D:\jetblip\github\blip-folder-names\map_folders.py" --path $args[0] }
Agora, podes simplesmente escrever de qualquer lugar:

PowerShell
blip-map D:\aijetlabs\github
📁 Exemplo de Output
Os ficheiros são guardados na subpasta maps/ com este formato:

📂 Folder Map: D:\jetblip\github
Generated on: 2026-05-11 16:37:00

Total folders found: 24

blip-ask

blip-brain

jet-naming-pro

⚖️ Licença
Este projeto é open-source e está disponível sob a licença MIT.

Mantido pela equipa Jetblip.