# Andos Reviews – Cloud Engineering Project

A full-stack hybrid cloud project that hosts a static anime review website on **Amazon S3** and combines both **serverless services** (API Gateway, Lambda, DynamoDB) and **traditional servers** (EC2 with Rocky Linux, Nginx, Apache).  

This project demonstrates **networking, security, serverless APIs, event-driven design, monitoring, CI/CD automation (Terraform + GitHub Actions + CodePipeline), and containerization with Docker**, using AWS services and open-source tools.

🔗 **Live Site:** [https://www.andosreviews.com](https://www.andosreviews.com)

---

## 🌐 Architecture
![Andos Architecture](docs/andos_week7_architecture_v8.png)

👉 See the detailed **Cloud Engineering Map** (PDF): [docs/andos_reviews_cloud_engineering_map_v9.pdf](docs/andos_reviews_cloud_engineering_map_v9.pdf)

---

## 🛠️ Skills Demonstrated
- **Cloud Networking & Security**: VPC with public/private subnets, NAT Gateway, IAM, Security Groups, Route Tables  
- **Serverless Compute**: AWS Lambda functions (CRUD + Jikan API integration), API Gateway  
- **Data Layer**: DynamoDB for persistent reviews storage  
- **Static Hosting & CDN**: S3 + CloudFront for global static website delivery  
- **CI/CD Automation**: GitHub Actions (staging → EC2, production → S3), CodePipeline (Lambda deployments)  
- **Monitoring & Logging**: CloudWatch metrics/logs, EventBridge events, CloudTrail auditing  
- **Infrastructure as Code**: Terraform modules for VPC, Lambda, API Gateway, and networking  
- **Containers & VMs**: Dockerized experiments (Flask, Nginx), Rocky Linux & Ubuntu VMs for practice  
- **Web Servers**: Nginx & Apache configuration on EC2/VMs  

---

## 📖 Project Journey
This project started with a **beginner-friendly static site** hosted on a Rocky Linux VM using NGINX.  
Over time it was modernized step-by-step into a **cloud-ready architecture**:

1. Static hosting on **S3 + CloudFront**  
2. **Custom domains + HTTPS** with Route 53 + ACM  
3. **Serverless backend** using Lambda, API Gateway, DynamoDB  
4. **CI/CD pipelines** with GitHub Actions + CodePipeline  
5. **Monitoring, security, and automation** using CloudWatch, EventBridge, CloudTrail, IAM, and Terraform  

---

## 🧑‍💻 Why This Project Matters
This project demonstrates the skills expected of a modern **Cloud Engineer / DevOps Engineer**:  
- Designing secure cloud architectures (hybrid of serverless + traditional compute)  
- Automating deployments and infrastructure with CI/CD + IaC  
- Managing networking, security, observability, and scalability end-to-end  

It’s not just an app — it’s a **portfolio piece** to showcase readiness for cloud engineering roles.  
