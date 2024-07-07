def generar_prompt(tipo_correo):
    prompts = {
        "invitación_evento": "Genera una plantilla de correo electrónico para invitar a un cliente a un evento organizado por la empresa. Utiliza un tono agradecido y atento, asegurándote de que el cliente se sienta valorado.",
        "aniversario_empresa": "Genera una plantilla de correo electrónico para felicitar a un cliente por su aniversario de ser parte de la empresa. Utiliza un tono agradecido y atento, asegurándote de que el cliente se sienta valorado.",
        "felicitaciones_logro": "Genera una plantilla de correo electrónico para felicitar a un cliente por un logro obtenido. Utiliza un tono agradecido y atento, asegurándote de que el cliente se sienta valorado.",
        "felicitaciones_cumpleaños": "Genera una plantilla de correo electrónico para felicitar a un cliente por su cumpleaños. Utiliza un tono agradecido y atento, asegurándote de que el cliente se sienta valorado.",
        "promocion_productos": "Genera una plantilla de correo electrónico para promocionar productos de la empresa a un cliente. Utiliza un tono agradecido y atento, asegurándote de que el cliente se sienta valorado.",
        "seguimiento_profesional": "Genera una plantilla de correo electrónico para hacer seguimiento profesional después de una reunión de negocios con un cliente. Utiliza un tono agradecido y atento, asegurándote de que el cliente se sienta valorado.",
        "confirmacion_reunion": "Genera una plantilla de correo electrónico para confirmar una reunión con un cliente. Utiliza un tono agradecido y atento, asegurándote de que el cliente se sienta valorado."
    }

    return prompts.get(tipo_correo, "Tipo de correo no reconocido. Por favor, elige uno de los siguientes tipos: invitación_evento, aniversario_empresa, felicitaciones_logro, felicitaciones_cumpleaños, promocion_productos, seguimiento_profesional, confirmacion_reunion.")
