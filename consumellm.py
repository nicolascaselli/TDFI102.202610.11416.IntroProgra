import requests
import json

# --- Configuración del Servidor Ollama ---
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "gemma4:e4b"  # El modelo que quieres usar


def generate_response(prompt: str):
    """
    Envía un prompt a la API de Ollama para obtener una respuesta del modelo.
    """
    # 1. Definir los datos a enviar (payload)
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False  # False para esperar la respuesta completa al final
    }

    # 2. Definir los encabezados (headers)
    headers = {
        "Content-Type": "application/json"
    }

    print(f"Enviando solicitud al servidor Ollama para el modelo {MODEL_NAME}...")

    try:
        # 3. Realizar la solicitud POST
        response = requests.post(OLLAMA_URL, headers=headers, data=json.dumps(payload))

        # 4. Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            # 5. Parsear la respuesta (la respuesta viene en formato JSON)
            data = response.json()

            # Extraer la respuesta del modelo
            generated_text = data.get("response", "No se encontró la respuesta.")

            print("\n" + "=" * 50)
            print(f"✅ Respuesta del modelo {MODEL_NAME}:")
            print("=" * 50)
            print(generated_text)
            print("=" * 50)

        else:
            print(f"\n❌ Error en la respuesta del servidor. Código de estado: {response.status_code}")
            print("Respuesta del servidor:", response.text)

    except requests.exceptions.ConnectionError:
        print("\n❌ ERROR DE CONEXIÓN:")
        print("Asegúrate de que el servidor Ollama esté corriendo y accesible en http://localhost:11434.")
    except Exception as e:
        print(f"\n❌ Ocurrió un error inesperado: {e}")


# --- Uso del Script ---
if __name__ == "__main__":
    user_prompt = "¿Cuál es la diferencia entre el aprendizaje supervisado y el no supervisado en Machine Learning?"

    generate_response(user_prompt)
