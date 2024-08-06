# Running this script will generate the dataset and save it as techsavvy_ab_test_data.csv in the current working directory.

```python
import pandas as pd
import numpy as np

# Set the random seed for reproducibility
np.random.seed(42)

# Number of users
n_users = 10000

# Simulate the data
data = {
    'user_id': range(1, n_users + 1),
    'group': np.random.choice(['A', 'B'], n_users),
    'timestamp': pd.date_range(start='2024-07-01', periods=n_users, freq='T'),
    'clicked_add_to_cart': np.random.binomial(1, 0.1, n_users),
    'session_duration': np.random.normal(50, 10, n_users).astype(int)
}

# Adjust probabilities for treatment group (B)
treatment_mask = (data['group'] == 'B')
data['clicked_add_to_cart'][treatment_mask] = np.random.binomial(1, 0.12, treatment_mask.sum())
data['session_duration'][treatment_mask] += 5

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('techsavvy_ab_test_data.csv', index=False)
