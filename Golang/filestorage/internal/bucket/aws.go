package bucket

import (
	"context"
	"io"
	"os"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/feature/s3/manager"
	"github.com/aws/aws-sdk-go-v2/service/s3"
)

type AwsConfig struct {
	Config         *aws.Config
	BucketDownload string
	BucketUpload   string
}

func newAwsSession(cfg AwsConfig) *awsSession {
	sess := s3.NewFromConfig(*cfg.Config)

	return &awsSession{
		sess:           sess,
		bucketDownload: cfg.BucketDownload,
		bucketUpload:   cfg.BucketUpload,
	}
}

type awsSession struct {
	sess           *s3.Client
	bucketDownload string
	bucketUpload   string
}

func (as *awsSession) Download(src string, dst string) (file *os.File, err error) {
	file, err = os.Create(dst)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	downloader := manager.NewDownloader(as.sess)
	_, err = downloader.Download(context.Background(), file, &s3.GetObjectInput{
		Bucket: &as.bucketDownload,
		Key:    &src,
	})
	return
}

func (as *awsSession) Upload(file io.Reader, key string) error {
	uploader := manager.NewUploader(as.sess)

	_, err := uploader.Upload(context.Background(), &manager.UploadInput{
		Bucket: &as.bucketUpload,
		Key:    &key,
		Body:   file,
	})

	return err
}

func (as *awsSession) Delete(key string) error {
	_, err := as.sess.DeleteObject(context.Background(), &s3.DeleteObjectInput{
		Bucket: &as.bucketDownload,
		Key:    &key,
	})
	if err != nil {
		return err
	}

	waiter := s3.NewObjectNotExistsWaiter(as.client)
	return waiter.Wait(context.Background(), &s3.HeadObjectInput{
		Bucket: &as.bucketDownload,
		Key:    &key,
	})
}
