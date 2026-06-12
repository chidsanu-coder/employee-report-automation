import pandas as pd

df = pd.read_excel('employee_data.xlsx')
#หาเงินเดือนเฉลี่ยของแต่ละแผนก
avg_salary = df.groupby("แผนก")["เงินเดือน"].mean()
#หาพนักงานที่มีเงินเดือนสูงสุด
max_employee = df.loc[df["เงินเดือน"].idxmax()]
#นับจำนวนพนักงานในแต่ละแผนก
employee_count = df.groupby("แผนก")["แผนก"].count().reset_index(name='จำนวนพนักงาน')
with pd.ExcelWriter('employee_report.xlsx') as writer:
    df.to_excel(writer, sheet_name='Employee Data', index=False)
    avg_salary.to_excel(writer, sheet_name='Average Salary')
    max_employee.to_frame().T.to_excel(writer, sheet_name='Highest Salary', index=False)
    employee_count.to_excel(writer, sheet_name='Employee Count')
print("รายงานพนักงานถูกบันทึกในไฟล์ employee_report.xlsx")