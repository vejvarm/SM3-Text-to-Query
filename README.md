# SM3-Text-to-Query: <ins>S</ins>ynthetic <ins>M</ins>ulti-<ins>M</ins>odel <ins>M</ins>edical Text-to-Query Benchmark

This repository contains both the data and code for:

**SM3-Text-to-Query: Synthetic Multi-Model Medical Text-to-Query Benchmark**   
Authors: Sithursan Sivasubramaniam, Cedric Osei-Akoto, Yi Zhang, Kurt Stockinger, Jonathan Fürst   
**Contact: jonathan.fuerst@zhaw.ch**

This work will be presented at [NeurIPS 2024](https://neurips.cc/virtual/2024/poster/97708).
**Please cite our work if you use our data or code.**

```
@misc{sivasubramaniam2024sm3texttoquerysyntheticmultimodelmedical,
      title={SM3-Text-to-Query: Synthetic Multi-Model Medical Text-to-Query Benchmark}, 
      author={Sithursan Sivasubramaniam and Cedric Osei-Akoto and Yi Zhang and Kurt Stockinger and Jonathan Fuerst},
      year={2024},
      eprint={2411.05521},
      archivePrefix={arXiv},
      primaryClass={cs.DB},
      url={https://arxiv.org/abs/2411.05521}, 
}
```

**Note: This repository will be updated further during the next week to make it easier to set up and use the four different databases.**

## Data

- `./data/synthea_database` contains the Synthea data used as the basis for PostgreSQL, Graph DB (RDF), Neo4j, and MongoDB.
- `./data/dataset/train_dev`contains the annotated
  train and dev splits for all four query languages: SQL, SPARQL, Cypher, and
  MQL
- `./data/dataset/processed_data` contains different data splits, including the responses from the respective databases.
- `./data/dataset/question_templates` contains the 408 question templates used to construct SM3-Text-to-Query.
- `./data/results` contains the results for each of the
  evaluated database systems and query languages for each of the five prompts,
the four LLMs for dev (results on test are not published to not expose the questions)

## Code

- `./src/setup_dbs` contains the code to set up the four different database systems (PostgreSQL, GraphDB, Neo4j, and MongoDB) and populate them with Synthea data.
- `./src/run_experiments` contains the code to
  replicate our experiments for all database models, LLMs, prompts, and few-shot
  sampling (repetitions).
- `./src/evaluation` contains the code to evaluate the
  results obtained by the LLMs for our four databases, including the necessary
  data-cleaning logic. It computes Execution Accuracy (EA) and Valid Efficiency
  Score (VES) for each combination of LLM, database model, and prompt-setting.

## Croissant Metadata

```json
{
  "@context": {
    "@language": "en",
    "@vocab": "https://schema.org/",
    "citeAs": "cr:citeAs",
    "column": "cr:column",
    "conformsTo": "dct:conformsTo",
    "cr": "http://mlcommons.org/croissant/",
    "rai": "http://mlcommons.org/croissant/RAI/",
    "data": {
      "@id": "cr:data",
      "@type": "@json"
    },
    "dataType": {
      "@id": "cr:dataType",
      "@type": "@vocab"
    },
    "dct": "http://purl.org/dc/terms/",
    "examples": {
      "@id": "cr:examples",
      "@type": "@json"
    },
    "extract": "cr:extract",
    "field": "cr:field",
    "fileProperty": "cr:fileProperty",
    "fileObject": "cr:fileObject",
    "fileSet": "cr:fileSet",
    "format": "cr:format",
    "includes": "cr:includes",
    "isLiveDataset": "cr:isLiveDataset",
    "jsonPath": "cr:jsonPath",
    "key": "cr:key",
    "md5": "cr:md5",
    "parentField": "cr:parentField",
    "path": "cr:path",
    "recordSet": "cr:recordSet",
    "references": "cr:references",
    "regex": "cr:regex",
    "repeated": "cr:repeated",
    "replace": "cr:replace",
    "sc": "https://schema.org/",
    "separator": "cr:separator",
    "source": "cr:source",
    "subField": "cr:subField",
    "transform": "cr:transform"
  },
  "@type": "sc:Dataset",
  "name": "SM3-text-to-query",
  "description": "Dataset used in project SM3-text-to-query",
  "conformsTo": "http://mlcommons.org/croissant/1.0",
  "url": "https://github.com/jf87/SM3-Text-to-Query",
  "distribution": [
    {
      "@type": "cr:FileObject",
      "@id": "sm3-text-to-query-train",
      "name": "sm3-text-to-query-train",
      "description": "SM3-Text-to-Query training data on GitHub.",
      "contentUrl": "https://github.com/jf87/SM3-Text-to-Query/blob/main/data/dataset/train_dev/train.csv",
      "encodingFormat": "text/csv",
      "sha256": "sha256"
    },
    {
      "@type": "cr:FileObject",
      "@id": "sm3-text-to-query-val",
      "name": "sm3-text-to-query-val",
      "description": "SM3-Text-to-Query validation data on GitHub.",
      "contentUrl": "https://github.com/jf87/SM3-Text-to-Query/blob/main/data/dataset/train_dev/dev.csv",
      "encodingFormat": "text/csv",
      "sha256": "sha256"
    },
    {
      "@type": "cr:FileObject",
      "@id": "sm3-text-to-query-sample-val",
      "name": "sm3-text-to-query-sample-val",
      "description": "SM3-Text-to-Query sampled validation data on GitHub.",
      "contentUrl": "https://github.com/jf87/SM3-Text-to-Query/blob/main/data/dataset/train_dev/sample_dev.csv",
      "encodingFormat": "text/csv",
      "sha256": "sha256"
    },
    {
      "@type": "cr:FileSet",
      "@id": "csv-files",
      "name": "csv-files",
      "description": "All data in csv format",
      "containedIn": [
        {
          "@id": "sm3-text-to-query-train"
        },
        {
          "@id": "sm3-text-to-query-val"
        },
        {
          "@id": "sm3-text-to-query-sample-val"
        }
      ],
      "encodingFormat": "text/csv",
      "includes": "*.csv"
    }
  ],
  "recordSet": [
    {
      "@type": "cr:RecordSet",
      "@id": "sql",
      "name": "sql",
      "field": [
        {
          "@type": "cr:Field",
          "@id": "csv-files/question",
          "name": "question",
          "description": "Questions of data",
          "dataType": "sc:Text",
          "source": {
            "fileSet": {
              "@id": "csv-files"
            },
            "extract": {
              "column": "question"
            }
          }
        },
        {
          "@type": "cr:Field",
          "@id": "csv-files/sql",
          "name": "sql",
          "description": "SQL queries of data",
          "dataType": "sc:Text",
          "source": {
            "fileSet": {
              "@id": "csv-files"
            },
            "extract": {
              "column": "sql"
            }
          }
        },
        {
          "@type": "cr:Field",
          "@id": "csv-files/sparql",
          "name": "sparql",
          "description": "SPAQL queries of data",
          "dataType": "sc:Text",
          "source": {
            "fileSet": {
              "@id": "csv-files"
            },
            "extract": {
              "column": "sparql"
            }
          }
        },
        {
          "@type": "cr:Field",
          "@id": "csv-files/cypher",
          "name": "cypher",
          "description": "Cypher queries of data",
          "dataType": "sc:Text",
          "source": {
            "fileSet": {
              "@id": "csv-files"
            },
            "extract": {
              "column": "cypher"
            }
          }
        },
        {
          "@type": "cr:Field",
          "@id": "csv-files/mql",
          "name": "mql",
          "description": "MongoDB queries of data",
          "dataType": "sc:Text",
          "source": {
            "fileSet": {
              "@id": "csv-files"
            },
            "extract": {
              "column": "mql"
            }
          }
        },
        {
          "@type": "cr:Field",
          "@id": "data/question_type",
          "name": "question_type",
          "description": "Question types of data",
          "dataType": "sc:Text",
          "source": {
            "fileSet": {
              "@id": "csv-files"
            },
            "extract": {
              "column": "question_type"
            }
          }
        },
        {
          "@type": "cr:Field",
          "@id": "data/class",
          "name": "class",
          "description": "Question classes of data",
          "dataType": "sc:Text",
          "source": {
            "fileSet": {
              "@id": "csv-files"
            },
            "extract": {
              "column": "class"
            }
          }
        }
      ]
    }
  ]
}
```
