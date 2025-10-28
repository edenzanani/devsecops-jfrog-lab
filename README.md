
# DevSecOps JFrog Artifactory Lab

## תיאור הפרויקט
בפרויקט זה בוצעה אוטומציה מלאה הכוללת:
- יצירת רפוזיטוריז (docker-local, generic-local) ב־JFrog עם Python.
- בניית Docker Image בענף ראשי בעזרת GitHub Actions.
- סריקה לכל Image עם Trivy — build נעצר בעת גילוי פגיעות HIGH/CRITICAL.
- יצירת SBOM (עם Syft) והעלאה אוטומטית ל־Artifactory.
- טיפול והורדת רמת סיכון ל־build ירוק ע"י שדרוג תלות (Flask לגירסה 2.3.2).
- כלל התהליך מתועד, Evidence בכל שלב.

## שלבי העבודה
### 1. אוטומציה בסקריפט פייתון
- סקריפט create_repos.py רץ מול ממשק REST של JFrog ליצירת הרפוזיטוריז.
- פרטי AUTH נשמרו כסוד בגיטהאב.
- וידוא התהליך בוצע ידנית בפורטל JFrog.

### 2. פייפליין אוטומטי בגיטהאב
- בניית Docker והרצת Trivy אוטומטית (trivy-action@0.10.0).
- build עוצר אוטומטית אם נמצאו פגיעות חמורות.
- טיפול נדרש: עדכון requirements.txt, שדרוג Flask.

### 3. SBOM והעלאה לרפוזיטורי
- ייצור sbom.json ע"י syft כמסמך CycloneDX.
- העלאה ודחיפה לרפוזיטורי generic-local.

### 4. סיכום Evidence ותוצאות
- תיעוד וצילום כל שלב בממשקים (GitHub Actions, JFrog, Syft, Trivy.
.
.

