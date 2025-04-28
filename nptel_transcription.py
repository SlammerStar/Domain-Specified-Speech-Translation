import os
import whisper
import Levenshtein
import csv
import librosa

def voice_transcription(file_path, model):
    voice, sr = librosa.load(file_path, sr=None) #loading the .wav files by using librosa
    voice = whisper.pad_or_trim(voice) #trim the audio according to usage
    mel = whisper.log_mel_spectrogram(voice).to(model.device) # Convert the audio to a log-mel spectrogram
    options = whisper.DecodingOptions(fp16=False)
    result = whisper.decode(model, mel, options) #initialising transcription
    return result.text

def solving_cer(transcription, truth_file):
    transcription = transcription.lower()
    truth_file = truth_file.lower()
    if len(truth_file)==0:
        return None
    return Levenshtein.distance(transcription, truth_file) / len(truth_file)

def extracting_files(voice_folder, truth_folder, model):
    cer_results = []
    for file_name in os.listdir(voice_folder):
        if file_name.endswith('.wav'):  #checking if the file is a .wav file
            voice_file_path = os.path.join(voice_folder, file_name)
            file_id = os.path.splitext(file_name)[0]
            transcription = voice_transcription(voice_file_path, model).strip().lower() #trancripting the .wav file
            truth_file_name = f"{file_id}.txt"
            truth_file_path = os.path.join(truth_folder, truth_file_name)
            if os.path.exists(truth_file_path): #checking for truth file
                with open(truth_file_path, "r", encoding="latin-1") as f:
                    truth = f.read().strip().lower()
                cer = solving_cer(transcription, truth)
                if cer is not None:
                    cer_results.append((file_id, cer))
                else:
                    print(f"Warning: Ground truth is empty for {file_id}")
            else:
                print(f"Truth file {truth_file_path} not found for {file_id}")
    return cer_results

if __name__ == "__main__":
    model = whisper.load_model("base") #using the whisper model
    voice_files_folder = r"C:\Users\arrus\OneDrive\Desktop\nptel\wav"
    truth_file_folder = r"C:\Users\arrus\OneDrive\Desktop\nptel\original_txt"
    all_cer_results = extracting_files(voice_files_folder, truth_file_folder, model)
    cer_output_file = r"C:\Users\arrus\OneDrive\Desktop\cer_results.csv" #results file path
    with open(cer_output_file, "w", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["File ID", "CER"])
        for result in all_cer_results:
            csv_writer.writerow(result)
    print("Transcription and CER calculation completed.")
