from django.shortcuts import render
import joblib, numpy as np, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model = joblib.load(os.path.join(BASE_DIR, 'titanic_model.pkl'))
scaler = joblib.load(os.path.join(BASE_DIR, 'scaler.pkl'))

def form_view(request):
    result, prob = None, None
    if request.method == 'POST':
        try:
            pclass = int(request.POST.get('pclass'))
            sex = int(request.POST.get('sex'))
            age = float(request.POST.get('age'))
            fare = float(request.POST.get('fare'))
            X = np.array([[pclass, sex, age, fare]])
            X_scaled = scaler.transform(X)
            prediction = model.predict(X_scaled)[0]
            probability = model.predict_proba(X_scaled)[0][1]
            result = 'Sobrevivió' if prediction == 1 else 'No sobrevivió'
            prob = round(probability * 100, 2)
        except Exception as e:
            result = f"Error: {e}"
    return render(request, 'predictor/form.html', {'result': result, 'prob': prob})
