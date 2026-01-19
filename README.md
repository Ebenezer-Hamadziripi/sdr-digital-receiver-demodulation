# SDR Digital Receiver Pipeline

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![NumPy](https://img.shields.io/badge/NumPy-DSP-orange)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Academic_Skeleton-lightgrey)

## 📡 Overview
This project implements a complete **Software Defined Radio (SDR) receiver** capable of demodulating multiple digital modulation schemes from raw I/Q samples.

The pipeline processes a 2.4 MS/s signal containing burst transmissions, performing synchronization, error correction, and symbol decoding to recover ASCII text payloads.

> ### 🔐 Academic Integrity & Full Implementation
**Note:** This repository contains the **architectural skeleton** of the project to comply with university academic integrity policies.

---

## 🚀 Key Features
* **Multi-Modulation Support:** Decodes **OOK**, **BPSK**, **DBPSK**, and **DQPSK**.
* **Carrier Synchronization:**
    * Coarse frequency offset estimation using FFT-based power spectrum analysis.
    * Fine phase tracking using **Costas Loops** and **Decision-Directed Feedback**.
* **Timing Recovery:**
    * Symbol synchronization using clock recovery algorithms to sample at optimal eye-openings.
* **Differential Decoding:**
    * Handles phase ambiguity in DBPSK and DQPSK using differential logic and Gray coding.

---

## 🛠️ System Architecture

The signal processing pipeline follows a standard digital receiver architecture:

```mermaid
graph TD
    A[Raw I/Q Data] -->|Normalization| B[Signal Splicing]
    B --> C{Modulation Type?}
    C -->|BPSK/QPSK| D[Coarse Freq Sync]
    D --> E[Carrier Correction]
    E --> F[Symbol Timing Recovery]
    F --> G[Fine Phase PLL]
    G --> H[Symbol Slicing & Decoding]
    H --> I[ASCII Output]
