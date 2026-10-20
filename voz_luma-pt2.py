respuesta = ("Hola. Para reiniciar tu router Luma, desconéctalo "
             "durante treinta segundos y vuelve a conectarlo.")
 
speech_config.speech_synthesis_voice_name = "es-MX-DaliaNeural"
audio_out = speechsdk.audio.AudioOutputConfig(filename="respuesta.wav")
synthesizer = speechsdk.SpeechSynthesizer(
    speech_config=speech_config, audio_config=audio_out)
 
result = synthesizer.speak_text_async(respuesta).get()
if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Audio guardado en respuesta.wav")
