from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
import os

def sync_video_audio(video_path, audio_path, output_path):
    # Cargar el video y el audio
    video = VideoFileClip(video_path)
    audio = AudioFileClip(audio_path)

    # Obtener las duraciones
    video_duration = video.duration
    audio_duration = audio.duration

    if video_duration < audio_duration:
        # Si el video es más corto, lo repetimos
        repeats = int(audio_duration / video_duration) + 1
        extended_video = concatenate_videoclips([video] * repeats)
        final_video = extended_video.subclip(0, audio_duration)
    else:
        # Si el video es más largo, lo cortamos
        final_video = video.subclip(0, audio_duration)

    # Establecer el audio
    final_video = final_video.set_audio(audio)

    # Escribir el resultado
    final_video.write_videofile(output_path, codec='libx264', audio_codec='aac')

    # Cerrar los clips para liberar recursos
    video.close()
    audio.close()
    final_video.close()

# Ejemplo de uso
video_file = 'input_video.mp4'
audio_file = 'input_audio.mp3'
output_file = 'output_video.mp4'

if __name__ == "__main__":
    if not os.path.exists(video_file):
        print(f"Error: El archivo de video '{video_file}' no existe.")
    elif not os.path.exists(audio_file):
        print(f"Error: El archivo de audio '{audio_file}' no existe.")
    else:
        sync_video_audio(video_file, audio_file, output_file)
        print(f"Video sincronizado creado con éxito: {output_file}")