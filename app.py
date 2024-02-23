import streamlit as st
import assemblyai as aai

# Replace with your AssemblyAI API key
aai.settings.api_key = "0f17d11299bd4b988050d81317fa37e8"

def transcribe_audio(file_url):
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(file_url)
    return transcript

def main():
    st.title("Audio Transcription App")

    file_url = st.text_input("Enter the URL of the audio file:")
    
    if st.button("Transcribe"):
        if not file_url:
            st.warning("Please enter the URL of the audio file.")
        else:
            transcript = transcribe_audio(file_url)
            
            if transcript.status == aai.TranscriptStatus.error:
                st.error(f"Transcription Error: {transcript.error}")
            else:
                st.success("Transcription Successful!")
                st.audio(file_url, format='audio/mp3', start_time=0)
                st.write("Transcription:")
                st.write(transcript.text)

if __name__ == "__main__":
    main()
