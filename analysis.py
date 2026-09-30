import pandas as pd               #استدعاء المكتبة المسؤولة عن تحليل البيانات
import matplotlib.pyplot as plt   #استدعاء مكتبة التمثيل والرسم البياني

#==========================================================

df = pd.read_csv("Project_Data_Analysis/StudentPerformanceFactors.csv")  #csv قراءة البيانات من ملف 

#==========================================================
print(df.head())         #طباعة أول خمس صفوف

print("=" * 50)  
#==========================================================
print(df.info())        #(اسماء الاعمدة,نوع بيانات كل عمود,.....)طباعة معلومات عامة عن الملف

print("=" * 50)
#==========================================================
print(df.describe())    #(الوسط الحسابي,الانحراف المعياري,.....)طباعة بيانات احصائية عامة

print("=" * 50)
#==========================================================
print(df.isnull().sum())  #طباعة عدد القيم الفارغة لكل عامود

print("=" * 50)
#==========================================================
#================ معالجة البيانات الفارغة  ==============
#==========================================================
df['Teacher_Quality'] = df['Teacher_Quality'].fillna("undefined")
df['Parental_Education_Level'] = df['Parental_Education_Level'].fillna("undefined")
df['Distance_from_Home'] = df['Distance_from_Home'].fillna("undefined")
#==========================================================
print(f"The mean for all students is: {df['Exam_Score'].mean():.3f}")  
#طباعة الوسط الحسابي لمعدلات جميع الطلاب مع التقريب لثلاث منازل عشرية

print("=" * 50)
#==========================================================
cor = df['Hours_Studied'].corr(df['Exam_Score'])#حساب معامل الارتباط بين ساعات الدراسة و المعدل

print(f"Correlation between (Hours_Studied, Exam_Score) = {cor:.5f}") #طباعة معامل الارتباط

if cor > 0.7:  #شرط يفحص قوة معامل الارتباط
    print("Strong Correlation.")
elif cor > 0.4:
    print("Medium Correlation.")    
else:
    print("Low Correlation.")

print("=" * 50)
#==========================================================

print(df.groupby('Parental_Involvement')['Exam_Score'].mean().sort_values(ascending=False))
#حساب المعدل لكل فئة من فئات مستوى الدعم العائلي و ترتب النتيجة تنازليا

#==========================================================
plt.hist(df['Exam_Score'],bins=20,color="#e74c3c") #عمل رسمة مدرج تكراري مع 20 شريط

plt.title("Exam_Score vs Students")  #وضع عنوان للرسمة
plt.xlabel("Grades")                 #وضع عنوان لمحور السينات
plt.ylabel("Stu_Number")             #وضع عنوان لمحور الصادات
plt.grid(True)                       #اضافة شبكة خلفية

plt.show()                           #عرض الرسمة
#==========================================================
plt.scatter(df['Hours_Studied'], df['Exam_Score'], color="Indigo")   #عمل رسمة نقاط مبعثرة

plt.title("Hours Studied vs Exam Score")  #وضع عنوان للرسمة
plt.xlabel("Hours Studied")               #وضع عنوان لمحور السينات
plt.ylabel("Exam Score")                  #وضع عنوان لمحور الصادات
plt.grid(True)                            #اضافة شبكة خلفية

plt.show()                                #عرض الرسمة
#==========================================================
df['Attendance_Groups'] = pd.cut(df['Attendance'], bins=3, labels=['Low', 'Medium', 'High'])
                          #تقسيم عامود الحضور الى ثلاث فئات

attendance_means = df.groupby('Attendance_Groups')['Exam_Score'].mean()
#حساب الوسط الحسابي للمعدلات حسب مستويات الحضور

plt.bar(attendance_means.index, attendance_means.values, color="#09cdefff", edgecolor="black", width=0.8)
#عمل رسمة اعمدة

plt.title("Average Exam Score vs Attendance Level")  #وضع عنوان للرسمة
plt.xlabel("Attendance Level")                       #وضع عنوان لمحور السينات
plt.ylabel("Average Exam Score")                     #وضع عنوان لمحور الصادات
plt.grid(True, axis='y')                             #اضافة شبكة خلفية بدون خطوط عمودية
plt.ylim(0, 80)                                      #وضع حدود للرسمة من 0 الى 80

plt.show()                                           #عرض الرسمة
#==========================================================
gender_means = df.groupby('Gender')['Exam_Score'].mean()
#حساب الوسط الحسابي للمعدلات حسب الجنس

plt.bar(gender_means.index,gender_means.values,color="#c70eff",width=0.4)
#عمل رسمة اعمدة

plt.title("Average Exam Score vs Gender")       #وضع عنوان للرسمة
plt.xlabel("Gender")                            #وضع عنوان لمحور السينات
plt.ylabel("Average Exam Score")                #وضع عنوان لمحور الصادات
plt.grid(True, axis='y')                        #اضافة شبكة خلفية بدون خطوط عمودية
plt.ylim(0, 80)                                 #وضع حدود للرسمة من 0 الى 80

plt.show()                                      #عرض الرسمة
#==========================================================
plt.scatter(df['Sleep_Hours'],df['Exam_Score'],color="#460eff")
#عمل رسمة نقاط مبعثرة

plt.title("Exam Score vs Sleep Hours")      #وضع عنوان للرسمة
plt.xlabel("Sleep_Hours")                   #وضع عنوان لمحور السينات
plt.ylabel("Exam Score")                    #وضع عنوان لمحور الصادات
plt.grid(True)                              #اضافة شبكة خلفية

plt.show()                                  #عرض الرسمة
#==========================================================

print("1. There is a clear positive relationship between hours studied and exam scores.")
print("2. Attendance levels directly effect positivly on student results.")
print("3. Higher parental involvement is positively associated with better student performance.")
print("4. There is no significant difference in average exam scores between male and female students.")
print("5. Educational strategies should prioritize improving attendance and encouraging dedicated study hours.")

#========================The End==========================#