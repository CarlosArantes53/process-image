from PIL import Image, ImageFilter
import os
import time
import threading

input_folder = 'input_images'
output_folder = 'output_images'

os.makedirs(output_folder, exist_ok=True)

def process_image(image_path, output_folder):
    with Image.open(image_path) as img:
        img = img.resize((800, 600))
        #Tarefas - 1. Redimensionamento: Redimensionar todas as imagens para uma resolução específica (por exemplo, 800x600 pixels).

        img_bw = img.convert("L") #preto e branco
        img_contrast = img.filter(ImageFilter.EDGE_ENHANCE) #aumento de contraste
        #Tarefas - 2. Aplicação de Filtros: Aplicar pelo menos dois filtros diferentes em cada imagem (por exemplo, preto e branco, aumento de contraste, etc.).
        
        base_name = os.path.basename(image_path)
        img_bw.save(os.path.join(output_folder, f"bw_{base_name}"))
        img_contrast.save(os.path.join(output_folder, f"contrast_{base_name}"))
        #Tarefas - 3. Salvar as imagens processadas em uma nova pasta.

def process_images_sequential(input_folder, output_folder):
    #Implementação - Versão Sequencia - 1. Implemente uma versão que processe as imagens uma por uma.
    start_time = time.time()

    for filename in os.listdir(input_folder):
        image_path = os.path.join(input_folder, filename)
        process_image(image_path, output_folder)

    end_time = time.time()
    print(f"Tempo Sequencial: {end_time - start_time:.5f} segundos")
    #Implementação - Versão Sequencia - 2. Meça e registre o tempo total de execução.

def process_image_thread(image_path, output_folder):
    process_image(image_path, output_folder)

#Implementação - Versão Concorrente:
def process_images_concurrent(input_folder, output_folder, num_threads):
    start_time = time.time()

    threads = []
    for filename in os.listdir(input_folder):
        image_path = os.path.join(input_folder, filename)
        thread = threading.Thread(target=process_image_thread, args=(image_path, output_folder))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"Tempo total de execução ({num_threads} threads): {end_time - start_time:.5f} segundos")
#Implementação - Versão Concorrente - 3. Meça e registre o tempo total de execução para cada configuração de threads.

if __name__ == "__main__":
    process_images_sequential(input_folder, output_folder)
    #Implementação - Versão Concorrente - 1. Implemente uma versão que utilize threads para processar múltiplas imagens simultaneamente.

    for num_threads in [2, 4, 8]:
        process_images_concurrent(input_folder, output_folder, num_threads) 
    #Implementação - Versão Concorrente - 2. Experimente com diferentes números de threads (por exemplo, 2, 4, 8) e compare os resultados.