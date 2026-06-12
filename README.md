# Employee Report Automation 👥

สคริปต์ Python สำหรับสรุปข้อมูลพนักงานจากไฟล์ Excel อัตโนมัติ

## ทำอะไรได้บ้าง
- หาเงินเดือนเฉลี่ยแยกตามแผนก
- หาพนักงานที่มีเงินเดือนสูงสุด
- นับจำนวนพนักงานในแต่ละแผนก
- Export รายงานเป็น Excel อัตโนมัติ 4 Sheet

## วิธีใช้งาน
1. วางไฟล์ employee_data.xlsx ในโฟลเดอร์เดียวกับ employee_report.py
2. รันคำสั่ง python employee_report.py
3. เปิดไฟล์ employee_report.xlsx ดูผลลัพธ์ได้เลย

## ติดตั้ง Library
pip install pandas

## ผลลัพธ์ที่ได้
| Sheet | รายละเอียด |
|---|---|
| Employee Data | ข้อมูลพนักงานทั้งหมด |
| Average Salary | เงินเดือนเฉลี่ยแต่ละแผนก |
| Highest Salary | พนักงานเงินเดือนสูงสุด |
| Employee Count | จำนวนพนักงานแต่ละแผนก |

## ✅ รองรับข้อมูลได้ไม่จำกัดจำนวนแถว
## ✅ ทดสอบกับข้อมูลจริงแล้ว

## Tech Stack
- Python 3
- pandas
