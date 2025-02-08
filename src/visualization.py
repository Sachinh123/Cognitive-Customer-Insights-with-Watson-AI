import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_sentiment_distribution(file_path):
    """Visualizes sentiment distribution."""
    df = pd.read_csv(file_path)
    
    # Ensure 'sentiment' column exists
    if 'sentiment' in df.columns:
        sns.countplot(x="sentence", data=df)
        plt.title("Customer Sentiment Distribution")
        plt.show()
    else:
        print("The 'sentiment' column is missing in the dataset.")

if __name__ == "__main__":
    plot_sentiment_distribution("../data/data.csv")
