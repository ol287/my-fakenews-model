import matplotlib.pyplot as plt

# Define actual K-Fold scores from the cross-validation process (replace with real values if available)
accuracy_scores = [0.85, 0.87, 0.86, 0.88, 0.84]  # Placeholder values
f1_scores = [0.83, 0.85, 0.84, 0.86, 0.82]  # Placeholder values
auc_scores = [0.89, 0.91, 0.90, 0.92, 0.88]  # Placeholder values

# Define the number of folds dynamically
k_folds = list(range(1, len(accuracy_scores) + 1))

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(k_folds, accuracy_scores, marker='o', label="Accuracy", linestyle='-', linewidth=2)
plt.plot(k_folds, f1_scores, marker='s', label="F1 Score", linestyle='--', linewidth=2)
plt.plot(k_folds, auc_scores, marker='d', label="AUC-ROC", linestyle='-.', linewidth=2)

# Set x-axis scale to increment by 1
plt.xticks(k_folds)  # Ensures only whole numbers appear on the x-axis

# Add labels and title
plt.xlabel("K-Fold Iteration", fontsize=12)
plt.ylabel("Score", fontsize=12)
plt.title("K-Fold Cross Validation Performance", fontsize=14, fontweight='bold')

# Improve visualization
plt.legend(fontsize=12)
plt.grid(True, linestyle="--", alpha=0.6)
plt.ylim(min(min(accuracy_scores), min(f1_scores), min(auc_scores)) - 0.02, 1.0)  # Adjust y-axis range

# Show the plot
plt.show()
