# Spark
## HDFS, Impala, Jupyter
<hr>

## Vstup

- Pomocí Spark.sql poslat select na libovolnou LinFada tabulku a vytvořit tempView.
- CSV file (třeba Titanic)
<hr>

## Výstup

Jupyter notebook na GIT/email.
<hr>

## Tasky:

1) Data z tempView uložit do df
2) Vypsat schema df
3) Zobrazit df (vyzkoušet truncate), vypsat počet řádků 
<hr>

4) Načíst přiložený CSV file s předem nadefinovaným schématem pomocí StructType (s hlavičkou, delimiterem)
5) Načíst přiložený CSV file s předem nadefinovaným schématem pomocí DDL stringu
6) Načíst přiložený CSV file za pomoci inferSchema (porovnat s ostatníma)
<hr>

7) Využití selectu na více sloupců se vstupem jako string, pyspark.sql.functions.col, colRegex
8) Vyselectit všechny sloupce, pouze prvních 5 indexů, selectExpr
9) Využití funkce filter, negace podmínky, && + ||, isin, contains, endswitch, like, array_contains 
10) Funkce where
<hr>

11) Vytvořit/přejmenovat sloupce s withColumnRenamed, withColumn
12) Využít Drop, dropDuplicates (subset)
13) Projít si agregace pomocí groupBy (agg,avg, count, sum)
14) Řadit df za pomoci Sort, orderBy
15) Zkusit si distinct, limit
<hr>

16) Join dvou dataframů (inner, left, outer, semi - hlavně jak fungují)
17) Cast data typů
18) Collect, explode, split, lit
19) Spark UDF - zkusit si aplikovat jednu funkci
<hr>

20) Uložit jako Parquet s partition
21) Stáhnout Parquet file z HDFS pomocí Jupyteru

Teorie:
- Co je a kdy se používá broadcast
- Rozdíl mezi cache a persist
- repartition x coalesce, partitionBy
- Cluster, client, local


### *pyspark.ml

Nad stejnym df si zkusit:

- StringIndexer
- OneHotEncoder
- VectorIndexer
- VectorAssembler
- Pipeline
- RandomForest (regressor)
- RegressionEvaluator
- +MlFlow (log_metric, log_param, log_model) - TBD na lokálu


