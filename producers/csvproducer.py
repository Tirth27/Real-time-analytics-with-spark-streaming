import pandas as pd
from confluent_kafka import Producer
import json
import time
from datetime import datetime
import sys
import argparse
import gdown
import os

def convert_to_json(dictionary, encoder):
    '''
    It converts a dictionary into a json string according to the encoder provided
    '''
    return json.dumps(dictionary).encode(encoder)

def callback(error, message):
    '''
    It returns Error or Sucess when producing data
    '''
    if error:
        print(f"Error: {message.value()}: {error.str()}")
    else:
        print(f"Sucess: {message.value()}")

def main(args):
    # Check if data directory exists
    output_dir = os.path.dirname(args.output)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Download data
    gdown.download(args.url, args.output, quiet=True)

    # Read data. If it has headers use it. If not, use the provided by the user
    if args.headers:
        df = pd.read_csv(args.output, encoder=args.encoder)
    else:
        # Split the column names provided by the user
        columns = args.names.split(",")
        df = pd.read_csv(args.output, header = 0, names = columns, encoding = args.encoder)

    # Create producer
    p = Producer({'bootstrap.servers': 'broker:29092'})

    # Start producing
    for index, row in df.iterrows():
        row = row.to_dict()
        p.produce(args.topic, value=convert_to_json(row, args.encoder), key=str(row[args.idcol]), callback=callback)
        p.flush()
        time.sleep(args.delay/1000)

def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--topic', type=str, default="mytopic") # Name of the topic
    parser.add_argument('--url', type=str), # CVS url
    parser.add_argument('--output', type=str), # Path to store the csv
    parser.add_argument('--encoder', type=str, default="utf-8'"), # Encoder
    parser.add_argument('--headers', type=str2bool, default="true"), # If the csv has headers or not
    parser.add_argument('--names', type=str), # Column names separated by comma
    parser.add_argument('--idcol', type=str), # Column that contains the id
    parser.add_argument('--delay', type=int), # Delay in miliseconds

    args = parser.parse_args()

    main(args)
    






