# 🧠 Predictive Test Generator

An AI-powered web application that generates personalized test questions based on the user's input topic and difficulty level using OpenAI's GPT model. This tool is ideal for students and educators who want to create dynamic practice tests in seconds.

## 🚀 Live Demo

👉 [Live Website](https://sanjana-tanwar.github.io/Predictive-Test-Generator/)

## 📌 Features

- 🧑‍🎓 Generate multiple-choice questions on any topic
- 📚 Choose from difficulty levels: Easy, Medium, Hard
- 🧪 Get 5 questions per test with 4 options each
- ✅ Check answers immediately
- 🎨 Clean, responsive UI using React and Tailwind CSS
- ⚙️ Powered by OpenAI API for content generation

## 🛠️ Tech Stack

- **Frontend**: React.js, Tailwind CSS
- **AI API**: OpenAI GPT-3.5
- **Deployment**: Vercel

## 📷 Screenshots

<p align="center">
  <img src="https://github.com/sanjana-tanwar/Predictive-Test-Generator/assets/117594940/6f4c2932-8b9f-4125-8b71-6c3b540e4d82" alt="Home Page" width="600"/>
</p>
<p align="center">
  <img src="https://github.com/sanjana-tanwar/Predictive-Test-Generator/assets/117594940/8f7a5930-c937-4c39-b7f8-9f7025e390a1" alt="Generated Test Page" width="600"/>
</p>

## 📦 Installation

To run locally:

```bash
# Clone the repository
git clone https://github.com/sanjana-tanwar/Predictive-Test-Generator.git
cd Predictive-Test-Generator

# Install dependencies
npm install

# Create .env file for OpenAI API key
echo "VITE_OPENAI_API_KEY=your_api_key_here" > .env

# Start the development server
npm run dev
