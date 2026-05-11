import os
from datetime import datetime
import argparse

def generate_folder_map():
    parser = argparse.ArgumentParser(description="Mapeia pastas de um diretório alvo.")
    parser.add_argument("--path", type=str, default="..", help="Caminho alvo para listar pastas")
    args = parser.parse_args()

    # 1. Definir pastas
    script_dir = os.path.dirname(os.path.abspath(__file__))
    target_dir = os.path.abspath(args.path)
    
    # Extrair o nome da pasta de origem (ex: "github" em vez do caminho completo)
    origin_name = os.path.basename(target_dir)
    # Se o path terminar em barra ou for raiz, o basename pode ser vazio
    if not origin_name:
        origin_name = "root"

    # 2. Criar pasta 'maps' se não existir
    maps_dir = os.path.join(script_dir, "maps")
    if not os.path.exists(maps_dir):
        os.makedirs(maps_dir)
        print(f"📁 Pasta criada: {maps_dir}")

    # 3. Nome do ficheiro: originDirectory-YYYYMMDD-HHMMSS
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"{origin_name}-{timestamp}.md"
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