
import psycopg2
import sys, os
import numpy as np
import pandas as pd
import pandas.io.sql as psql

# Set up a connection to the postgres server.
conn_string = "postgresql://postgres:root@localhost/courier";
conn=psycopg2.connect(conn_string)
print("Connected!")
