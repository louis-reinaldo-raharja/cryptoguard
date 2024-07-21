# Use an official Python runtime as the base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

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
RUN poetry init --no-interaction --name=cryptoguard --author="louis reinaldo <louisreinaldo@gmail.com>"

# Add dependencies
RUN poetry add streamlit plotly web3 requests openai langchain langchain-community elasticsearch "numpy<2.0.0" pandas scikit-learn

# Install project dependencies
RUN poetry install --no-dev

# Copy the Streamlit app and specific scripts
COPY scripts/ scripts/
COPY images/ images/



# Expose the port that Streamlit will run on
EXPOSE 8505

# Set the command to run the Streamlit app
CMD ["poetry", "run", "streamlit", "run", "scripts/app.py", "--server.port=8505", "--server.address=0.0.0.0"]