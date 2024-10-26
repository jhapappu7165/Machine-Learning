
from sklearn.utils.class_weight import compute_class_weight

y = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # Example imbalanced target variable
classes = np.unique(y)

class_weights = compute_class_weight(class_weight='balanced', classes=classes, y=y)
class_weight_dict = dict(zip(classes, class_weights))

print(class_weight_dict)
