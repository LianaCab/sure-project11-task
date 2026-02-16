# Resolving Ambiguity in Visual Question Answering for Accessibility

This project implements an ambiguity-aware Visual Question Answering (VQA) system designed for blind and low-vision users.

The system explicitly surfaces ambiguity and supports two interaction modes:

1. Respond in One Pass – Provides a structured, comprehensive description.
2. Clarify Iteratively – Engages in a multi-turn clarification dialogue.

---

## Features

- Image upload
- Text-based question input
- Ambiguity detection
- Object counting and grouping
- Spatial organization (left/right/top/bottom)
- Accessible UI (ARIA labels, keyboard navigation)
- Two interaction modes

---

## Tech Stack

Backend:
- Flask
- OpenAI Vision API

Frontend:
- HTML
- CSS
- Vanilla JavaScript

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/vqa-ambiguity-accessibility.git
cd vqa-ambiguity-accessibility
