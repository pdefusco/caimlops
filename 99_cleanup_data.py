#****************************************************************************
# (C) Cloudera, Inc. 2020-2023
#  All rights reserved.
#
#  Applicable Open Source License: GNU Affero General Public License v3.0
#
#  NOTE: Cloudera open source products are modular software products
#  made up of hundreds of individual components, each of which was
#  individually copyrighted.  Each Cloudera open source product is a
#  collective work under U.S. Copyright Law. Your license to use the
#  collective work is as provided in your written agreement with
#  Cloudera.  Used apart from the collective work, this file is
#  licensed for your use pursuant to the open source license
#  identified above.
#
#  This code is provided to you pursuant a written agreement with
#  (i) Cloudera, Inc. or (ii) a third-party authorized to distribute
#  this code. If you do not have a written agreement with Cloudera nor
#  with an authorized and properly licensed third party, you do not
#  have any rights to access nor to use this code.
#
#  Absent a written agreement with Cloudera, Inc. (“Cloudera”) to the
#  contrary, A) CLOUDERA PROVIDES THIS CODE TO YOU WITHOUT WARRANTIES OF ANY
#  KIND; (B) CLOUDERA DISCLAIMS ANY AND ALL EXPRESS AND IMPLIED
#  WARRANTIES WITH RESPECT TO THIS CODE, INCLUDING BUT NOT LIMITED TO
#  IMPLIED WARRANTIES OF TITLE, NON-INFRINGEMENT, MERCHANTABILITY AND
#  FITNESS FOR A PARTICULAR PURPOSE; (C) CLOUDERA IS NOT LIABLE TO YOU,
#  AND WILL NOT DEFEND, INDEMNIFY, NOR HOLD YOU HARMLESS FOR ANY CLAIMS
#  ARISING FROM OR RELATED TO THE CODE; AND (D)WITH RESPECT TO YOUR EXERCISE
#  OF ANY RIGHTS GRANTED TO YOU FOR THE CODE, CLOUDERA IS NOT LIABLE FOR ANY
#  DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, PUNITIVE OR
#  CONSEQUENTIAL DAMAGES INCLUDING, BUT NOT LIMITED TO, DAMAGES
#  RELATED TO LOST REVENUE, LOST PROFITS, LOSS OF INCOME, LOSS OF
#  BUSINESS ADVANTAGE OR UNAVAILABILITY, OR LOSS OR CORRUPTION OF
#  DATA.
#
# #  Author(s): Paul de Fusco, Manoj Jain
#***************************************************************************/

import os
import numpy as np
import pandas as pd
from datetime import datetime
from pyspark.sql.types import LongType, IntegerType, StringType
from pyspark.sql import SparkSession

class TelcoDataGen:

    '''Class to Generate Telco Data'''

    def __init__(self, username, dbname, datalake_directory):
        self.username = username
        self.dbname = dbname
        self.datalake_directory = datalake_directory


    def createSparkSession(self):
        """
        Method to create a Spark Connection using CML Data Connections
        """

        spark = (SparkSession.builder.appName("MyApp")\
          .config("spark.jars", "/opt/spark/optional-lib/iceberg-spark-runtime.jar")\
          .config("spark.sql.hive.hwc.execution.mode", "spark")\
          .config("spark.sql.extensions", "com.qubole.spark.hiveacid.HiveAcidAutoConvertExtension, org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions")\
          .config("spark.sql.catalog.spark_catalog.type", "hive")\
          .config("spark.sql.catalog.spark_catalog", "org.apache.iceberg.spark.SparkSessionCatalog")\
          .config("spark.yarn.access.hadoopFileSystems", self.datalake_directory)\
          .getOrCreate()
          )

        return spark


    def deleteTableAndDatabase(self, spark):
        """
        Method to create database before data generated is saved to new database and table
        """
        spark.sql("DROP TABLE IF EXISTS {0}.TELCO_CELL_TOWERS_{1}".format(self.dbname, self.username))
        spark.sql("DROP DATABASE IF EXISTS {} ".format(self.dbname))

        return spark

def main():

    USERNAME = os.environ["PROJECT_OWNER"]
    DBNAME = "TELCO_MLOPS_"+USERNAME
    DATALAKE_DIRECTORY = "hdfs://nameservice1" #Modify as needed

    # Instantiate BankDataGen class
    dg = TelcoDataGen(USERNAME, DBNAME, DATALAKE_DIRECTORY)

    # Create CML Spark Connection
    spark = dg.createSparkSession()

    df=dg.deleteTableAndDatabase(spark)

if __name__ == '__main__':
    main()
