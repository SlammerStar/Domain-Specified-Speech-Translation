# 🎙️ Domain-Specified-Speech-Translation

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SlammerStar/Domain-Specified-Speech-Translation/blob/main/Domain_Speech_Translation_Colab.ipynb)

## 📌 Overview
**Domain-Specified Speech Translation** is a Python-based project that leverages **OpenAI's Whisper ASR** to transcribe speech into text with high accuracy, optimized for specific domains such as **NPTEL educational content** and **robot instruction parsing**.  
The project evaluates transcription quality using **Character Error Rate (CER)** and includes domain-specific NLP post-processing.

---

## 🎯 Goals
- **Accurate Speech-to-Text Conversion** using state-of-the-art **Whisper** model.
- **Domain Adaptation** for improved recognition of specialized vocabulary and context.
- **Performance Evaluation** via **CER** to measure transcription reliability.
- **Efficient Workflow** to save manual transcription time.

---

## ⚙️ Features
- **Whisper-based ASR**: Robust speech recognition trained on diverse datasets.
- **Domain-Specific Models**: Tailored scripts for **NPTEL** lectures and **robot instructions**.
- **Performance Metrics**: Automated CER calculation for quality assessment.
- **Multi-Script Architecture**:
  - `whisper_transcribe_cer.py` → Transcription with CER evaluation.
  - `nptel_transcription.py` → NPTEL-specific transcription handling.
  - `Robot_Instruction_NLP.py` → NLP for robot instruction parsing.
- **JSON Output Support** for structured results.

---

## 🛠️ Skills & Technologies Used
- **Programming**: Python
- **AI/ML**: OpenAI Whisper, NLP, ASR
- **Data Processing**: Text normalization, CER calculation
- **Domain Adaptation**: Specialized vocabulary integration
- **Tools**: Git, JSON handling
- **Libraries**: 
  - `whisper`
  - `torch`
  - `numpy`
  - `pandas`
  - `jiwer` (for CER calculation)

---

## 🗂️ Project Structure
📂 Domain-Specified-Speech-Translation
├── scripts/
│ ├── whisper_transcribe_cer.py
│ ├── nptel_transcription.py
│ └── Robot_Instruction_NLP.py
├── sample_audio/
│ └── harvard.wav
├── requirements.txt
├── README.md

---

## 🚀 Installation & Usage

### **Option 1 — Run on Google Colab** (Recommended)
Click the **"Open in Colab"** badge above and run all cells.  
No local setup needed.

---

### **Option 2 — Run Locally**
1️⃣ **Clone the Repository**
```bash
git clone https://github.com/SlammerStar/Domain-Specified-Speech-Translation.git
cd Domain-Specified-Speech-Translation

2️⃣ **Install Dependencies**
pip install -r requirements.txt

3️⃣ Run Transcription
python scripts/whisper_transcribe_cer.py --audio sample_audio/harvard.wav

4️⃣ Run Domain-Specific Scripts
# NPTEL Lectures
python scripts/nptel_transcription.py --audio path/to/lecture.wav

# Robot Instructions
python scripts/Robot_Instruction_NLP.py --input path/to/audio.wav

📊 Performance (CER Results)
| Dataset         | CER         |
| --------------- | ----------- |
| test-clean      | 0.000312535 |
| test-other      | 0.000821592 |
| train-clean-100 | 0.000172000 |
| NPTEL Dataset   | 0.278767957 |

📌 Example Output
Input Audio: sample_audio/harvard.wav
Transcription Output:THE BIRCH CANOE SLID ON THE SMOOTH PLANKS
CER: 0.00031

📈 Future Improvements
-Add real-time transcription capability.
-Implement GUI/web interface for user-friendly operation.
-Expand domain adaptation for medical and legal transcription.
-Deploy as an API for integration into other applications.

🧑‍💻 Author
Pratham Nigam
B.Tech 3rd Year, Computer Science
Skills: Python, Django, NLP, Web Development, Machine Learning

📜 License
This project is licensed under the MIT License.

---

