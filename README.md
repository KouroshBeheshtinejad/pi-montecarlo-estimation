# 🧮 Monte Carlo Pi Estimation
A simple Python program to estimate the value of **π (Pi)** using the **Monte Carlo method**.

## 📌 How It Works
1. Generate **N** random points `(x, y)` in a unit square.  
2. Count how many points satisfy `x² + y² ≤ 1`.  
3. Estimate π using:  
π ≈ 4 × (points_inside_circle / total_points)

## 🚀 Run
```bash
python pi-montecarlo.py
📊 Example Output
Estimated value of Pi: 3.1415
Error: 0.00009
🎯 Visualization
The program shows a scatter plot of generated points:
Blue → Inside the quarter circle
Red → Outside the quarter circle

👨‍💻 Author
Kourosh Beheshtinejad

📜 License
This project is open-source and free to use.