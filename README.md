# Sincronizador de Video MP4 con Audio MP3

Este script de Python sincroniza un archivo de video MP4 con un archivo de audio MP3, ajustando la duración del video para que coincida con la del audio. Es útil para crear videos musicales, añadir nuevas pistas de audio a videos existentes, o sincronizar clips de video con grabaciones de audio separadas.

## Características

- Sincroniza un archivo de video MP4 con un archivo de audio MP3.
- Ajusta automáticamente la duración del video:
  - Si el video es más corto que el audio, lo repite hasta que coincida con la duración del audio.
  - Si el video es más largo que el audio, lo recorta para que coincida con la duración del audio.
- Utiliza la biblioteca MoviePy para un procesamiento eficiente y fácil de usar.

## Requisitos

- Python 3.6 o superior
- MoviePy

## Instalación

1. Asegúrate de tener Python instalado en tu sistema.
2. Instala MoviePy usando pip:

   ```
   pip install moviepy
   ```

## Uso

1. Coloca el script `sync_video_audio.py` en el mismo directorio que tus archivos de video y audio.

2. Modifica las siguientes variables en el script para que coincidan con los nombres de tus archivos:

   ```python
   video_file = 'input_video.mp4'
   audio_file = 'input_audio.mp3'
   output_file = 'output_video.mp4'
   ```

3. Ejecuta el script:

   ```
   python sync_video_audio.py
   ```

4. El script generará un nuevo archivo de video (`output_video.mp4`) que combina el video de entrada con el audio de entrada, ajustando la duración del video según sea necesario.

## Cómo funciona

1. El script carga el video y el audio usando MoviePy.
2. Compara la duración del video con la del audio.
3. Si el video es más corto, lo repite las veces necesarias y luego lo recorta para que coincida exactamente con la duración del audio.
4. Si el video es más largo, simplemente lo recorta para que coincida con la duración del audio.
5. Combina el video ajustado con el audio original.
6. Guarda el resultado como un nuevo archivo de video.

## Notas

- El procesamiento puede llevar tiempo, especialmente para archivos grandes.
- Asegúrate de tener suficiente espacio en disco para el archivo de salida.
- La calidad del video de salida dependerá de la calidad de los archivos de entrada.

## Solución de problemas

Si encuentras algún error, verifica lo siguiente:

1. Asegúrate de que MoviePy esté correctamente instalado.
2. Verifica que los nombres de los archivos de entrada sean correctos y que los archivos existan en el mismo directorio que el script.
3. Asegúrate de tener permisos de escritura en el directorio para crear el archivo de salida.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir cambios importantes antes de enviar un pull request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.
