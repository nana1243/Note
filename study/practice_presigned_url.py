from typing import Optional

import boto3
import botocore


class S3Client:
    MAX_POOL_CONNECTIONS = 20

    # Check the reference of boto3_config at
    # https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html
    def __init__(self, **boto3_config):
        self._default_boto3_config = botocore.config.Config(
            **{**dict(max_pool_connections=self.MAX_POOL_CONNECTIONS), **boto3_config}
        )
        self.client = boto3.client(
            **load_func(json, s3_config_path), config=self._default_boto3_config
        )


    def generate_presigned_url(
        self,
        bucket_name: str,
        s3_key: str,
        expires_in: int = 300,
        http_method: Optional[str] = None,
        **client_method_params,
    ) -> str:
        """Presigned url을 생성합니다. client method로는 `get_object`를 사용합니다.
        관련 문서:
            `generate_presigned_url`: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.generate_presigned_url  # noqa: E501
            `get_object`: `https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.get_object`  # noqa: E501


        > 다운로드 파일명 변경 예시 (아래 URL로 파일 다운로드 시 `download_filename`으로 다운로드 됩니다.)
        > Content-Disposition 헤더 문서: https://developer.mozilla.org/ko/docs/Web/HTTP/Headers/Content-Disposition  # noqa: E501
        >>> client = S3Client()
        >>> download_filename = "278-edm-deep_house-uplifting_deep_29-music_1.wav"
        >>> presigned_url = client.generate_presigned_url(
        >>>     bucket_name="example_bucket_name",
        >>>     s3_key="example_s3_key",
        >>>     expires_in=300,
        >>>     **{
        >>>         "ResponseContentDisposition": f"attachment; filename={download_filename}",
        >>>     },
        >>> )

        Args:
            bucket_name: `str`. 버켓명
            s3_key: `str`. S3 key
            expires_in: `int`. url 만료 시간 (초)
            http_method: `Optional[str]`. url에 사용될 http method
            client_method_params: `S3.Client.generate_presigned_url`의 `Params`에 전달할 추가 인자
                자세한 인자는 `get_object` 문서 참조
        Returns:
            `str`. 생성된 presigned url. `expires_in` 시간 동안만 유효합니다.
        """
        return self.client.generate_presigned_url(
            ClientMethod="get_object",
            Params={"Bucket": bucket_name, "Key": s3_key, **client_method_params},
            ExpiresIn=expires_in,
            HttpMethod=http_method,
        )
