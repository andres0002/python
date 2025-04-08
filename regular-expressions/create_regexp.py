import re

# Detectando un num CABA (formato Argentina) y ocultandolo.

text = "Hola Pepe, mi numero es: +54 11 4321-4321, +54 11 4421-4523."

pattern = r"\+\d{2}\s\d{2}\s\d{4}-\d{4}"

remplacet = re.sub(pattern, "(hided num)", text)

print(remplacet)