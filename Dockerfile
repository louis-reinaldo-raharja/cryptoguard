# Use an official Python runtime as the base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install poetry

# Create pyproject.toml
RUN poetry init --no-interaction --name=your-project-name --author="Your Name <your@email.com>"

# Add dependencies
RUN poetry add streamlit plotly web3 requests openai langchain langchain-community elasticsearch numpy pandas scikit-learn

# Install project dependencies
RUN poetry install --no-dev

# Copy the Streamlit app and specific scripts
COPY app.py .
COPY scripts/ scripts/
COPY images/ images/


# Expose the port that Streamlit will run on
EXPOSE 8501

# Set the command to run the Streamlit app
CMD ["poetry", "run", "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]