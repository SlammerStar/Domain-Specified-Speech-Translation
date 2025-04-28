import os
import whisper
import Levenshtein
import librosa
import re
import json

def preprocess_text(text):
    text=text.lower()
    text=re.sub(r'[^\w\s]','',text)
    tokens=text.split()
    return tokens

def is_move_intent(tokens):
    move_keywords=['move','go','forward','ascend','up','advance','fly','down','descend']
    for token in tokens:
        if token in move_keywords:
            return True
    return False

def extract_commands(tokens):
    actions=[]
    i=0
    while i<len(tokens):
        if tokens[i] in ['move','go','advance','fly','ascend','descend']:
            action={'action':tokens[i]}
            if i+1<len(tokens) and tokens[i+1] in ['up','forward','backward','down']:
                action['direction']=tokens[i+1]
                i+=2
            else:
                action['direction']=None
                i+=1

            if i<len(tokens) and tokens[i]=='by':
                if i+2<len(tokens) and tokens[i+1].isdigit() and tokens[i+2] in ['meters','meter']:
                    action['distance']=int(tokens[i+1])
                    i+=3
                elif i+1<len(tokens) and tokens[i].isdigit():
                    action['distance']=int(tokens[i+1])
                    i+=2
                else:
                    action['distance']=None
            else:
                action['distance']=None
            actions.append(action)
        else:
            i+=1
    return actions

def process_transcription(transcription):
    tokens=preprocess_text(transcription)
    if is_move_intent(tokens):
        commands=extract_commands(tokens)
        return commands
    else:
        print("No movement intent detected.")
        return []


def voice_transcription(file_path, model): #transcribe the audio files
    voice, sr = librosa.load(file_path, sr=None)
    voice = whisper.pad_or_trim(voice)
    mel = whisper.log_mel_spectrogram(voice).to(model.device)
    options = whisper.DecodingOptions(fp16=False)
    result = whisper.decode(model, mel, options)
    return result.text

def solving_cer(transcription, truth_file):
    # Convert both transcriptions and ground truth to lower case
    transcription = transcription.lower()
    truth_file = truth_file.lower()
    return Levenshtein.distance(transcription, truth_file) / len(truth_file)


if __name__ == "__main__":
    model = whisper.load_model("base")
    directory = r"C:\Users\arrus\OneDrive\Desktop\Robot"

    ground_truth_file=None
    data_file=None


    for file_name in os.listdir(directory):
        if file_name.endswith(('.mp3','.wav','.m4a','.flac')):
            data_file=os.path.join(directory,file_name)
        elif file_name=='robot_instruction.txt':
            ground_truth_file=os.path.join(directory,file_name)


    transcription=None
    ground_truth=None
    cer=None
    commands=None

    if data_file and ground_truth_file:
        transcription=voice_transcription(data_file,model)

        with open(ground_truth_file,"r",encoding="utf-8") as f:
            ground_truth=f.read().strip()

        cer = solving_cer(transcription,ground_truth)

        print(f"Transcription: {transcription}")
        print(f"Ground Truth: {ground_truth}")
        print(f"CER: {cer}")

        commands= process_transcription(transcription)
        print("Extracted Commands: \n",commands)
    else:
        print("Data file or ground truth file not found.")
    if transcription and ground_truth and cer is not None and commands is not None:
            results={
                "Transcription: ":transcription,
                "Ground Truth: ":ground_truth,
                "CER: ":cer,
                "Commands ":commands
            }
    with open('Robot_Instruction_results.json','w') as json_file:
        json.dump(results,json_file,indent=4)

    print("Transcription, command extraction, and CER calculation completed.")