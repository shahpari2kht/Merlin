# Merlin | Intelligent Data Wizard

Automated data‑preprocessing suite for Data Scientists.  
ابزار خودکار پیش‌پردازش داده، طراحی‌شده برای دانشمندان داده.

---

## Features | ویژگی‌ها  
- Data cleaning and transformation tools  
  ابزارهایی برای پاک‌سازی و تبدیل داده‌ها  
- Basic model training templates  
  قالب‌های پایه برای آموزش مدل  
- Integration with pandas / scikit‑learn pipelines  
  ادغام با pandas و scikit‑learn برای جریان کاری آماده

---

## Installation | نصب  
```bash
pip install -r requirements.txt
or if packaged:

pip install merlin‑datawizard

Usage | نحوه استفاده
import merlin
df = merlin.load_data("data.csv")
df_clean = merlin.clean(df)
model = merlin.train_model(df_clean, target="y")


Example output:

Cleaning completed: 1234 rows processed  
Model training completed: accuracy = 0.87

Architecture | ساختار

The library uses a modular design:

merlin.clean: for data cleaning

merlin.transform: for feature engineering

merlin.model: for training/evaluation
پوشه‌ها با ماژول‌های مستقل برای تمیزکاری، مهندسی ویژگی‌ها و مدل‌سازی سازماندهی شده‌اند.

Contributing | همکاری

Contributions are welcome! Please follow the steps:

Fork the repository

Create a new feature branch

Write tests and update documentation

Submit a pull request
(لطفاً مستند CONTRIBUTING.md را مطالعه کنید.)

License | مجوز

This project is licensed under the MIT License – see the LICENSE
 file for details.
این پروژه تحت مجوز MIT است – برای جزئیات به فایل LICENSE مراجعه کنید.

About Me | درباره من

Hi, I'm Parisa Mohammadzadeh (پریسا محمدزاده).
I’m building tools at the intersection of data, technology & humanity.
فارغ‌التحصیل مهندسی نفت و ریاضیات کاربردی، علاقه‌مند به علم داده و برنامه‌نویسی.
📬 Contact: LinkedIn
 | GitHub
 | Shahpari2kht@gmail.com
