import pandas as pd

# Load quiz file
df = pd.read_csv("docs/brier_quiz.csv")

# Ensure 'correct' is boolean
df["correct"] = df["correct"].astype(bool)

# Compute squared error for each prediction
df["squared_error"] = (df["confidence"] - df["correct"].astype(int)) ** 2

# Compute Brier score
brier_score = df["squared_error"].mean()

# Print summary
print("📊 Brier Calibration Report")
print("----------------------------")
print(f"Brier Score: {brier_score:.4f}")
print("\nDetailed Results:")
print(df[["question", "confidence", "correct", "squared_error"]])
