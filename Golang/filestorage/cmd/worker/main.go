package main

import (
	"bytes"
	"compress/gzip"
	"fmt"
	"io"
	"log"
	"os"
	"time"

	"github.com/MarcosBan/filestorage/internal/bucket"
	"github.com/MarcosBan/filestorage/internal/queue"
)

func main() {
	qcfg := queue.RabbitMQConfig{
		URL:       os.Getenv("RABBIT_URL"),
		TopicName: os.Getenv("RABBIT_TOPIC_NAME"),
		Timeout:   time.Second * 30,
	}
	qc, err := queue.New(queue.RabbitMQ, qcfg)
	if err != nil {
		panic(err)
	}
	c := make(chan queue.QueueDto)

	qc.Consume(c)

	bcfg := bucket.AwsConfig{
		Config: &aws.Config{
			Region: os.Getenv("AWS_REGION"),
			Credentials: aws.NewCredentialsCache(
				aws.NewStaticCredentialsProvider(
					os.Getenv("AWS_ACCESS_KEY_ID"),
					os.Getenv("AWS_SECRET_ACCESS_KEY"),
					"",
				),
			),
		},
		BucketDownload: "filestorage-raw",
		BucketUpload:   "filestorage-compressed",
	}
	b, err := bucket.New(bucket.AwsProvider, bcfg)
	if err != nil {
		panic(err)
	}
	for msg := range c {
		src := fmt.Sprintf("%s/%s", msg.Path, msg.Filename)
		dst := fmt.Sprintf("%d_%s", msg.ID, msg.Filename)
		file, err := b.Download(src, dst)
		if err != nil {
			log.Printf("ERROR: %v\n", err)
			continue
		}
		body, err := io.ReadAll(file)
		if err != nil {
			log.Printf("ERROR: %v\n", err)
			continue
		}

		var buf bytes.Buffer
		zw := gzip.NewWriter(&buf)
		_, err = zw.Write(body)
		if err != nil {
			log.Printf("ERROR: %v\n", err)
			continue
		}
		if err := zw.Close(); err != nil {
			log.Printf("ERROR: %v\n", err)
			continue
		}

		zr, err := gzip.NewReader(&buf)
		if err != nil {
			log.Printf("ERROR: %v\n", err)
			continue
		}
		err = b.Upload(zr, dst)
		if err != nil {
			log.Printf("ERROR: %v\n", err)
			continue
		}

		os.Remove(dst)
	}
}
