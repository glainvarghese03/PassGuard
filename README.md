# PassGuard: Password Security Suite
> A Python-based CLI tool to evaluate password strength and generate secure, salted SHA-256 hashes.

## 📖 Overview
PassGuard is a lightweight, command-line cybersecurity tool designed for educational and defensive purposes. It helps users understand password vulnerabilities and demonstrates how to securely store passwords using cryptographic hashing and salting. 

## ✨ Features
- **Password Strength Evaluation:** Analyzes passwords based on length, character complexity (uppercase, lowercase, numbers, symbols), and provides actionable feedback.
- **Secure Hashing (SHA-256):** Generates SHA-256 hashes.
- **Cryptographic Salting:** Uses Python's `secrets` module to generate a random 16-byte salt for every hash, protecting against Rainbow Table attacks.
- **Secure Password Generator:** Generates cryptographically strong random passwords using the `secrets` module.
- **Color-Coded CLI:** Professional terminal interface for easy readability.

## 🛠️ Prerequisites
- Python 3.6 or higher.
- No external libraries are required (uses standard library: `hashlib`, `re`, `secrets`, `string`, `sys`).

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/glainvarghese03/PassGuard.git