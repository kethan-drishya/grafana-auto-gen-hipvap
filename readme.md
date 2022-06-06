# Dashboard Backend API

## Query a data source

Queries a data source having a backend implementation

### Resource Information

Method and URI - POST [https://hipvap-pilot-test.brains-qa.drishya.ai/api/ds/query](https://hipvap-pilot-test.brains-qa.drishya.ai/api/ds/query)

Data Format - JSON

### Request

#### Headers

Authorization - string - Must be Bearer , where is obtained via OAuth

Content-Type  - string - Must be application/json

#### Body Structure

- from/to – Specifies the time range for the queries. The time can be either epoch timestamps in milliseconds or relative using Grafana time units. For example, now-5m.
- queries – Specifies one or more queries. Must contain at least 1.
- queries.datasource.uid – Specifies the UID of data source to be queried. Each query in the request must have a unique datasource.
- queries.refId – Specifies an identifier of the query. Defaults to “A”.
- queries.format – Specifies the format the data should be returned in. Valid options are time\_series or table depending on the data source.
- queries.maxDataPoints - Specifies the maximum amount of data points that a dashboard panel can render. Defaults to 100.
- queries.intervalMs - Specifies the time series time interval in milliseconds. Defaults to 1000.

### Response Status Codes

Code Description

- 200 - All data source queries returned a successful response
- 400 - Bad request due to invalid JSON, missing content type, missing or invalid fields, etc. Or one or more data source queries were unsuccessful. Refer to the body for more details.
- 403 - Access denied.
- 404 - Either the data source or plugin required to fulfil the request could not be found.
- 500 - Unexpected error. Refer to the body and/or server logs for more details.

### Example Request Body Structure for the Test Data Source

``` json
{
  "queries": [
    {
      "database": "\"qahipvap-timestreamdb\"",
      "datasource": {
        "uid": "P45460985913E4ED4",
        "type": "grafana-timestream-datasource"
      },
      "decimalSeparator": ".",
      "delimiter": ",",
      "header": true,
      "ignoreUnknown": false,
      "measure": "value",
      "rawQuery": "SELECT p.time,round(p.measure_value::double,5) FROM $__database.$__table p where p.tags = '\''FIT-10802_HOT_OIL_RECIRCULATION_PUMP_P-108_DISCHARGE_FLOW_CALCULATED'\'' AND $__timeFilter",
      "refId": "A",
      "schema": [
        {
          "name": "",
          "type": "string"
        }
      ],
      "skipRows": 0,
      "table": "\"qahipvap-pi-data-table-v2\"",
      "datasourceId": 3,
      "intervalMs": 600000,
      "maxDataPoints": 916
    }
  ],
  "range": {
    "from": "2022-05-25T03:45:17.000Z",
    "to": "2022-05-25T03:46:00.000Z",
    "raw": {
      "from": "2022-05-25T03:45:17.000Z",
      "to": "2022-05-25T03:46:00.000Z"
    }
  },
  "from": "1653450317000",
  "to": "1653450360000"
}
```

### Response Body Structure (201)

- results : dict: string
- results.{{refId}}.frames : array:object, Data frame series results of respective refId query
- results.{{refId}}.frames.schema : object, Schema of data table referred by refId query
- results.{{refId}}.frames.schema.fields : array: object, Fields description in the table referred by refId query
- results.{{refId}}.frames.meta : object, Meta Data of query results referred by refId query
- results.{{refId}}.frames.data : array:object, Data received for the query referred by refId
- results.{{refId}}.frames.data.values : array:string, Values of the data received for the query

### Example Response Body:

``` json
{
    "results": {
        "A": {
            "frames": [
                {
                    "schema": {
                        "refId": "A",
                        "meta": {
                            "custom": {
                                "executionFinishTime": 1653453814013,
                                "executionStartTime": 1653453812280,
                                "queryId": "AEDACANEP257UP4K4YXGMOQDOE3XCMDO6FPRRYC662FMWUPDMYV2XX46AXIA64Q",
                                "status": {
                                    "CumulativeBytesMetered": 10000000,
                                    "CumulativeBytesScanned": 651,
                                    "ProgressPercentage": 100
                                }
                            },
                            "executedQueryString": "SELECT p.time,round(p.measure_value::double,5) FROM \"qahipvap-timestreamdb\".\"qahipvap-pi-data-table-v2\" p where p.tags = 'FIT-10802_HOT_OIL_RECIRCULATION_PUMP_P-108_DISCHARGE_FLOW_CALCULATED' AND time BETWEEN from_milliseconds(1653450317000) AND from_milliseconds(1653450360000)"
                        },
                        "fields": [
                            {
                                "name": "time",
                                "type": "time",
                                "typeInfo": {
                                    "frame": "time.Time"
                                }
                            },
                            {
                                "name": "_col1",
                                "type": "number",
                                "typeInfo": {
                                    "frame": "float64",
                                    "nullable": true
                                }
                            }
                        ]
                    },
                    "data": {
                        "values": [
                            [
                                1653450319982,
                                1653450326471,
                                1653450332982,
                                1653450339478,
                                1653450345986,
                                1653450352477,
                                1653450358980
                            ],
                            [
                                136577.03,
                                136577.03,
                                137601.03,
                                138592.27,
                                140673.03,
                                141697.03,
                                137601.03
                            ]
                        ]
                    }
                }
            ]
        }
    }
}
```

### Example Request:
```
curl -v 'https://hipvap-pilot-test.brains-qa.drishya.ai/api/ds/query'\ 

-X 'POST' \ 

-H 'Content-Type: application/json' \ 

-H 'Authorization: Bearer eyJrIjoiRlE2Q0s5aDZZMm8yb0VWYXpsUmh4a0pVYWhnaUliam8iLCJuIjoicWEiLCJpZCI6MX0=' \   
-d '{
  "queries": [
    {
      "database": "\"qahipvap-timestreamdb\"",
      "datasource": {
        "uid": "P45460985913E4ED4",
        "type": "grafana-timestream-datasource"
      },
      "decimalSeparator": ".",
      "delimiter": ",",
      "header": true,
      "ignoreUnknown": false,
      "measure": "value",
      "rawQuery": "SELECT p.time,round(p.measure_value::double,5) FROM $__database.$__table p where p.tags = '\''FIT-10802_HOT_OIL_RECIRCULATION_PUMP_P-108_DISCHARGE_FLOW_CALCULATED'\'' AND $__timeFilter",
      "refId": "A",
      "schema": [
        {
          "name": "",
          "type": "string"
        }
      ],
      "skipRows": 0,
      "table": "\"qahipvap-pi-data-table-v2\"",
      "datasourceId": 3,
      "intervalMs": 600000,
      "maxDataPoints": 916
    }
  ],
  "range": {
    "from": "2022-05-25T03:45:17.000Z",
    "to": "2022-05-25T03:46:00.000Z",
    "raw": {
      "from": "2022-05-25T03:45:17.000Z",
      "to": "2022-05-25T03:46:00.000Z"
    }
  },
  "from": "1653450317000",
  "to": "1653450360000"
}'
```

### Example Response:
```

HTTP/2 200

date: Wed, 25 May 2022 04:55:22 GMT content-type: application/json content-length: 975 

server: nginx/1.20.2 

cache-control: no-cache 

expires: -1 

pragma: no-cache x-content-type-options: nosniff x-frame-options: deny 

x-xss-protection: 1; mode=block 

access-control-allow-headers: Authorization,Accept,Origin,DNT,X-CustomHeader,x- grafana-org-id,Keep-Alive,Content-Type 

access-control-allow-credentials: true 

access-control-allow-methods: GET,POST,OPTIONS,PUT,DELETE,PATCH
{
    "results": {
        "A": {
            "frames": [
                {
                    "schema": {
                        "refId": "A",
                        "meta": {
                            "custom": {
                                "executionFinishTime": 1653453814013,
                                "executionStartTime": 1653453812280,
                                "queryId": "AEDACANEP257UP4K4YXGMOQDOE3XCMDO6FPRRYC662FMWUPDMYV2XX46AXIA64Q",
                                "status": {
                                    "CumulativeBytesMetered": 10000000,
                                    "CumulativeBytesScanned": 651,
                                    "ProgressPercentage": 100
                                }
                            },
                            "executedQueryString": "SELECT p.time,round(p.measure_value::double,5) FROM \"qahipvap-timestreamdb\".\"qahipvap-pi-data-table-v2\" p where p.tags = 'FIT-10802_HOT_OIL_RECIRCULATION_PUMP_P-108_DISCHARGE_FLOW_CALCULATED' AND time BETWEEN from_milliseconds(1653450317000) AND from_milliseconds(1653450360000)"
                        },
                        "fields": [
                            {
                                "name": "time",
                                "type": "time",
                                "typeInfo": {
                                    "frame": "time.Time"
                                }
                            },
                            {
                                "name": "_col1",
                                "type": "number",
                                "typeInfo": {
                                    "frame": "float64",
                                    "nullable": true
                                }
                            }
                        ]
                    },
                    "data": {
                        "values": [
                            [
                                1653450319982,
                                1653450326471,
                                1653450332982,
                                1653450339478,
                                1653450345986,
                                1653450352477,
                                1653450358980
                            ],
                            [
                                136577.03,
                                136577.03,
                                137601.03,
                                138592.27,
                                140673.03,
                                141697.03,
                                137601.03
                            ]
                        ]
                    }
                }
            ]
        }
    }
}
```
