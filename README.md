# ProdPrepAI - AI-Powered Interview Preparation for Product Managers

## Project Overview
ProdPrepAI is a cutting-edge AI platform designed to assist aspiring product managers with comprehensive interview preparation. This platform simulates realistic product management interview scenarios, providing tailored feedback to help users strengthen their skills and improve their performance. Leveraging advanced NLP models and reinforcement learning, ProdPrepAI ensures an interactive and adaptive interview experience.

This project is part of the **CS230: Deep Learning course** at Stanford (Fall '24), taught by **Prof. Andrew Ng** and **Kian Katanforoosh**.

## Problem Statement
In a highly competitive job market, candidates for product management roles face unique challenges in preparing for interviews. Traditional mock interviews often lack consistent, high-quality feedback. ProdPrepAI bridges this gap by offering an AI-driven, standardized platform for product management interview preparation, providing insightful feedback based on real interview dynamics.

## Objectives
- **Simulate Real PM Interviews**: Provide AI-driven, mock interview experiences with realistic questions and scenarios.
- **Standardized, Objective Feedback**: Ensure consistent, data-driven evaluation criteria for candidate responses.
- **Personalized Insights**: Guide candidates on specific improvement areas through AI-based analysis.

## Project Pipeline
ProdPrepAI is organized into key modules:

1. **Data Collection & Preparation**
   - Collects PM interview questions and answers from multiple sources (e.g., web scraping, YouTube transcripts).
   - Generates synthetic data using GPT-4 for comprehensive training.
   - Preprocesses data to create a structured dataset with questions, responses, and evaluation metrics.

2. **Core ML Models**
   - **Response Analyzer**: Uses BERT for scoring candidate responses across criteria such as semantic similarity, coherence, and technical accuracy.
   - **Reinforcement Learning Agent**: Guides interview flow by deciding on follow-up questions or feedback based on response quality.

3. **LLM Integration**
   - Integrates with GPT-4 to generate personalized feedback and improvement suggestions, ensuring an interactive learning experience.

4. **Evaluation & Feedback**
   - Conducts qualitative and quantitative evaluations of responses to help candidates refine their interview skills effectively.

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/prodprepai.git
   cd prodprepai
