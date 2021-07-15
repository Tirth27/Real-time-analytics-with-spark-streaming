# Tweets-Streaming

This repo has all the files needed to run a sentiment analysis on data produced by the Twitter API. It also has some additional visualisations to enrich the analysis.

## Installation

Clone the repo and create the images and containers with the following:

```bash
docker-compose up -d
```

If you want to install additional applications or python packages change the `./Dockerfile` file.

### Accessing Confluent Control Center

To access Confluent control center go to [http://localhost:9021/](http://localhost:9021/) in your browser.

### Accessing Jupyter Lab

To access Jupyter Lab write the following in your console:

```bash
docker logs --tail 50 jupyter_docker_lab_8
```

Then, click on the last Jupyter URL.

## Retrain the model

The model trained by us is stored in the `./models` folder. If you want to retrain the model you need to run the `./01 Sentiment Analysis Model.ipynb` file in a Jupyter Notebook using the `Jupyter` container.

The script will download the Sentiment 140 dataset and start sending it as messages to a Kafka topic. Then, it will stream that topic and create a parquet file, which will be used to train the model.

## Connect to the Twitter API

Run the cells on the `./02 Connection Streams Tables.ipynb`, which will creates the Twitter API connection and additional streams, tables and topics on Confluent.

To modify the Twitter API connection, change the parameters in the `configs/twitterConnector.json` file before running the `./02 Connection Streams Tables.ipynb` script.

## Tweets by location

Run the cells on the `./03 Country Window Stream.ipynb`, which will creates a table with the number of tweets per country in a two minute window.

You need to do the `Connect to the Twitter API` step first.

## Tweets wordcloud

Run the cells on the `./04 Wordcloud Stream.ipynb`, which will creates a wordcloud with the most used hashtags in the last hour.

You need to do the `Connect to the Twitter API` step first.

## Inference data stream

Run the cells on the `./05 Sentiment Analysis Stream.ipynb`, which will creates a new topic with the sentiment of each english tweet.

You need to do the `Connect to the Twitter API` step first.

# Authors
De la Carrera Garcia, Javiera \
Leriche, Sandra \
Monroy Morales, Felipe \
Patel, Tirth

# Credits
Go, A., Bhayani, R. and Huang, L., 2009. Twitter sentiment classification using distant supervision. CS224N Project Report, Stanford, 1(2009), p.12.

