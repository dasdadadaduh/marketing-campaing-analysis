import matplotlib.pyplot as plt
import seaborn as sns

def plot_channel_performance(df):
    """Visualize ROI across different marketing channels."""
    plt.figure(figsize=(10,6))
    sns.barplot(x='Channel', y='ROI', data=df)
    plt.title("Marketing Channel ROI")
    plt.show()
