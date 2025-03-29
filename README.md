# Cryptographic Analysis Tool

Analyzes various cryptographic algorithms, including caesar cipher, frequency analysis and bigram analysis.

## Introduction

This repository contains a Python-based cryptographic analysis tool designed to assist in the analysis and decryption of ciphertext. The tool performs several analyses on encrypted texts, including frequency analysis, calculation of the Index of Coincidence, Caesar cipher brute force decryption, bigram frequency analysis and chi-squared analysis to suggest the best Caesar shift.

## Features

- **Frequency Analysis:** Computes the relative frequency of each letter in the ciphertext.
- **Index of Coincidence:** Calculates the likelihood two randomly selected letters from the text are identical, which can help determine if a monoalphabetic substitution cipher is in use.
- **Caesar Cipher Brute Force:** Attempts all 26 possible shifts of a Caesar cipher and displays the decrypted output.
- **Bigram Analysis:** Analyzes two-letter combinations and computes their relative frequencies.
- **Chi-Squared Analysis for Caesar Cipher:** Uses chi-squared statistics to evaluate the likelihood of each Caesar cipher shift and identifies the most likely decryption.
- **Logging:** Uses Python’s built-in logging module to track the tool’s progress and key events.
- **Output File:** Aggregates all analysis results into a single output file for easy review.
