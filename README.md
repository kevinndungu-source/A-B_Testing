# A | B Testing

## A/B Testing for Improving User Engagement at **TechSavvy Inc.**

### Introduction

In today's competitive e-commerce landscape, user engagement is crucial for driving sales and customer loyalty. **TechSavvy Inc.**, a fictional online retailer of tech gadgets, noticed a decline in user engagement on their product pages. The company wanted to explore whether changing the **"Add to Cart"** button color from blue to green would increase user engagement and conversions.

I, Kevin, an experienced AWS Certified Solutions Architect and Data Analyst, was brought in to tackle this problem. Leveraging my expertise in A/B testing, data analysis, and business intelligence, I devised a comprehensive plan to address TechSavvy Inc.'s challenge.


### Understanding the Problem

**TechSavvy Inc.** had observed that users were spending less time on product pages and that the click-through rate for the "Add to Cart" button had decreased. The goal was to test a hypothesis: would a green "Add to Cart" button capture more user attention and encourage more clicks compared to the existing blue button?

**Objective**: Increase user engagement and conversion rates by optimizing the "Add to Cart" button color.

---
>### Definitions
>
>1. **A/B Testing**: A method of comparing two versions of a webpage or app against each other to determine which one performs better.
>
>2. **Control Group (Group A)**: The group that experiences the original version of the product or feature.
>
>3. **Treatment Group (Group B)**: The group that experiences the modified version of the product or feature.
>
>4. **Conversion Rate**: The percentage of users who complete a desired action (e.g., clicking the "Add to Cart" button).
>
>5. **T-Test**: A statistical test used to determine if there are significant differences between the means of two groups.
>
>6. **Chi-Square Test**: A statistical test used to determine if there is a significant association between two categorical variables.
>
>7. **P-Value**: The probability that the observed results are due to chance. A low p-value (typically < 0.05) indicates that the results are statistically significant.
>
>8. **Null Hypothesis**: The hypothesis that there is no effect or difference. In A/B testing, it assumes that any observed difference between the control and treatment groups is due to random chance.
>
>9. **Alternative Hypothesis**: The hypothesis that there is an effect or difference. In A/B testing, it assumes that any observed difference between the control and treatment groups is due to the change being tested.

---

## Step-by-Step Solution

### 1. **Define Hypothesis**

I proposed the following hypothesis:
- **Null Hypothesis (H0)**: Changing the button color has no effect on user engagement.
- **Alternative Hypothesis (H1)**: Changing the button color increases user engagement.



### 2. **Design the Experiment**

I designed an A/B test to compare two versions of the product page:
- **Version A (Control)**: Product page with a blue "Add to Cart" button.
- **Version B (Treatment)**: Product page with a green "Add to Cart" button.

Users would be randomly assigned to one of the two versions to ensure unbiased results.



### 3. **Simulate Data Collection**

To prepare for the experiment, I simulated a dataset representing user interactions. The dataset included:
- `user_id`: Unique identifier for each user.
- `group`: Indicates whether the user is in the control group (A) or the treatment group (B).
- `timestamp`: The time when the user visited the product page.
- `clicked_add_to_cart`: A binary variable indicating whether the user clicked the "Add to Cart" button.
- `session_duration`: Duration of the user's session on the product page in seconds.

```python
# Import necessary libraries
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# Simulate data
np.random.seed(42)
n_users = 10000
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

df = pd.DataFrame(data)
```


### 4. **Analyze the Results**

I calculated the conversion rates and performed statistical tests to compare the engagement rates between the two groups.

```python
# Calculate conversion rates
conversion_A = df[df['group'] == 'A']['clicked_add_to_cart'].mean()
conversion_B = df[df['group'] == 'B']['clicked_add_to_cart'].mean()

# Perform t-test
t_stat, p_value_ttest = stats.ttest_ind(
    df[df['group'] == 'A']['clicked_add_to_cart'],
    df[df['group'] == 'B']['clicked_add_to_cart']
)

# Perform chi-square test
contingency_table = pd.crosstab(df['group'], df['clicked_add_to_cart'])
chi2_stat, p_value_chi2, _, _ = stats.chi2_contingency(contingency_table)

print(f"Conversion Rate A: {conversion_A:.2f}")
print(f"Conversion Rate B: {conversion_B:.2f}")
print(f"T-Statistic: {t_stat:.2f}")
print(f"P-Value (t-test): {p_value_ttest:.4f}")
print(f"Chi-Square Statistic: {chi2_stat:.2f}")
print(f"P-Value (chi-square): {p_value_chi2:.4f}")
```


### 5. **Visualize the Findings**

I created visualizations to illustrate the differences in conversion rates and session durations between the two groups.


```python
# Visualization
plt.figure(figsize=(12, 6))

# Conversion rates
plt.subplot(1, 2, 1)
sns.barplot(x='group', y='clicked_add_to_cart', data=df, ci=None)
plt.title('Conversion Rate by Group')
plt.xlabel('Group')
plt.ylabel('Conversion Rate')

# Session durations
plt.subplot(1, 2, 2)
sns.boxplot(x='group', y='session_duration', data=df)
plt.title('Session Duration by Group')
plt.xlabel('Group')
plt.ylabel('Session Duration (seconds)')

plt.tight_layout()
plt.show()
```


### 6. **Draw Conclusions**

Based on the statistical analysis, I determined whether the change in button color had a significant effect on user engagement.

```python
# Conclusion
alpha = 0.05
if p_value_ttest < alpha and p_value_chi2 < alpha:
    print("Reject the null hypothesis. The button color change has a significant effect on user engagement.")
else:
    print("Fail to reject the null hypothesis. The button color change does not have a significant effect on user engagement.")
```


### **Impact and Insights**

Through this A/B testing project, I demonstrated my ability to:

- Identify and define a problem: Addressing the decline in user engagement.

- Design an experiment: Creating a robust A/B test to gather meaningful data.

- Analyze data: Using statistical methods to derive insights from user interactions.Visualize findings: Effectively communicating results through visualizations.

- Draw actionable conclusions: Providing evidence-based recommendations for improving user engagement.

By adopting this structured approach, TechSavvy Inc. gained valuable insights into user behavior, enabling them to make data-driven decisions to enhance their product pages and boost overall engagement.


>**NB:** *TechSavvy Inc.* is a fictional company created for the purpose of this A/B testing project demonstration.

---

