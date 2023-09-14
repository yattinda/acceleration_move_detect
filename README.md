# acceleration_move_detect

## 体重と加速度からおおよその消費カロリーを返してくれるAPI

### 利用方法

1. https://acceleration-move-detect.onrender.com/ に以下の形式でJSONをPOSTする
```
{"weight": 60,
 "DATA":[
    {
        "x": 0.2,
        "y": 0.1,
        "z": 0.2
    },
    {
        "x": 0.5,
        "y": 0.1,
        "z": -0.1
    },
  ]
}
```
※weightは体重 <br>
※DATAは0.1秒間隔で取得した３軸加速度(3軸加速度の個数は任意)

2. POSTされたJSONから消費カロリーを自動計算(float)
   例：　5.12333334

### License
The source code is licensed MIT. The website content is licensed CC BY 4.0,see LICENSE.
