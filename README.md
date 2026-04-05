# 🚀 Real-Time Financial Fraud Detection Pipeline

![Project Demo](fraudDetection.gif)

## 📌 Project Overview
In the financial sector, detecting fraudulent transactions using end-of-day batch processing is no longer sufficient; anomalies must be caught in milliseconds. 

This project is an end-to-end **Real-Time Data Engineering Pipeline** built entirely within **Microsoft Fabric**. It ingests continuous, high-velocity streaming data (simulated Point-of-Sale transactions), analyzes it for fraudulent patterns using Kusto Query Language (KQL), visualizes the spikes with zero latency, and triggers automated email alerts to security teams—all without human intervention.

## 🏗️ Architecture & Data Flow

This pipeline shifts away from traditional ETL toward an **Event-Driven Streaming Architecture**.

```text
[🐍 Python POS Simulator]  --> Generates 10,000+ live transactions/hr (Normal & Fraud).
       ⬇
[⚡ Fabric Eventstreams]   --> Captures and routes the high-velocity telemetry data.
       ⬇
[🗄️ KQL Database]          --> Ingests streams into an Eventhouse for sub-second querying.
       ⬇
[📊 Power BI Direct Lake]  --> Auto-refreshing dashboard monitoring fraud in real-time.
       ⬇
[🚨 Data Activator]        --> Evaluates KQL stream and triggers automated Email Alerts.
