import streamlit as st
import google.generativeai as genai

from cat_promts_tipo_correo import generar_prompt

GOOGLE_API_KEY = 'xxxxx'
##########################################################
genai.configure(api_key=GOOGLE_API_KEY)

# for m in genai.list_models():
#   if 'generateContent' in m.supported_generation_methods:
#     print(m.name)

model = genai.GenerativeModel('gemini-1.0-pro')

def generar_correo(prompt):
    # Llamada al modelo de lenguaje para generar el correo electrónico
    response = model.generate_content(prompt)
    correo = response.text
    return correo

# Configuración de la interfaz de Streamlit
st.title("EmailBot")

st.write("### Descripción")
st.write("Esta aplicación te ayuda a generar plantillas de correos electrónicos para diferentes propósitos.")

st.write("### Cómo Funciona")
st.write("""
- **Selecciona el tipo de correo:** Elige el tipo de correo electrónico que deseas generar.
- **Generar Correo:** Presiona el botón para generar la plantilla que podrás usar para crear tu correo electrónico.
- **Resultados:** Obtendrás una plantilla que podrás adaptar y usar para tu comunicación con clientes.
""")

tipo_correo = st.selectbox(
    "Selecciona el tipo de correo electrónico",
    ["invitación_evento", "aniversario_empresa", "felicitaciones_logro", "felicitaciones_cumpleaños", "promocion_productos", "seguimiento_profesional", "confirmacion_reunion"]
)

if st.button("Generar Correo"):
     prompt = generar_prompt(tipo_correo)
     correo_generado = generar_correo(prompt)
     st.subheader("Tu Plantilla de Correo Electrónico:")
     st.write(correo_generado)
   

