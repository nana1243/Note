

1. 모니터링

1.1 change_stream
```
"""mongodb change stream을 이용해 db 변경사항을 SSE 메시지로 발송합니다.
     change stream 구독 시 공식 문서에서 소개하는 대로 change stream을 순회하면
     그 순간부터 블로킹되기 때문에 외부에서 SSE를 통제할 수 없습니다.
     이를 방지하기 위해 change stream에서 next 호출 시 데이터를 받아오는 메서드를 직접 호출합니다.
     자세한 소스코드는 `pymongo.change_stream.ChangeStream`를 참조하세요.
     References:
         https://docs.mongodb.com/manual/changeStreams/
         https://docs.mongodb.com/manual/reference/change-events/
         https://pymongo.readthedocs.io/en/stable/api/pymongo/change_stream.html
         https://developer.mongodb.com/quickstart/python-change-streams/
         https://itnext.io/how-to-use-mongodb-change-streams-part-2-6a6d049426bb
"""
```
1.2 celery
