# 📂 Blip-Folder-Map

```powershell
# O comando oficial e estruturado
function blip-map { 
    python "D:\jetblip\github\blip-folder-names\map_folders.py" --path $args[0] 
}

# Atalho rápido para máxima eficiência
Set-Alias blipmap blip-map

```

THEN!!!

blip-map D:\ollama\models\manifests\registry.ollama.ai\library


Uma utilitária leve e sem dependências em Python para gerar mapas organizados de diretórios em formato Markdown. Esta ferramenta faz parte do **Ecossistema Jetblip (v5)**.

## 🚀 Visão Geral

O `Blip-Folder-Map` foi criado para programadores que precisam de documentar arquiteturas de projetos, mapear estruturas legadas ou partilhar uma visão limpa do conteúdo de um repositório. O script gera um ficheiro `.md` ordenado com todas as pastas dentro de um caminho alvo, guardando-os numa pasta `maps/` local.

## ✨ Funcionalidades

* **Zero Dependências**: Utiliza apenas bibliotecas padrão do Python (`os`, `datetime`, `argparse`, `re`).
* **Nomenclatura Inteligente (Hybrid Context-Aware)**: O script adapta o nome do ficheiro automaticamente para garantir legibilidade:
* **Caminhos Simples**: Usa o padrão *Kebab-case* (ex: `d-ollama-models`).
* **Caminhos Complexos**: Se detetar hífens no caminho (ex: `my-projects`), muda para o estilo *Dot-Namespace* (ex: `D.my-projects.app`) para evitar confusão.
* **Tratamento de Conflitos**: Se existirem pontos e hífens em simultâneo, aplica uma lógica de prioridade para manter a hierarquia clara.


* **Mapeamento Limpo**: Ignora automaticamente pastas ocultas (como `.git`) e foca-se apenas na estrutura de diretórios.
* **Auto-Organização**: Cria automaticamente uma pasta `maps/` para manter a raiz do teu repositório organizada.

## 🛠️ Instalação

1. **Clonar o repositório**:
```powershell
git clone https://github.com/jeremytrindade/blip-folder-map.git
cd blip-folder-map

```


2. **Requisitos**:
* Python 3.6+ instalado.



## 📖 Como Usar

### 1. Chamada por Alias (Recomendado)

Para usar o comando `blip-map` de qualquer lugar no teu PC, adiciona estas funções ao teu perfil do PowerShell (`$PROFILE`):

```powershell
# O comando oficial e estruturado
function blip-map { 
    python "D:\jetblip\github\blip-folder-names\map_folders.py" --path $args[0] 
}

# Atalho rápido para máxima eficiência
Set-Alias blipmap blip-map

```

### 2. Exemplos de Execução Autómata

O script decide o melhor nome de ficheiro sozinho:

| Comando | Lógica Aplicada | Exemplo de Nome Gerado |
| --- | --- | --- |
| `blip-map D:\ollama\models` | Kebab Style | `d-ollama-models__20260511-2230.md` |
| `blip-map D:\my-projects\app` | Dot Style | `D.my-projects.app__20260511-2230.md` |
| `blip-map C:\v1.5\test-files` | Priority Style | `C.v1..5.test-files__20260511-2230.md` |

## 📁 Estrutura do Output

Os ficheiros são guardados na subpasta `maps/` com este formato:

```markdown
# 📂 Folder Map: D:\target\path
*Generated on: 2026-05-11 22:30:15*

Total folders found: 5

* `folder-one`
* `folder-two`

```

## ⚖️ Licença

Este projeto é open-source e está disponível sob a licença MIT.

Mantido pela equipa **Jetblip**.