from PIL import Image, ImageFilter
import os
import time

# Definindo a pasta de entrada e saída
input_folder = 'input_images'
output_folder = 'output_images'

# Cria a pasta de saída se não existir
os.makedirs(output_folder, exist_ok=True)

# Função para redimensionar e aplicar filtros
def process_image(image_path, output_folder):
    with Image.open(image_path) as img:
        # Redimensiona a imagem para 800x600
        img = img.resize((800, 600))

        # Aplica dois filtros: preto e branco e aumento de contraste
        img_bw = img.convert("L")  # Converte para preto e branco
        img_contrast = img.filter(ImageFilter.EDGE_ENHANCE)  # Filtro de realce de bordas

        # Salva as imagens processadas na pasta de saída
        base_name = os.path.basename(image_path)
        img_bw.save(os.path.join(output_folder, f"bw_{base_name}"))
        img_contrast.save(os.path.join(output_folder, f"contrast_{base_name}"))

# Função para a versão sequencial
def process_images_sequential(input_folder, output_folder):
    start_time = time.time()

    # Itera sobre todas as imagens da pasta de entrada
    for filename in os.listdir(input_folder):
        image_path = os.path.join(input_folder, filename)
        process_image(image_path, output_folder)

    end_time = time.time()
    print(f"Tempo total de execução (Sequencial): {end_time - start_time:.2f} segundos")

if __name__ == "__main__":
    process_images_sequential(input_folder, output_folder)
