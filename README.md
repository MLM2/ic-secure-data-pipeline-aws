# ic-secure-data-pipeline-aws

Serverless AWS data pipeline demonstrating secure ingestion, processing, and storage using S3, Lambda, and event-driven architecture aligned to IC-style mission workflows.

---

## 🧠 Architecture

![AWS Data Pipeline Architecture](architecture/architecture.png)

---

## ⚙️ How It Works

1. User uploads JSON data to S3 Raw Bucket  
2. S3 triggers AWS Lambda via event notification (ObjectCreated)  
3. Lambda processes and transforms the data  
4. Output is written to S3 Processed Bucket  
5. Execution logs are captured in CloudWatch  

---

## 🧪 Example

### Input
```json
{
  "mission": "space",
  "source": "MASINT",

### Output

```json
{
  "mission": "space",
  "source": "MASINT",
  "confidence": 0.95,
  "processed": true
}
  "confidence": 0.95
}


---

## 🧠 Why this matters

It shows:

👉 **transformation logic**

Without it, a reviewer has to *guess* what your system does.

---

# 🚀 UPGRADE 2 — ADD “TECH STACK” (VERY HIGH SIGNAL)

Add this section ABOVE “How It Works”:

```markdown
## ⚙️ Tech Stack

- Amazon S3 (data ingestion and storage)
- AWS Lambda (serverless processing)
- AWS IAM (access control)
- Amazon CloudWatch (logging and monitoring)

---

## 🧠 Why This Matters

This project demonstrates a real-world event-driven architecture pattern used in cloud-based data pipelines, where services are loosely coupled and triggered by events rather than direct calls.
