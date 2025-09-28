# TP = 90   
# FN = 210  
# FP = 140 
# TN = 9560 
TP = int(input("True Positives: "))
FN = int(input("False Negatives: "))
FP = int(input("False Positives: "))
TN = int(input("True Negatives: "))

Total = TP + FN + FP + TN

# Calculations
sensitivity = TP / (TP + FN)  # Recall
specificity = TN / (TN + FP)
accuracy = (TP + TN) / Total
error_rate = 1 - accuracy
precision = TP / (TP + FP)
recall = sensitivity
f1_score = 2 * (precision * recall) / (precision + recall)

# Print results
print(f"Sensitivity (Recall): {sensitivity}")
print(f"Specificity: {specificity}")
print(f"Accuracy: {accuracy}")
print(f"Error Rate: {error_rate}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1-score: {f1_score}")

