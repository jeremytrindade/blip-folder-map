import os
from datetime import datetime
import argparse
import re

def generate_folder_map():
    parser = argparse.ArgumentParser(description="Mapeia pastas de um diretório alvo.")
    parser.add_argument("--path", type=str, default="..", help="Caminho alvo para listar pastas")
    parser.add_argument("--style", type=str, choices=['kebab', 'dot'], default='kebab', 
                        help="Estilo do nome do ficheiro: 'kebab' (padrão) ou 'dot'")
    args = parser.parse_args()

    # 1. Definir pastas
    script_dir = os.path.dirname(os.path.abspath(__file__))
    target_dir = os.path.abspath(args.path)
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    
    # 2. Lógica de Estilização
    if args.style == 'dot':
        # Estilo Dot: D.Ollama.Models__20260511-222730.md
        clean_path = target_dir.replace(":\\", ".").replace(":/", ".").replace("\\", ".").replace("/", ".")
        path_id = re.sub(r'[^a-zA-Z0-9.-]', '', clean_path)
        path_id = re.sub(r'\.+', '.', path_id).strip('.')
        filename = f"{path_id}__{timestamp}.md"
    else:
        # Estilo Kebab (Industry Standard): d-ollama-models--20260511-222730.md
        clean_path = target_dir.lower().replace(":\\", "-").replace(":/", "-").replace("\\", "-").replace("/", "-")
        path_id = re.sub(r'[^a-z0-9-]', '', clean_path)
        path_id = re.sub(r'-+', '-', path_id).strip('-')
        filename = f"{path_id}--{timestamp}.md"

    # 3. Criar pasta 'maps' se não existir
    maps_dir = os.path.join(script_dir, "maps")
    if not os.path.exists(maps_dir):
        os.makedirs(maps_dir)
        print(f"📁 Pasta criada: {maps_dir}")

    save_path = os.path.join(maps_dir, filename)

    try:
        folders = [f for f in os.listdir(target_dir) 
                   if os.path.isdir(os.path.join(target_dir, f)) and not f.startswith('.')]
        folders.sort()

        with open(save_path, 'w', encoding='utf-8') as md_file:
            md_file.write(f"# 📂 Folder Map: {target_dir}\n")
            md_file.write(f"*Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n")
            md_file.write(f"Total folders found: **{len(folders)}**\n\n---\n\n")
            for folder in folders:
                md_file.write(f"* `{folder}`\n")

        print(f"✅ Sucesso! Ficheiro criado: {filename}")
        print(f"📍 Mapeado de: {target_dir}")
        print(f"📂 Guardado em: {maps_dir}")

    except Exception as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    generate_folder_map()