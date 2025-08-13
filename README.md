# 🎙️ Domain-Specified Speech Translation

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
├── whisper_transcribe_cer.py # Core transcription + CER evaluation
├── nptel_transcription.py # NPTEL domain-specific transcription
├── Robot_Instruction_NLP.py # NLP for robot instruction processing
├── Robot_Instruction_results.json # Sample output for NLP script
├── requirements.txt # Dependencies
├── README.md # Documentation (this file)
└── ...

---

## 🚀 Installation & Usage

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/SlammerStar/Domain-Specified-Speech-Translation.git
cd Domain-Specified-Speech-Translation

2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run Transcription
python whisper_transcribe_cer.py --audio path/to/audio.wav
4️⃣ Domain-Specific Execution
NPTEL Lectures
python nptel_transcription.py --audio path/to/lecture.wav
Robot Instructions
python Robot_Instruction_NLP.py --input path/to/audio.wav

📊 Performance (CER Results)
| Dataset         | CER         |
| --------------- | ----------- |
| test-clean      | 0.000312535 |
| test-other      | 0.000821592 |
| train-clean-100 | 0.000172000 |
| NPTEL Dataset   | 0.278767957 |

📈 Future Improvements
Add real-time transcription capability.

Implement GUI/web interface for user-friendly operation.

Expand domain adaptation for medical and legal transcription.

Deploy as an API for integration into other applications.

🧑‍💻 Author
Pratham Nigam
B.Tech 3rd Year, Computer Science
Skills: Python, Django, NLP, Web Development, Machine Learning

📜 License
This project is licensed under the MIT License.

---

If you want, I can also **add usage examples with screenshots and sample outputs** so your README looks visually appealing for GitHub visitors. That would make it more professional and recruiter-friendly.
