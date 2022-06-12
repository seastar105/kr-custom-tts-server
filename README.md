# kr-custom-tts-server

[kr-custom-tts](https://github.com/seastar105/kr-custom-tts)를 사용하여 학습된 모델을 fastAPI와 espnet의 Inference API를 사용하여 API화하는 예제 코드를 담은 레포지토리입니다. 



## 음성합성 모델 세팅

[kr-custom-tts](https://github.com/seastar105/kr-custom-tts)를 따라서 학습을 끝마쳤으면 `exp`폴더에 `tts_finetune_jets_raw_phn_null_g2pk_train.total_count.best.zip` 파일이 있을 것입니다. 

해당 압축 파일을 풀면 아래와 같은 구조를 가진 `exp` 폴더가 있습니다. 

```
exp
├── tts_finetune_jets_raw_phn_null_g2pk
│   ├── 100epoch.pth
│   ├── config.yaml
│   └── images
└── tts_stats_raw_phn_null_g2pk
    └── train
```

여기서 `.pth`로 끝나는 파일이 학습이 끝난 모델입니다. `app/constants.py`의 `MODEL_PATH`를 해당 모델의 경로로 바꿔주세요.

해당 MODEL_PATH에 해당하는 파일이 존재하지 않으면 KSS 데이터셋에 대해 훈련된 모델을 사용합니다.



만약 학습이 다 끝나지 않았지만 모델을 사용해보고 싶다면 아래와 같은 구조로 `exp` 폴더를 만드시고 실행하셔도 사용이 가능합니다.

```
exp
├── tts_finetune_jets_raw_phn_null_g2pk
│   ├── *.pth
│   └── config.yaml
└── tts_stats_raw_phn_null_g2pk
    └── train
```



## 서버 실행 방법

```
pip -r requirements.txt
uvicorn app.main:app --host=0.0.0.0 --port=PORT_NUMBER
```

로 실행하시면 `localhost:PORT_NUMBER/api/tts`로 API를 사용할 수 있습니다. `localhost:PORT_NUMBER`로 접속하시면 index.html이 표시되며 텍스트를 입력하고 버튼을 누르시면 음성 합성을 수행합니다. 제일 처음 실행은 시간이 걸릴 수(약 1분) 있습니다.





### Docker를 사용하는 경우

`docker build -t tts-server .`를 통해 이미지를 만드신 후 다음 커맨드로 서버를 실행해주세요.

```
docker run -d -v $(pwd)/exp:/code/exp -p PORT_NUMBER:80 tts-server
```

`exp` 폴더를 `/code/exp`로 마운트 해주셔야 합니다.

 

